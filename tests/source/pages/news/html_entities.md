title:       HTML Entities
date:        3/18/2015 5:46 am
description: List of html entities
author:      tim
categories:  example
tags:        markdown
             html
             entities
             BeautifulSoup

# {{title}} <br><small>{{description}}</small>
by {{author}} <small>on {{date}}</small>
{: .h4}
****************************************************************************************************************

<div id="post" markdown="1">

This list of `html` entities is for reference and testing of entity handling.
{: .lead}

Name     | Character  | `HTML` (quilt shortcut)   | Unicode hex (decimal) | Description
---------|------------|---------------------------|-----------------------|---------------------------------------------------------------------
quot     | &quot;     | `&quot;`                  | \x0022 (34)           | quotation mark (APL quote)
amp      | &amp;      | `&amp;`                   | \x0026 (38)           | ampersand
apos     | &apos;     | `&apos;`                  | \x0027 (39)           | apostrophe (apostrophe-quote); see below
lt       | &lt;       | `&lt;`                    | \x003C (60)           | less-than sign
gt       | &gt;       | `&gt;`                    | \x003E (62)           | greater-than sign
nbsp     | &nbsp;     | `&nbsp;`                  | \x00A0 (160)          | no-break space (non-breaking space)
iexcl    | &iexcl;    | `&iexcl;`                 | \x00A1 (161)          | inverted exclamation mark
cent     | &cent;     | `&cent;`                  | \x00A2 (162)          | cent sign
pound    | &pound;    | `&pound;`                 | \x00A3 (163)          | pound sign
curren   | &curren;   | `&curren;`                | \x00A4 (164)          | currency sign
yen      | &yen;      | `&yen;`                   | \x00A5 (165)          | yen sign (yuan sign)
brvbar   | &brvbar;   | `&brvbar;`                | \x00A6 (166)          | broken bar (broken vertical bar)
sect     | &sect;     | `&sect;`                  | \x00A7 (167)          | section sign
uml      | &uml;      | `&uml;`                   | \x00A8 (168)          | diaeresis (spacing diaeresis); see Germanic umlaut
copy     | &copy;     | `&copy;` (`(c)`)          | \x00A9 (169)          | copyright symbol
ordf     | &ordf;     | `&ordf;`                  | \x00AA (170)          | feminine ordinal indicator
laquo    | &laquo;    | `&laquo;`                 | \x00AB (171)          | left-pointing double angle quotation mark (left pointing guillemet)
not      | &not;      | `&not;`                   | \x00AC (172)          | not sign
shy      | &shy;      | `&shy;`                   | \x00AD (173)          | soft hyphen (discretionary hyphen)
reg      | &reg;      | `&reg;` (`(r)`)           | \x00AE (174)          | registered sign (registered trademark symbol)
macr     | &macr;     | `&macr;`                  | \x00AF (175)          | macron (spacing macron, overline, APL overbar)
deg      | &deg;      | `&deg;` (`(d)` or (`(o)`) | \x00B0 (176)          | degree symbol
plusmn   | &plusmn;   | `&plusmn;` (`+-`)         | \x00B1 (177)          | plus-minus sign (plus-or-minus sign)
sup2     | &sup2;     | `&sup2;`                  | \x00B2 (178)          | superscript two (superscript digit two, squared)
sup3     | &sup3;     | `&sup3;`                  | \x00B3 (179)          | superscript three (superscript digit three, cubed)
acute    | &acute;    | `&acute;`                 | \x00B4 (180)          | acute accent (spacing acute)
micro    | &micro;    | `&micro;`                 | \x00B5 (181)          | micro sign
para     | &para;     | `&para;`                  | \x00B6 (182)          | pilcrow sign (paragraph sign)
middot   | &middot;   | `&middot;`                | \x00B7 (183)          | middle dot (Georgian comma, Greek middle dot)
cedil    | &cedil;    | `&cedil;`                 | \x00B8 (184)          | cedilla (spacing cedilla)
sup1     | &sup1;     | `&sup1;`                  | \x00B9 (185)          | superscript one (superscript digit one)
ordm     | &ordm;     | `&ordm;`                  | \x00BA (186)          | masculine ordinal indicator
raquo    | &raquo;    | `&raquo;`                 | \x00BB (187)          | right-pointing double angle quotation mark (right pointing guillemet)
frac14   | &frac14;   | `&frac14;` (`(1/4)`)      | \x00BC (188)          | vulgar fraction one quarter (fraction one quarter)
frac12   | &frac12;   | `&frac12;` (`(1/2)`)      | \x00BD (189)          | vulgar fraction one half (fraction one half)
frac34   | &frac34;   | `&frac34;` (`(3/4)`)      | \x00BE (190)          | vulgar fraction three quarters (fraction three quarters)
iquest   | &iquest;   | `&iquest;`                | \x00BF (191)          | inverted question mark (turned question mark)
Agrave   | &Agrave;   | `&Agrave;`                | \x00C0 (192)          | Latin capital letter A with grave accent (Latin capital letter A grave)
Aacute   | &Aacute;   | `&Aacute;`                | \x00C1 (193)          | Latin capital letter A with acute accent
Acirc    | &Acirc;    | `&Acirc;`                 | \x00C2 (194)          | Latin capital letter A with circumflex
Atilde   | &Atilde;   | `&Atilde;`                | \x00C3 (195)          | Latin capital letter A with tilde
Auml     | &Auml;     | `&Auml;`                  | \x00C4 (196)          | Latin capital letter A with diaeresis
Aring    | &Aring;    | `&Aring;`                 | \x00C5 (197)          | Latin capital letter A with ring above (Latin capital letter A ring)
AElig    | &AElig;    | `&AElig;`                 | \x00C6 (198)          | Latin capital letter AE (Latin capital ligature AE)
Ccedil   | &Ccedil;   | `&Ccedil;`                | \x00C7 (199)          | Latin capital letter C with cedilla
Egrave   | &Egrave;   | `&Egrave;`                | \x00C8 (200)          | Latin capital letter E with grave accent
Eacute   | &Eacute;   | `&Eacute;`                | \x00C9 (201)          | Latin capital letter E with acute accent
Ecirc    | &Ecirc;    | `&Ecirc;`                 | \x00CA (202)          | Latin capital letter E with circumflex
Euml     | &Euml;     | `&Euml;`                  | \x00CB (203)          | Latin capital letter E with diaeresis
Igrave   | &Igrave;   | `&Igrave;`                | \x00CC (204)          | Latin capital letter I with grave accent
Iacute   | &Iacute;   | `&Iacute;`                | \x00CD (205)          | Latin capital letter I with acute accent
Icirc    | &Icirc;    | `&Icirc;`                 | \x00CE (206)          | Latin capital letter I with circumflex
Iuml     | &Iuml;     | `&Iuml;`                  | \x00CF (207)          | Latin capital letter I with diaeresis
ETH      | &ETH;      | `&ETH;`                   | \x00D0 (208)          | Latin capital letter Eth
Ntilde   | &Ntilde;   | `&Ntilde;`                | \x00D1 (209)          | Latin capital letter N with tilde
Ograve   | &Ograve;   | `&Ograve;`                | \x00D2 (210)          | Latin capital letter O with grave accent
Oacute   | &Oacute;   | `&Oacute;`                | \x00D3 (211)          | Latin capital letter O with acute accent
Ocirc    | &Ocirc;    | `&Ocirc;`                 | \x00D4 (212)          | Latin capital letter O with circumflex
Otilde   | &Otilde;   | `&Otilde;`                | \x00D5 (213)          | Latin capital letter O with tilde
Ouml     | &Ouml;     | `&Ouml;`                  | \x00D6 (214)          | Latin capital letter O with diaeresis
times    | &times;    | `&times;` (`(x)`)         | \x00D7 (215)          | multiplication sign
Oslash   | &Oslash;   | `&Oslash;`                | \x00D8 (216)          | Latin capital letter O with stroke (Latin capital letter O slash)
Ugrave   | &Ugrave;   | `&Ugrave;`                | \x00D9 (217)          | Latin capital letter U with grave accent
Uacute   | &Uacute;   | `&Uacute;`                | \x00DA (218)          | Latin capital letter U with acute accent
Ucirc    | &Ucirc;    | `&Ucirc;`                 | \x00DB (219)          | Latin capital letter U with circumflex
Uuml     | &Uuml;     | `&Uuml;`                  | \x00DC (220)          | Latin capital letter U with diaeresis
Yacute   | &Yacute;   | `&Yacute;`                | \x00DD (221)          | Latin capital letter Y with acute accent
THORN    | &THORN;    | `&THORN;`                 | \x00DE (222)          | Latin capital letter THORN
szlig    | &szlig;    | `&szlig;`                 | \x00DF (223)          | Latin small letter sharp s (ess-zed); see German Eszett
agrave   | &agrave;   | `&agrave;`                | \x00E0 (224)          | Latin small letter a with grave accent
aacute   | &aacute;   | `&aacute;`                | \x00E1 (225)          | Latin small letter a with acute accent
acirc    | &acirc;    | `&acirc;`                 | \x00E2 (226)          | Latin small letter a with circumflex
atilde   | &atilde;   | `&atilde;`                | \x00E3 (227)          | Latin small letter a with tilde
auml     | &auml;     | `&auml;`                  | \x00E4 (228)          | Latin small letter a with diaeresis
aring    | &aring;    | `&aring;`                 | \x00E5 (229)          | Latin small letter a with ring above
aelig    | &aelig;    | `&aelig;`                 | \x00E6 (230)          | Latin small letter ae (Latin small ligature ae)
ccedil   | &ccedil;   | `&ccedil;`                | \x00E7 (231)          | Latin small letter c with cedilla
egrave   | &egrave;   | `&egrave;`                | \x00E8 (232)          | Latin small letter e with grave accent
eacute   | &eacute;   | `&eacute;`                | \x00E9 (233)          | Latin small letter e with acute accent
ecirc    | &ecirc;    | `&ecirc;`                 | \x00EA (234)          | Latin small letter e with circumflex
euml     | &euml;     | `&euml;`                  | \x00EB (235)          | Latin small letter e with diaeresis
igrave   | &igrave;   | `&igrave;`                | \x00EC (236)          | Latin small letter i with grave accent
iacute   | &iacute;   | `&iacute;`                | \x00ED (237)          | Latin small letter i with acute accent
icirc    | &icirc;    | `&icirc;`                 | \x00EE (238)          | Latin small letter i with circumflex
iuml     | &iuml;     | `&iuml;`                  | \x00EF (239)          | Latin small letter i with diaeresis
eth      | &eth;      | `&eth;`                   | \x00F0 (240)          | Latin small letter eth
ntilde   | &ntilde;   | `&ntilde;`                | \x00F1 (241)          | Latin small letter n with tilde
ograve   | &ograve;   | `&ograve;`                | \x00F2 (242)          | Latin small letter o with grave accent
oacute   | &oacute;   | `&oacute;`                | \x00F3 (243)          | Latin small letter o with acute accent
ocirc    | &ocirc;    | `&ocirc;`                 | \x00F4 (244)          | Latin small letter o with circumflex
otilde   | &otilde;   | `&otilde;`                | \x00F5 (245)          | Latin small letter o with tilde
ouml     | &ouml;     | `&ouml;`                  | \x00F6 (246)          | Latin small letter o with diaeresis
divide   | &divide;   | `&divide;` (`(/)`)        | \x00F7 (247)          | division sign (obelus)
oslash   | &oslash;   | `&oslash;`                | \x00F8 (248)          | Latin small letter o with stroke (Latin small letter o slash)
ugrave   | &ugrave;   | `&ugrave;`                | \x00F9 (249)          | Latin small letter u with grave accent
uacute   | &uacute;   | `&uacute;`                | \x00FA (250)          | Latin small letter u with acute accent
ucirc    | &ucirc;    | `&ucirc;`                 | \x00FB (251)          | Latin small letter u with circumflex
uuml     | &uuml;     | `&uuml;`                  | \x00FC (252)          | Latin small letter u with diaeresis
yacute   | &yacute;   | `&yacute;`                | \x00FD (253)          | Latin small letter y with acute accent
thorn    | &thorn;    | `&thorn;`                 | \x00FE (254)          | Latin small letter thorn
yuml     | &yuml;     | `&yuml;`                  | \x00FF (255)          | Latin small letter y with diaeresis
OElig    | &OElig;    | `&OElig;`                 | \x0152 (338)          | Latin capital ligature oe
oelig    | &oelig;    | `&oelig;`                 | \x0153 (339)          | Latin small ligature oe
Scaron   | &Scaron;   | `&Scaron;`                | \x0160 (352)          | Latin capital letter s with caron
scaron   | &scaron;   | `&scaron;`                | \x0161 (353)          | Latin small letter s with caron
Yuml     | &Yuml;     | `&Yuml;`                  | \x0178 (376)          | Latin capital letter y with diaeresis
fnof     | &fnof;     | `&fnof;` (`(f)`)          | \x0192 (402)          | Latin small letter f with hook (function, florin)
circ     | &circ;     | `&circ;`                  | \x02C6 (710)          | modifier letter circumflex accent
tilde    | &tilde;    | `&tilde;`                 | \x02DC (732)          | small tilde
Alpha    | &Alpha;    | `&Alpha;`                 | \x0391 (913)          | Greek capital letter Alpha
Beta     | &Beta;     | `&Beta;`                  | \x0392 (914)          | Greek capital letter Beta
Gamma    | &Gamma;    | `&Gamma;`                 | \x0393 (915)          | Greek capital letter Gamma
Delta    | &Delta;    | `&Delta;`                 | \x0394 (916)          | Greek capital letter Delta
Epsilon  | &Epsilon;  | `&Epsilon;`               | \x0395 (917)          | Greek capital letter Epsilon
Zeta     | &Zeta;     | `&Zeta;`                  | \x0396 (918)          | Greek capital letter Zeta
Eta      | &Eta;      | `&Eta;`                   | \x0397 (919)          | Greek capital letter Eta
Theta    | &Theta;    | `&Theta;`                 | \x0398 (920)          | Greek capital letter Theta
Iota     | &Iota;     | `&Iota;`                  | \x0399 (921)          | Greek capital letter Iota
Kappa    | &Kappa;    | `&Kappa;`                 | \x039A (922)          | Greek capital letter Kappa
Lambda   | &Lambda;   | `&Lambda;`                | \x039B (923)          | Greek capital letter Lambda
Mu       | &Mu;       | `&Mu;`                    | \x039C (924)          | Greek capital letter Mu
Nu       | &Nu;       | `&Nu;`                    | \x039D (925)          | Greek capital letter Nu
Xi       | &Xi;       | `&Xi;`                    | \x039E (926)          | Greek capital letter Xi
Omicron  | &Omicron;  | `&Omicron;`               | \x039F (927)          | Greek capital letter Omicron
Pi       | &Pi;       | `&Pi;`                    | \x03A0 (928)          | Greek capital letter Pi
Rho      | &Rho;      | `&Rho;`                   | \x03A1 (929)          | Greek capital letter Rho
Sigma    | &Sigma;    | `&Sigma;`                 | \x03A3 (931)          | Greek capital letter Sigma
Tau      | &Tau;      | `&Tau;`                   | \x03A4 (932)          | Greek capital letter Tau
Upsilon  | &Upsilon;  | `&Upsilon;`               | \x03A5 (933)          | Greek capital letter Upsilon
Phi      | &Phi;      | `&Phi;`                   | \x03A6 (934)          | Greek capital letter Phi
Chi      | &Chi;      | `&Chi;`                   | \x03A7 (935)          | Greek capital letter Chi
Psi      | &Psi;      | `&Psi;`                   | \x03A8 (936)          | Greek capital letter Psi
Omega    | &Omega;    | `&Omega;`                 | \x03A9 (937)          | Greek capital letter Omega
alpha    | &alpha;    | `&alpha;`                 | \x03B1 (945)          | Greek small letter alpha
beta     | &beta;     | `&beta;`                  | \x03B2 (946)          | Greek small letter beta
gamma    | &gamma;    | `&gamma;`                 | \x03B3 (947)          | Greek small letter gamma
delta    | &delta;    | `&delta;`                 | \x03B4 (948)          | Greek small letter delta
epsilon  | &epsilon;  | `&epsilon;`               | \x03B5 (949)          | Greek small letter epsilon
zeta     | &zeta;     | `&zeta;`                  | \x03B6 (950)          | Greek small letter zeta
eta      | &eta;      | `&eta;`                   | \x03B7 (951)          | Greek small letter eta
theta    | &theta;    | `&theta;`                 | \x03B8 (952)          | Greek small letter theta
iota     | &iota;     | `&iota;`                  | \x03B9 (953)          | Greek small letter iota
kappa    | &kappa;    | `&kappa;`                 | \x03BA (954)          | Greek small letter kappa
lambda   | &lambda;   | `&lambda;`                | \x03BB (955)          | Greek small letter lambda
mu       | &mu;       | `&mu;`                    | \x03BC (956)          | Greek small letter mu
nu       | &nu;       | `&nu;`                    | \x03BD (957)          | Greek small letter nu
xi       | &xi;       | `&xi;`                    | \x03BE (958)          | Greek small letter xi
omicron  | &omicron;  | `&omicron;`               | \x03BF (959)          | Greek small letter omicron
pi       | &pi;       | `&pi;`                    | \x03C0 (960)          | Greek small letter pi
rho      | &rho;      | `&rho;`                   | \x03C1 (961)          | Greek small letter rho
sigmaf   | &sigmaf;   | `&sigmaf;`                | \x03C2 (962)          | Greek small letter final sigma
sigma    | &sigma;    | `&sigma;`                 | \x03C3 (963)          | Greek small letter sigma
tau      | &tau;      | `&tau;`                   | \x03C4 (964)          | Greek small letter tau
upsilon  | &upsilon;  | `&upsilon;`               | \x03C5 (965)          | Greek small letter upsilon
phi      | &phi;      | `&phi;`                   | \x03C6 (966)          | Greek small letter phi
chi      | &chi;      | `&chi;`                   | \x03C7 (967)          | Greek small letter chi
psi      | &psi;      | `&psi;`                   | \x03C8 (968)          | Greek small letter psi
omega    | &omega;    | `&omega;`                 | \x03C9 (969)          | Greek small letter omega
thetasym | &thetasym; | `&thetasym;`              | \x03D1 (977)          | Greek theta symbol
upsih    | &upsih;    | `&upsih;`                 | \x03D2 (978)          | Greek Upsilon with hook symbol
piv      | &piv;      | `&piv;`                   | \x03D6 (982)          | Greek pi symbol
ensp     | &ensp;     | `&ensp;`                  | \x2002 (8194)         | en space
emsp     | &emsp;     | `&emsp;`                  | \x2003 (8195)         | em space
thinsp   | &thinsp;   | `&thinsp;`                | \x2009 (8201)         | thin space
zwnj     | &zwnj;     | `&zwnj;`                  | \x200C (8204)         | zero-width non-joiner
zwj      | &zwj;      | `&zwj;`                   | \x200D (8205)         | zero-width joiner
lrm      | &lrm;      | `&lrm;`                   | \x200E (8206)         | left-to-right mark
rlm      | &rlm;      | `&rlm;`                   | \x200F (8207)         | right-to-left mark
ndash    | &ndash;    | `&ndash;` (`--`)          | \x2013 (8211)         | en dash
mdash    | &mdash;    | `&mdash;` (`---`)         | \x2014 (8212)         | em dash
lsquo    | &lsquo;    | `&lsquo;`                 | \x2018 (8216)         | left single quotation mark
rsquo    | &rsquo;    | `&rsquo;`                 | \x2019 (8217)         | right single quotation mark
sbquo    | &sbquo;    | `&sbquo;`                 | \x201A (8218)         | single low-9 quotation mark
ldquo    | &ldquo;    | `&ldquo;`                 | \x201C (8220)         | left double quotation mark
rdquo    | &rdquo;    | `&rdquo;`                 | \x201D (8221)         | right double quotation mark
bdquo    | &bdquo;    | `&bdquo;`                 | \x201E (8222)         | double low-9 quotation mark
dagger   | &dagger;   | `&dagger;` (`(t)`)        | \x2020 (8224)         | dagger, obelisk
Dagger   | &Dagger;   | `&Dagger;` (`(tt)`)       | \x2021 (8225)         | double dagger, double obelisk
bull     | &bull;     | `&bull;`                  | \x2022 (8226)         | bullet (black small circle)
hellip   | &hellip;   | `&hellip;` (`...`)        | \x2026 (8230)         | horizontal ellipsis (three dot leader)
permil   | &permil;   | `&permil;`                | \x2030 (8240)         | per mille sign
prime    | &prime;    | `&prime;`                 | \x2032 (8242)         | prime (minutes, feet)
Prime    | &Prime;    | `&Prime;`                 | \x2033 (8243)         | double prime (seconds, inches)
lsaquo   | &lsaquo;   | `&lsaquo;`                | \x2039 (8249)         | single left-pointing angle quotation mark
rsaquo   | &rsaquo;   | `&rsaquo;`                | \x203A (8250)         | single right-pointing angle quotation mark
oline    | &oline;    | `&oline;`                 | \x203E (8254)         | overline (spacing overscore)
frasl    | &frasl;    | `&frasl;`                 | \x2044 (8260)         | fraction slash (solidus)
euro     | &euro;     | `&euro;`                  | \x20AC (8364)         | euro sign
image    | &image;    | `&image;`                 | \x2111 (8465)         | black-letter capital I (imaginary part)
weierp   | &weierp;   | `&weierp;`                | \x2118 (8472)         | script capital P (power set, Weierstrass p)
real     | &real;     | `&real;`                  | \x211C (8476)         | black-letter capital R (real part symbol)
trade    | &trade;    | `&trade;` (`(tm)`)        | \x2122 (8482)         | trademark symbol
alefsym  | &alefsym;  | `&alefsym;`               | \x2135 (8501)         | alef symbol (first transfinite cardinal)
larr     | &larr;     | `&larr;` (`(<)`)          | \x2190 (8592)         | leftwards arrow
uarr     | &uarr;     | `&uarr;` (`(^)`)          | \x2191 (8593)         | upwards arrow
rarr     | &rarr;     | `&rarr;` (`(>)`)          | \x2192 (8594)         | rightwards arrow
darr     | &darr;     | `&darr;` (`(v)`)          | \x2193 (8595)         | downwards arrow
harr     | &harr;     | `&harr;` (`(<>)`)         | \x2194 (8596)         | left right arrow
crarr    | &crarr;    | `&crarr;`                 | \x21B5 (8629)         | downwards arrow with corner leftwards (carriage return)
lArr     | &lArr;     | `&lArr;`                  | \x21D0 (8656)         | leftwards double arrow
uArr     | &uArr;     | `&uArr;`                  | \x21D1 (8657)         | upwards double arrow
rArr     | &rArr;     | `&rArr;`                  | \x21D2 (8658)         | rightwards double arrow
dArr     | &dArr;     | `&dArr;`                  | \x21D3 (8659)         | downwards double arrow
hArr     | &hArr;     | `&hArr;`                  | \x21D4 (8660)         | left right double arrow
forall   | &forall;   | `&forall;`                | \x2200 (8704)         | for all
part     | &part;     | `&part;`                  | \x2202 (8706)         | partial differential
exist    | &exist;    | `&exist;`                 | \x2203 (8707)         | there exists
empty    | &empty;    | `&empty;`                 | \x2205 (8709)         | empty set (null set); see also \x8960, ⌀
nabla    | &nabla;    | `&nabla;`                 | \x2207 (8711)         | del or nabla (vector differential operator)
isin     | &isin;     | `&isin;`                  | \x2208 (8712)         | element of
notin    | &notin;    | `&notin;`                 | \x2209 (8713)         | not an element of
ni       | &ni;       | `&ni;`                    | \x220B (8715)         | contains as member
prod     | &prod;     | `&prod;`                  | \x220F (8719)         | n-ary product (product sign)
sum      | &sum;      | `&sum;`                   | \x2211 (8721)         | n-ary summation
minus    | &minus;    | `&minus;`                 | \x2212 (8722)         | minus sign
lowast   | &lowast;   | `&lowast;`                | \x2217 (8727)         | asterisk operator
radic    | &radic;    | `&radic;`                 | \x221A (8730)         | square root (radical sign)
prop     | &prop;     | `&prop;`                  | \x221D (8733)         | proportional to
infin    | &infin;    | `&infin;` (`(oo)`)        | \x221E (8734)         | infinity
ang      | &ang;      | `&ang;`                   | \x2220 (8736)         | angle
and      | &and;      | `&and;`                   | \x2227 (8743)         | logical and (wedge)
or       | &or;       | `&or;`                    | \x2228 (8744)         | logical or (vee)
cap      | &cap;      | `&cap;`                   | \x2229 (8745)         | intersection (cap)
cup      | &cup;      | `&cup;`                   | \x222A (8746)         | union (cup)
int      | &int;      | `&int;`                   | \x222B (8747)         | integral
there4   | &there4;   | `&there4;`                | \x2234 (8756)         | therefore sign
sim      | &sim;      | `&sim;`                   | \x223C (8764)         | tilde operator (varies with, similar to)
cong     | &cong;     | `&cong;`                  | \x2245 (8773)         | congruent to
asymp    | &asymp;    | `&asymp;`                 | \x2248 (8776)         | almost equal to (asymptotic to)
ne       | &ne;       | `&ne;`                    | \x2260 (8800)         | not equal to
equiv    | &equiv;    | `&equiv;`                 | \x2261 (8801)         | identical to; sometimes used for 'equivalent to'
le       | &le;       | `&le;`                    | \x2264 (8804)         | less-than or equal to
ge       | &ge;       | `&ge;`                    | \x2265 (8805)         | greater-than or equal to
sub      | &sub;      | `&sub;`                   | \x2282 (8834)         | subset of
sup      | &sup;      | `&sup;`                   | \x2283 (8835)         | superset of
nsub     | &nsub;     | `&nsub;`                  | \x2284 (8836)         | not a subset of
sube     | &sube;     | `&sube;`                  | \x2286 (8838)         | subset of or equal to
supe     | &supe;     | `&supe;`                  | \x2287 (8839)         | superset of or equal to
oplus    | &oplus;    | `&oplus;`                 | \x2295 (8853)         | circled plus (direct sum)
otimes   | &otimes;   | `&otimes;`                | \x2297 (8855)         | circled times (vector product)
perp     | &perp;     | `&perp;`                  | \x22A5 (8869)         | up tack (orthogonal to, perpendicular)
sdot     | &sdot;     | `&sdot;`                  | \x22C5 (8901)         | dot operator
lceil    | &lceil;    | `&lceil;`                 | \x2308 (8968)         | left ceiling (APL upstile)
rceil    | &rceil;    | `&rceil;`                 | \x2309 (8969)         | right ceiling
lfloor   | &lfloor;   | `&lfloor;`                | \x230A (8970)         | left floor (APL downstile)
rfloor   | &rfloor;   | `&rfloor;`                | \x230B (8971)         | right floor
lang     | &lang;     | `&lang;`                  | \x2329 (9001)         | left-pointing angle bracket (bra)
rang     | &rang;     | `&rang;`                  | \x232A (9002)         | right-pointing angle bracket (ket)
loz      | &loz;      | `&loz;`                   | \x25CA (9674)         | lozenge
spades   | &spades;   | `&spades;`                | \x2660 (9824)         | black spade suit
clubs    | &clubs;    | `&clubs;`                 | \x2663 (9827)         | black club suit (shamrock)
hearts   | &hearts;   | `&hearts;`                | \x2665 (9829)         | black heart suit (valentine)
diams    | &diams;    | `&diams;`                 | \x2666 (9830)         | black diamond suit
{: .table-striped .table-hover .table-condensed}

</div>
