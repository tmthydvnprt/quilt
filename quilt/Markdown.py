"""
Markdown

Custom Markdown Extensions
{: .lead}

Adds both included and custom extensions to `Python-Markdown` :
1. 'markdown.extensions.extra'
2. 'markdown.extensions.nl2br'
3. 'markdown.extensions.sane_lists'
4. 'markdown.extensions.codehilite'
5. 'markdown.extensions.wikilinks'
6. 'markdown.extensions.toc'
7. ChecklistExtension()
8. SuperscriptExtension()
9. StrikethroughExtension()
10. SubscriptExtension()
11. SmallExtension()
12. DeleteExtension()
13. InsertExtension()
14. CiteExtension()
15. HighlightExtension()
16. CustomSpanClassExtension()
17. BlankLineExtension()
18. 'markdown.extensions.footnotes'
19. AetherExtension()

"""
import re
import sys

sys.path.insert(1, '/Users/timothydavenport/GitHub/Python-Markdown/')
import markdown
from markdown.util import AMP_SUBSTITUTE, etree, AtomicString
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown.inlinepatterns import Pattern
from markdown.inlinepatterns import SimpleTagPattern

from quilt.Constants import CHECKBOX_RE, MD_INLINE_TAGS, MULTIMATCH_RE, SYMBOLS, SYMBOLS_RE
from quilt.Constants import CUSTOM_CLS_RE, REPLACE_TAGS, REPLACE_TAGS_RE, MATHS_RE

def convert_checkbox(match=None):
    """handle checkbox logic"""
    checked = ' checked' if match.group(1) != ' ' else ''
    return '<li><input type="checkbox" %s>' % (checked)

class ChecklistPostprocessor(Postprocessor):
    """post process to add checklist class to list element"""
    def run(self, html):
        """post process"""
        html = re.sub(CHECKBOX_RE, convert_checkbox, html)
        before = '<ul>\n<li><input type="checkbox"'
        after = before.replace('<ul>', '<ul class="checklist">')
        return html.replace(before, after)

class MultiPattern(Pattern):
    """match multiple patterns"""
    def handleMatch(self, m):
        """handle matched inline pattern"""
        # find which match
        tag = MD_INLINE_TAGS[m.group(2)]
        # create element
        elem = etree.Element(tag)
        elem.text = m.group(3)
        return elem

class ReplacePattern(Pattern):
    """match multiple patterns"""
    def handleMatch(self, m):
        """handle matched inline pattern"""
        # find which match
        tag = REPLACE_TAGS[m.group(2)]
        # create element
        elem = etree.Element(tag)
        return elem

class CustomSpanPattern(Pattern):
    """custom span pattern"""
    def handleMatch(self, matched):
        """handle matched inline pattern"""
        elem = etree.Element("span")
        elem.set("class", matched.group("class"))
        elem.text = AtomicString(matched.group("text"))
        return elem

class SymbolPattern(Pattern):
    """match symbols and replace html entities"""
    def handleMatch(self, m):
        """replace match with span.symbol"""
        node = etree.Element('span')
        node.set('class', 'symbol')
        node.text = SYMBOLS[m.group(2)] % (AMP_SUBSTITUTE)
        return node

class MathsPattern(SimpleTagPattern):
    """match LaTeX math patterns"""
    def handleMatch(self, m):
        """replace match with span.maths """
        node = etree.Element(self.tag)
        node.set('class', 'maths')
        node.text = AtomicString(m.group(2)+m.group(3)+m.group(4))
        return node

class ChecklistExtension(Extension):
    """adds checkbox to markdown list (e.g. [x] checked or [ ] unchecked)"""
    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns."""
        md.postprocessors.add('checklist', ChecklistPostprocessor(md), '>raw_html')
        return self

class MultiExtension(Extension):
    """extension: multiple matches"""
    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns."""
        md.inlinePatterns.add('multi', MultiPattern(MULTIMATCH_RE), '>not_strong')

class CustomSpanExtension(Extension):
    """Adds custom span extension to Markdown class"""
    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns."""
        md.inlinePatterns.add('custom_span', CustomSpanPattern(CUSTOM_CLS_RE, md), '>not_strong')

class ReplaceTagsExtension(Extension):
    """Adds line break extension to Markdown class."""
    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns."""
        md.inlinePatterns.add('replacement_tags', ReplacePattern(REPLACE_TAGS_RE), '>not_strong')

class SymbolExtension(Extension):
    """pre process to add checklist class to list element"""
    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns"""
        md.inlinePatterns.add('symbols', SymbolPattern(SYMBOLS_RE), '>not_strong')

class MathExtension(Extension):
    """ create mathjax extension"""
    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns"""
        md.inlinePatterns.add('inlinemaths', MathsPattern(MATHS_RE, 'span'), '<escape')
        return self

MD_EXT = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.sane_lists',
    'markdown.extensions.codehilite',
    'markdown.extensions.wikilinks',
    'markdown.extensions.toc',
    ChecklistExtension(),
    CustomSpanExtension(),
    ReplaceTagsExtension(),
    'markdown.extensions.footnotes',
    SymbolExtension(),
    MultiExtension(),
    MathExtension()
]

MD_EXT_CONFIG = {
    'markdown.extensions.codehilite': {
        'guess_lang': True,
        'use_pygments': False
    },
    'markdown.extensions.footnotes': {
        'PLACE_MARKER': '///footnotes///'
    },
    'markdown.extensions.toc': {
        'permalink': '%ssect;' % (AMP_SUBSTITUTE)
    },
    'markdown.extensions.wikilinks': {
        'base_url': 'http://en.wikipedia.org/wiki/',
        'end_url': ''
    }
}

MD = markdown.Markdown(
    extensions=MD_EXT,
    extension_configs=MD_EXT_CONFIG,
    output_format="html5",
    laxy_ol=False
)
