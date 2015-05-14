title: quilt
description: a python based static site html code stitcher

<div class="jumbotron">
    <div class="container">
        <div class="row">
            <div class="col-xs-6 col-sm-4 text-center">
                <h2><code>,,,,,,,<br>;#~#~#;<br>;~#~#~;<br>;#~#~#;<br>'''''''</code></h2>
            </div>
            <div class="col-xs-6 col-sm-4">
                <h2><br></h2>
                <h1>{{name}}</h1>
                <p>A <code>python</code> based static site <code>html</code> <em>stitcher</em>.</p>
            </div>
            <div class="col-sm-4 hidden-xs">
                <ul>
                    <li class="dir"><code>site_files/</code><br/>
                        <ul>
                            <li class="file"><code>config.json</code><br/></li>
                            <li class="file"><code>quilt.html</code><br/></li>
                            <li class="dir"><code>assets/</code><br/>
                                <ul class="list-inline keeppad">
                                    <li class="dir"><code>css/</code><br/></li>
                                    <li class="dir"><code>js/</code><br/></li>
                                    <li class="dir"><code>imgs/</code><br/></li>
                                </ul>
                            </li>
                            <li class="dir"><code>pages/</code><br/>
                                <ul class="list-inline keeppad">
                                    <li class="file"><code>index.html</code><br/></li>
                                    <li class="dir"><code>posts/</code><br/></li>
                                    <li class="file"><span class="symbol">&hellip;</span><br/></li>
                                </ul>
                            </li>
                            <li class="dir"><code>patches/</code><br/>
                                <ul class="list-inline keeppad">
                                    <li class="file"><code>head.html</code><br/></li>
                                    <li class="file"><code>nav.html</code><br/></li>
                                    <li class="file"><code>scripts.html</code><br/></li>
                                    <li class="file"><span class="symbol">&hellip;</span><br/></li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
<div class="container">
    <div class="row">
        <div class="col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
            <h2>What is quilt? <small> &mdash; <em>another</em> static site generator</small></h2>
            <p class="lead">Generate a static site via <code>python</code> from content-only <code>html</code> and <code>markdown</code> pages that are <em>stitched</em> together along with patch <small>(e.g. <code>nav.html</code>, <code>footer.html</code>)</small> files onto a main site <code>quilt.html</code> file.</p>
            <h3>Why? <small>cause there's a bunch of <strong>other</strong> static site generators already!</small></h3>
            <h5>Because I wanted...</h5>
            <ol class="list-inline">
                <li>1. specific features</li>
                <li>2. something I didn't see in others</li>
                <li>3. to improve python fluency</li>
                <li>4. homegrown customization</li>
            </ol>
            <h2>Notable features</h2>
            <ul class="checklist">
                <li><input checked="" type="checkbox">focus on page content, site features (head, navbar, footer) are written &amp; stored separately</li>
                <li><input checked="" type="checkbox">write content in <mark><code>html</code> or <code>markdown</code></mark></li>
                <li><input checked="" type="checkbox">extensible markdown for custom needs</li>
                <li><input checked="" type="checkbox"><mark>\(\LaTeX\) Support</mark></li>
                <li><input checked="" type="checkbox">unique template overrides in each directory</li>
                <li><input checked="" type="checkbox">automatically fill <code>alt</code>/<code>img</code> attributes, and remove empty tags</li>
                <li><input checked="" type="checkbox">automatically vendorize, minimize, &amp; combine <code>css</code> and <code>js</code> files</li>
                <li><input checked="" type="checkbox">automatically create certain files (<code>robot.txt</code>, <code>sitemap.xml</code>, multiple sized favicons, etc.)</li>
                <li><input checked="" type="checkbox">provide some dynamic <em>blogy</em> abilities (reverse chronology, tags, categories)</li>
                <li><input checked="" type="checkbox">create atom/rss feeds</li>
                <li><input checked="" type="checkbox">index the text of final site for searching (e.g. with <a href="https://twitter.github.io/typeahead.js/" target="_blank"><code>typeahead</code></a>)</li>
                <li><input type="checkbox"><mark>potential for <a href="http://www.nltk.org" target="_blank"><code>nltk</code></a> integration</mark></li>
                <li><input checked="" type="checkbox">spell checking</li>
                <li><input type="checkbox"><mark>parallel processing</mark></li>
                <li><input type="checkbox"><em>any ideas?</em></li>
                <li><input type="checkbox"></li>
            </ul>
            <p>Check out all the features and what's coming up on the <a href="features_todo.html">features+todo</a> page.</p>
            <h2>Want an example?</h2>
            <div class="alert alert-success">
                <p>This site was <em>stitched</em> with quilt!  Download or inspect the source.</p>
            </div>
            <h2>Want to learn more?</h2>
            <p class="lead">Get an overview on the <a href="readme.html">about(readme)</a> page, or read the full <a href="docs/index.html">documentation</a>.</p>
        </div>        
    </div>
</div>