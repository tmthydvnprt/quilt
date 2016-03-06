title:       \(\LaTeX\) Support
date:        3/20/2015 10:49 pm
description: List of LaTeX Commands
author:      tim
categories:  example
tags:        LaTeX


# {{title}} <br><small>{{description}}</small>
by {{author}} <small>on {{date}}</small>
{: .h4}
****************************************************************************************************************

<div id="post" markdown="1">

A list of [MathJax](https://www.mathjax.org) \(\LaTeX\) Command  examples.  These alphabetical examples come from [here](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm). There are a lot of examples so the page may take a while to render.
{: .lead}

### Symbols

\(\LaTeX\) Command   | Syntax Examples                                                       | `MathJax.js` Output
---------------------|-----------------------------------------------------------------------|--------------------------------------
`#`                  | `$$\def\specialFrac#1#2{\frac{x + #1}{y + #2}}\specialFrac{7}{z+3}$$` | $$\def\specialFrac#1#2{\frac{x + #1}{y + #2}}\specialFrac{7}{z+3}$$
`%`                  | `$$(x+1)^2 % this is a comment$$`                                     | $$(x+1)^2 % this is a comment$$
`&`                  | `$$\begin{matrix} a & b\cr c & d \end{matrix}$$`                      | $$\begin{matrix} a & b\cr c & d \end{matrix}$$
&nbsp;               | `$$a &lt; b$$`                                                        | $$a < b$$
&nbsp;               | `$$\text{Carol }\&\text{ Julia}$$`                                    | $$\text{Carol }\&\text{ Julia}$$
`^`                  | `$$^i$$`                                                              | $$^i$$
&nbsp;               | `$$x^i_2$$`                                                           | $$x^i_2$$
&nbsp;               | `$${x^i}_2$$`                                                         | $${x^i}_2$$
&nbsp;               | `$$x^{i_2}$$`                                                         | $$x^{i_2}$$
&nbsp;               | `$$x^{i^2}$$`                                                         | $$x^{i^2}$$
&nbsp;               | `$${x^i}^2$$`                                                         | $${x^i}^2$$
&nbsp;               | `$$^ax^b$$`                                                           | $$^ax^b$$
&nbsp;               | `$$\sum_{n=1}^\infty$$`                                               | $$\sum_{n=1}^\infty$$
&nbsp;               | `$$\overbrace{x+\cdots+x} ^{n\text{ times}}$$`                        | $$\overbrace{x+\cdots+x} ^{n\text{ times}}$$
&nbsp;               | `$$_2$$`                                                              | $$_2$$
&nbsp;               | `$$x_i^2$$`                                                           | $$x_i^2$$
&nbsp;               | `$${x_i}^2$$`                                                         | $${x_i}^2$$
&nbsp;               | `$$x_{i^2}$$`                                                         | $$x_{i^2}$$
&nbsp;               | `$$x_{i_2}$$`                                                         | $$x_{i_2}$$
&nbsp;               | `$${x_i}_2$$`                                                         | $${x_i}_2$$
&nbsp;               | `$$^a_bx^c_d$$`                                                       | $$^a_bx^c_d$$
&nbsp;               | `$$\sum_{n=1}^\infty$$`                                               | $$\sum_{n=1}^\infty$$
&nbsp;               | `$$\underbrace{x+\cdots+x} _{n\text{ times}}$$`                       | $$\underbrace{x+\cdots+x} _{n\text{ times}}$$
`{ }`                | `$$\boldsymbol aa$$`                                                  | $$\boldsymbol aa$$
&nbsp;               | `$$\boldsymbol \alpha\alpha$$`                                        | $$\boldsymbol \alpha\alpha$$
&nbsp;               | `$$\boldsymbol{a\alpha}a\alpha$$`                                     | $$\boldsymbol{a\alpha}a\alpha$$
&nbsp;               | `$$\bf ab$$`                                                          | $$\bf ab$$
&nbsp;               | `$${\bf ab}cd$$`                                                      | $${\bf ab}cd$$
&nbsp;               | `$$\bf{ab}cd$$`                                                       | $$\bf{ab}cd$$
&nbsp;               | `$${\bf{ab}c}d$$`                                                     | $${\bf{ab}c}d$$
&nbsp;               | `$${efg\bf{ab}c}d$$`                                                  | $${efg\bf{ab}c}d$$
&nbsp;               | `$$ab \bf cd \rm ef $$`                                               | $$ab \bf cd \rm ef$$
&nbsp;               | `$$ab \bf cd {\rm ef} gh$$`                                           | $$ab \bf cd {\rm ef} gh$$
&nbsp;               | `$$\boldsymbol{ab}cd$$`                                               | $$\boldsymbol{ab}cd$$
&nbsp;               | `$$\bf{ab}cd$$`                                                       | $$\bf{ab}cd$$
`\!`                 | `$$\rm IR$$`                                                          | $$\rm IR$$
&nbsp;               | `$$\rm I\! R$$`                                                       | $$\rm I\! R$$
`\\,`                | `$$\,$$`                                                              | $$\,$$
`\\:`                | `$$\:$$`                                                              | $$\:$$
`\\>`                | `$$\>$$`                                                              | $$\>$$
`\\;`                | `$$\;$$`                                                              | $$\;$$
`\\`                 | `$$\rm This is a sentence.$$`                                         | $$\rm This is a sentence.$$
&nbsp;               | `$$\rm This\ is\ a\ sentence.$$`                                      | $$\rm This\ is\ a\ sentence.$$
`~`                  | `$$\rm This~is~a~sentence.$$`                                         | $$\rm This~is~a~sentence.$$
&nbsp;               | `$$\text{This is a sentence.}$$`                                      | $$\text{This is a sentence.}$$
&nbsp;               | `$$\rm Dr. Carol J.V. Fisher$$`                                       | $$\rm Dr. Carol J.V. Fisher$$
&nbsp;               | `$$\rm Dr.~Carol~J.V.~Fisher$$`                                       | $$\rm Dr.~Carol~J.V.~Fisher$$
&nbsp;               | `$$\text{Dr. Carol J.V. Fisher}$$`                                    | $$\text{Dr. Carol J.V. Fisher}$$
&nbsp;               | `$$a b      c d$$`                                                    | $$a b      c d$$
&nbsp;               | `$$a~b~~~~~~c~d$$`                                                    | $$a~b~~~~~~c~d$$
`\#`                 | `$$\#$$`                                                              | $$\#$$
`\$`                 | `$$\$$$`                                                              | $$\$$$
`\%`                 | `$$\%$$`                                                              | $$\%$$
`\&`                 | `$$\&$$`                                                              | $$\&$$
`\\`                 | `$$\\$$`                                                              | $$\\$$
&nbsp;               | `$$\begin{gather}a\\a+b\\a+b+c\end{gather}$$`                         | $$\begin{gather}a\\a+b\\a+b+c\end{gather}$$
`\_`                 | `$$\_$$`                                                              | $$\_$$
&nbsp;               | `$$a_2$$`                                                             | $$a_2$$
&nbsp;               | `$$a\_2$$`                                                            | $$a\_2$$
`\{ \}`              | `$${1,2,3}$$`                                                         | $${1,2,3}$$
&nbsp;               | `$$\{1,2,3\}$$`                                                       | $$\{1,2,3\}$$
&nbsp;               | `$$\left\{\frac ab,c\right\}$$`                                       | $$\left\{\frac ab,c\right\}$$
`\\|`                | `$$\|x\|$$`                                                           | $$\|x\|$$
&nbsp;               | `$$\|\frac ab\|$$`                                                    | $$\|\frac ab\|$$
&nbsp;               | `$$\left\|\frac ab\right\|$$`                                         | $$\left\|\frac ab\right\|$$
&nbsp;               | `$$\{x \| x\in\Bbb Z\}$$`                                             | $$\{x \| x\in\Bbb Z\}$$
&nbsp;               | `$$\{x\,\|\,x\in\Bbb Z\}$$`                                           | $$\{x\,\|\,x\in\Bbb Z\}$$
&nbsp;               | `$$\\|x\\|$$`                                                         | $$\\|x\\|$$
&nbsp;               | `$$\\|\frac ab\\|$$`                                                  | $$\\|\frac ab\\|$$
&nbsp;               | `$$\left\\|\frac ab\right\\|$$`                                       | $$\left\\|\frac ab\right\\|$$
`( )`                | `$$(\frac ab,c)$$`                                                    | $$(\frac ab,c)$$
&nbsp;               | `$$\left(\frac ab,c\right)$$`                                         | $$\left(\frac ab,c\right)$$
`.`                  | `$$3.14$$`                                                            | $$3.14$$
&nbsp;               | `$$a.b$$`                                                             | $$a.b$$
&nbsp;               | `$$a{.}b$$`                                                           | $$a{.}b$$
`/`                  | `$$a/b$$`                                                             | $$a/b$$
`+`                  | `$$a+b$$`                                                             | $$a+b$$
`-`                  | `$$a-b$$`                                                             | $$a-b$$
&nbsp;               | `$$-b$$`                                                              | $$-b$$
&nbsp;               | `$$\text{first: } -a\star b$$`                                        | $$\text{first: } -a\star b$$
&nbsp;               | `$$\text{first: } {-}a\star b$$`                                      | $$\text{first: } {-}a\star b$$
`[ ]`                | `$$[\frac ab,c]$$`                                                    | $$[\frac ab,c]$$
`[ ]`                | `$$\left[\frac ab,c\right]$$`                                         | $$\left[\frac ab,c\right]$$
`=`                  | `$$=$$`                                                               | $$=$$
`'`                  | `$$f(x) = x^2, \\ f'(x) = 2x, \\ f''(x) = 2$$`                        | $$f(x) = x^2, \\ f'(x) = 2x, \\ f''(x) = 2$$

### A

\(\LaTeX\) Command   | Syntax Examples                                                       | `MathJax.js` Output
---------------------|-----------------------------------------------------------------------|--------------------------------------
`\above`             | `$$a+1 \above 1pt b$$`                                                | $$a+1 \above 1pt b$$
&nbsp;               | `$$a \above 1pt b+2$$`                                                | $$a \above 1pt b+2$$
&nbsp;               | `$${a+1 \above 1.5pt b+2}+c$$`                                        | $${a+1 \above 1.5pt b+2}+c$$
`\abovewithdelims`   | `$$a+1 \abovewithdelims [ ] 1pt b$$`                                  | $$a+1 \abovewithdelims [ ] 1pt b$$
&nbsp;               | `$${a \abovewithdelims . \| 1.5pt b+2}_{a=3}$$`                       | $${a \abovewithdelims . \| 1.5pt b+2}_{a=3}$$
&nbsp;               | `$${a+1 \abovewithdelims \{ \} 1pt b+2}+c$$`                          | $${a+1 \abovewithdelims \{ \} 1pt b+2}+c$$
`\acute`             | `$$\acute e$$`                                                        | $$\acute e$$
&nbsp;               | `$$\acute E$$`                                                        | $$\acute E$$
&nbsp;               | `$$\acute eu$$`                                                       | $$\acute eu$$
&nbsp;               | `$$\acute{eu}$$`                                                      | $$\acute{eu}$$
`\aleph`             | `$$\aleph$$`                                                          | $$\aleph$$
`\alpha`             | `$$\alpha$$`                                                          | $$\alpha$$
`\amalg`             | `$$\amalg$$`                                                          | $$\amalg$$
`\And`               | `$$\And$$`                                                            | $$\And$$
`\angle`             | `$$\angle$$`                                                          | $$\angle$$
`\approx`            | `$$\approx$$`                                                         | $$\approx$$
`\approxeq`          | `$$\approxeq$$`                                                       | $$\approxeq$$
`\arccos`            | `$$\arccos$$`                                                         | $$\arccos$$
`\arcsin`            | `$$\arcsin$$`                                                         | $$\arcsin$$
`\arctan`            | `$$\arctan$$`                                                         | $$\arctan$$
`\arg`               | `$$\arg$$`                                                            | $$\arg$$
`\array`             | `$$\array{ a & b+1 \cr c+1 & d }$$`                                   | $$\array{ a & b+1 \cr c+1 & d }$$
`\arrowvert`         | `$$\arrowvert$$`                                                      | $$\arrowvert$$
`\Arrowvert`         | `$$\Arrowvert$$`                                                      | $$\Arrowvert$$
`\ast`               | `$$\ast$$`                                                            | $$\ast$$
`\asymp`             | `$$\asymp$$`                                                          | $$\asymp$$
`\atop`              | `$$a \atop b$$`                                                       | $$a \atop b$$
&nbsp;               | `$$a+1 \atop b+2$$`                                                   | $$a+1 \atop b+2$$
&nbsp;               | `$${a+1 \atop b+2}+c$$`                                               | $${a+1 \atop b+2}+c$$
`\atopwithdelims`    | `$$a \atopwithdelims [ ] b$$`                                         | $$a \atopwithdelims [ ] b$$
&nbsp;               | `$$a+1 \atopwithdelims . \| b+2$$`                                    | $$a+1 \atopwithdelims . \| b+2$$
&nbsp;               | `$${a+1 \atopwithdelims \{ \} b+2}+c$$`                               | $${a+1 \atopwithdelims \{ \} b+2}+c$$

### B

\(\LaTeX\) Command   | Syntax Examples                                                       | `MathJax.js` Output
---------------------|-----------------------------------------------------------------------|--------------------------------------
`\backepsilon`       | `$$\backepsilon$$`                                                    | $$\backepsilon$$
`\backprime`         | `$$\backprime$$`                                                      | $$\backprime$$
`\backsim`           | `$$\backsim$$`                                                        | $$\backsim$$
`\backsimeq`         | `$$\backsimeq$$`                                                      | $$\backsimeq$$
`\backslash`         | `$$\backslash$$`                                                      | $$\backslash$$
`\bar`               | `$$\bar x$$`                                                          | $$\bar x$$
&nbsp;               | `$$\bar X$$`                                                          | $$\bar X$$
&nbsp;               | `$$\bar xy$$`                                                         | $$\bar xy$$
&nbsp;               | `$$\bar{xy}$$`                                                        | $$\bar{xy}$$
`\Bbb`               | `$$\Bbb R$$`                                                          | $$\Bbb R$$
&nbsp;               | `$$\Bbb ZR$$`                                                         | $$\Bbb ZR$$
&nbsp;               | `$$\Bbb{AaBbKk}Cc$$`                                                  | $$\Bbb{AaBbKk}Cc$$
&nbsp;               | `$$\Bbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$`                                | $$\Bbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$
`\Bbbk`              | `$$\Bbbk$$`                                                           | $$\Bbbk$$
`\because`           | `$$\because$$`                                                        | $$\because$$
`\beta`              | `$$\beta$$`                                                           | $$\beta$$
`\beth`              | `$$\beth$$`                                                           | $$\beth$$
`\between`           | `$$\between$$`                                                        | $$\between$$
`\bf`                | `$$\bf AaBb\alpha\beta123$$`                                          | $$\bf AaBb\alpha\beta123$$
&nbsp;               | `$${\bf A B} A B$$`                                                   | $${\bf A B} A B$$
&nbsp;               | `$$\bf AB \rm CD$$`                                                   | $$\bf AB \rm CD$$
&nbsp;               | `$$\bf{AB}CD$$`                                                       | $$\bf{AB}CD$$
`\Bigg`              | `$$\Bigg$$`                                                           | $$\Bigg$$
`\bigg`              | `$$\bigg$$`                                                           | $$\bigg$$
`\Big`               | `$$\Big$$`                                                            | $$\Big$$
`\big`               | `$$\big$$`                                                            | $$\big$$
`\big`               | `$$x\big\| y$$`                                                       | $$x\big\| y$$
`\bigm`              | `$$x\bigm\| y$$`                                                      | $$x\bigm\| y$$
`\bigcap`            | `$$\bigcap$$`                                                         | $$\bigcap$$
`\bigcirc`           | `$$\bigcirc$$`                                                        | $$\bigcirc$$
`\bigcup`            | `$$\bigcup$$`                                                         | $$\bigcup$$
`\bigodot`           | `$$\bigodot$$`                                                        | $$\bigodot$$
`\bigoplus`          | `$$\bigoplus$$`                                                       | $$\bigoplus$$
`\bigotimes`         | `$$\bigotimes$$`                                                      | $$\bigotimes$$
`\bigsqcup`          | `$$\bigsqcup$$`                                                       | $$\bigsqcup$$
`\bigstar`           | `$$\bigstar$$`                                                        | $$\bigstar$$
`\bigtriangledown`   | `$$\bigtriangledown$$`                                                | $$\bigtriangledown$$
`\bigtriangleup`     | `$$\bigtriangleup$$`                                                  | $$\bigtriangleup$$
`\biguplus`          | `$$\biguplus$$`                                                       | $$\biguplus$$
`\bigvee`            | `$$\bigvee$$`                                                         | $$\bigvee$$
`\bigwedge`          | `$$\bigwedge$$`                                                       | $$\bigwedge$$
`\binom`             | `$$\binom n k$$`                                                      | $$\binom n k$$
&nbsp;               | `$$\binom{n-1}k-1$$`                                                  | $$\binom{n-1}k-1$$
&nbsp;               | `$$\binom{n-1}{k-1}$$`                                                | $$\binom{n-1}{k-1}$$
`\blacklozenge`      | `$$\blacklozenge$$`                                                   | $$\blacklozenge$$
`\blacksquare`       | `$$\blacksquare$$`                                                    | $$\blacksquare$$
`\blacktriangle`     | `$$\blacktriangle$$`                                                  | $$\blacktriangle$$
`\blacktriangledown` | `$$\blacktriangledown$$`                                              | $$\blacktriangledown$$
`\bmod`              | `$$a \bmod b$$`                                                       | $$a \bmod b$$
`\bot`               | `$$\bot$$`                                                            | $$\bot$$
`\bowtie`            | `$$\bowtie$$`                                                         | $$\bowtie$$
`\Box`               | `$$\Box$$`                                                            | $$\Box$$
`\boxdot`            | `$$\boxdot$$`                                                         | $$\boxdot$$
`\boxed`             | `$$\boxed ab$$`                                                       | $$\boxed ab$$
&nbsp;               | `$$\boxed{ab}$$`                                                      | $$\boxed{ab}$$
&nbsp;               | `$$\boxed{ab\strut}$$`                                                | $$\boxed{ab\strut}$$
&nbsp;               | `$$\boxed{\text{boxed text}}$$`                                       | $$\boxed{\text{boxed text}}$$
`\boxminus`          | `$$\boxminus$$`                                                       | $$\boxminus$$
`\boxplus`           | `$$\boxplus$$`                                                        | $$\boxplus$$
`\boxtimes`          | `$$\boxtimes$$`                                                       | $$\boxtimes$$
`\brace`             | `$$\brace$$`                                                          | $$\brace$$
&nbsp;               | `$$a\brace b$$`                                                       | $$a\brace b$$
&nbsp;               | `$$a+b+c\brace d+e+f$$`                                               | $$a+b+c\brace d+e+f$$
&nbsp;               | `$$a+{b+c\brace d+e}+f$$`                                             | $$a+{b+c\brace d+e}+f$$
`\brack`             | `$$\brack$$`                                                          | $$\brack$$
&nbsp;               | `$$a\brack b$$`                                                       | $$a\brack b$$
&nbsp;               | `$$a+b+c\brack d+e+f$$`                                               | $$a+b+c\brack d+e+f$$
&nbsp;               | `$$a+{b+c\brack d+e}+f$$`                                             | $$a+{b+c\brack d+e}+f$$
`\breve`             | `$$\breve e$$`                                                        | $$\breve e$$
&nbsp;               | `$$\breve E$$`                                                        | $$\breve E$$
&nbsp;               | `$$\breve eu$$`                                                       | $$\breve eu$$
&nbsp;               | `$$\breve{eu}$$`                                                      | $$\breve{eu}$$
`\buildrel`          | `$$\buildrel \alpha\beta \over \longrightarrow$$`                     | $$\buildrel \alpha\beta \over \longrightarrow$$
&nbsp;               | `$$\buildrel \rm def \over {:=}$$`                                    | $$\buildrel \rm def \over {:=}$$
`\bullet`            | `$$\bullet$$`                                                         | $$\bullet$$
`\Bumpeg`            | `$$\Bumpeg$$`                                                         | $$\Bumpeg$$
`\bumpeg`            | `$$\bumpeg$$`                                                         | $$\bumpeg$$

### C

\(\LaTeX\) Command   | Syntax Examples                                                       | `MathJax.js` Output
---------------------|-----------------------------------------------------------------------|--------------------------------------
`\cal`               | `$$\cal ABCDEFGHIJKLMNOPQRSTUVWXYZ$$`                                 | $$\cal ABCDEFGHIJKLMNOPQRSTUVWXYZ$$
&nbsp;               | `$$\cal 0123456789$$`                                                 | $$\cal 0123456789$$
&nbsp;               | `$$\cal abcdefghijklmnopqrstuvwxyz$$`                                 | $$\cal abcdefghijklmnopqrstuvwxyz$$
&nbsp;               | `$${\cal AB}AB$$`                                                     | $${\cal AB}AB$$
&nbsp;               | `$$\cal AB \rm AB$$`                                                  | $$\cal AB \rm AB$$
&nbsp;               | `$$\cal{AB}CD$$`                                                      | $$\cal{AB}CD$$
`\cancel`            | `$$\frac{(x+1)\cancel{(x+2)}}{3\cancel{(x+2)}}$$`                     | $$\frac{(x+1)\cancel{(x+2)}}{3\cancel{(x+2)}}$$
`\bcancel`           | `$$\frac{\bcancel{\frac13}}{\bcancel{\frac13}} = 1$$`                 | $$\frac{\bcancel{\frac13}}{\bcancel{\frac13}} = 1$$
`\Cap`               | `$$\Cap$$`                                                            | $$\Cap$$
`\cap`               | `$$\cap$$`                                                            | $$\cap$$
`\cdot`              | `$$a\cdot b$$`                                                        | $$a\cdot b$$
`\cdotp`             | `$$a\cdotp b$$`                                                       | $$a\cdotp b$$
`\centerdot`         | `$$a\centerdot b$$`                                                   | $$a\centerdot b$$
`\cdot`              | `$$\rm s \cdot h$$`                                                   | $$\rm s \cdot h$$
`\cdotp`             | `$$\rm s \cdotp h$$`                                                  | $$\rm s \cdotp h$$
`\cdots`             | `$$x_1 + \cdots + x_n$$`                                              | $$x_1 + \cdots + x_n$$
`\cases`             | `$$\|x\| = \cases{x  & \text{if} x\ge 0\cr -x & \text{if} x\lt 0}$$`  | $$\|x\| = \cases{x  & \text{if } x\ge 0\cr -x & \text{if } x\lt 0}$$
`\cfrac`             | `$$\cfrac{2}{1+\cfrac{2}{1+\cfrac{2}{1}}}$$`                          | $$\cfrac{2}{1+\cfrac{2}{1+\cfrac{2}{1}}}$$
`\check`             | `$$\check o$$`                                                        | $$\check o$$
&nbsp;               | `$$\check O$$`                                                        | $$\check O$$
&nbsp;               | `$$\check oe$$`                                                       | $$\check oe$$
&nbsp;               | `$$\check{oe}$$`                                                      | $$\check{oe}$$
`\chi`               | `$$\chi$$`                                                            | $$\chi$$
`\choose`            | `$$n+1 \choose k+2$$`                                                 | $$n+1 \choose k+2$$
&nbsp;               | `$${n+1 \choose k+2}$$`                                               | $${n+1 \choose k+2}$$
&nbsp;               | `$$1+{n \choose 2}+k$$`                                               | $$1+{n \choose 2}+k$$
`\circ`              | `$$(f\circ g)(x) = f(g(x))$$`                                         | $$(f\circ g)(x) = f(g(x))$$
`\circ`              | `$$45^\circ$$`                                                        | $$45^\circ$$
`\circeq`            | `$$\circeq$$`                                                         | $$\circeq$$
`\circlearrowleft`   | `$$\circlearrowleft$$`                                                | $$\circlearrowleft$$
`\circlearrowright`  | `$$\circlearrowright$$`                                               | $$\circlearrowright$$
`\circledast`        | `$$\circledast$$`                                                     | $$\circledast$$
`\circledcirc`       | `$$\circledcirc$$`                                                    | $$\circledcirc$$
`\circleddash`       | `$$\circleddash$$`                                                    | $$\circleddash$$
`\circledR`          | `$$\circledR$$`                                                       | $$\circledR$$
`\circledS`          | `$$\circledS$$`                                                       | $$\circledS$$
`\clubsuit`          | `$$\clubsuit$$`                                                       | $$\clubsuit$$
`:`                  | `$$f:A\to B$$`                                                        | $$f:A\to B$$
`\colon`             | `$$f\colon A\to B$$`                                                  | $$f\colon A\to B$$
`\color`             | `$$\color{red}{ \frac{1+\sqrt{5}}{2} }$$`                             | $$\color{red}{ \frac{1+\sqrt{5}}{2} }$$
&nbsp;               | `$$\color{#0000FF}AB$$`                                               | $$\color{#0000FF}AB$$
`\complement`        | `$$\complement$$`                                                     | $$\complement$$
`\cong`              | `$$\cong$$`                                                           | $$\cong$$
`\coprod`            | `$$\coprod$$`                                                         | $$\coprod$$
`\cos`               | `$$\cos(2x-1)$$`                                                      | $$\cos(2x-1)$$
`\cosh`              | `$$\cosh(2x-1)$$`                                                     | $$\cosh(2x-1)$$
`\cot`               | `$$\cot(2x-1)$$`                                                      | $$\cot(2x-1)$$
`\coth`              | `$$\coth(2x-1)$$`                                                     | $$\coth(2x-1)$$
`\csc`               | `$$\csc(2x-1)$$`                                                      | $$\csc(2x-1)$$
`\Cup`               | `$$\Cup$$`                                                            | $$\Cup$$
`\cup`               | `$$\cup$$`                                                            | $$\cup$$
`\curlyeqprec`       | `$$\curlyeqprec$$`                                                    | $$\curlyeqprec$$
`\curlyeqsucc`       | `$$\curlyeqsucc$$`                                                    | $$\curlyeqsucc$$
`\curlyvee`          | `$$\curlyvee$$`                                                       | $$\curlyvee$$
`\curlywedge`        | `$$\curlywedge$$`                                                     | $$\curlywedge$$
`\curvearrowleft`    | `$$\curvearrowleft$$`                                                 | $$\curvearrowleft$$
`\curvearrowright`   | `$$\curvearrowright$$`                                                | $$\curvearrowright$$

### D

\(\LaTeX\) Command   | Syntax Examples                                                       | `MathJax.js` Output
---------------------|-----------------------------------------------------------------------|--------------------------------------
`\dagger`            | `$$\dagger$$`                                                         | $$\dagger$$
`\ddagger`           | `$$\ddagger$$`                                                        | $$\ddagger$$
`\daleth`            | `$$\daleth$$`                                                         | $$\daleth$$
`\dashleftarrow`     | `$$\dashleftarrow$$`                                                  | $$\dashleftarrow$$
`\dashrightarrow`    | `$$\dashrightarrow$$`                                                 | $$\dashrightarrow$$
`\dashv`             | `$$\dashv$$`                                                          | $$\dashv$$
`\dbinom`            | `$$\dbinom n k$$`                                                     | $$\dbinom n k$$
&nbsp;               | `$$\dbinom{n-1}k-1$$`                                                 | $$\dbinom{n-1}k-1$$
&nbsp;               | `$$\dbinom{n-1}{k-1}$$`                                               | $$\dbinom{n-1}{k-1}$$
`\dot`               | `$$\dot x$$`                                                          | $$\dot x$$
`\ddot`              | `$$\ddot x$$`                                                         | $$\ddot x$$
`\dddot`             | `$$\dddot x$$`                                                        | $$\dddot x$$
`\ddddot`            | `$$\ddddot x$$`                                                       | $$\ddddot x$$
`\ddot`              | `$$\ddot x(t)$$`                                                      | $$\ddddot x(t)$$
`\ddddot`            | `$$\ddddot{x(t)}$$`                                                   | $$\ddddot{x(t)}$$
`\ddot`              | `$$\ddots$$`                                                          | $$\ddots$$
`\deg`               | `$$\deg$$`                                                            | $$\deg$$
`\Delta`             | `$$\Delta$$`                                                          | $$\Delta$$
`\delta`             | `$$\delta$$`                                                          | $$\delta$$
`\det_`              | `$$\det_{\rm sub}$$`                                                  | $$\det_{\rm sub}$$
&nbsp;               | `$$\det_{\rm sub}$$`                                                  | $$\det_{\rm sub}$$
&nbsp;               | `$$\det\limits_{\rm sub}$$`                                           | $$\det\limits_{\rm sub}$$
&nbsp;               | `$$\det\nolimits_{\rm sub}$$`                                         | $$\det\nolimits_{\rm sub}$$
`\dfrac`             | `$$\dfrac a b$$`                                                      | $$\dfrac a b$$
&nbsp;               | `$$\dfrac{a-1}b-1$$`                                                  | $$\dfrac{a-1}b-1$$
&nbsp;               | `$$\dfrac{a-1}{b-1} $$`                                               | $$\dfrac{a-1}{b-1}$$
`\diagdown`          | `$$\diagdown$$`                                                       | $$\diagdown$$
`\diagup`            | `$$\diagup$$`                                                         | $$\diagup$$
`\Diamond`           | `$$\Diamond$$`                                                        | $$\Diamond$$
`\diamond`           | `$$\diamond$$`                                                        | $$\diamond$$
`\diamondsuit`       | `$$\diamondsuit$$`                                                    | $$\diamondsuit$$
`\div`               | `$$\div$$`                                                            | $$\div$$
`\divideontimes`     | `$$\divideontimes$$`                                                  | $$\divideontimes$$
`\Doteq`             | `$$\Doteq$$`                                                          | $$\Doteq$$
`\doteq`             | `$$\doteq$$`                                                          | $$\doteq$$
`\dotplus`           | `$$\dotplus$$`                                                        | $$\dotplus$$
`\dots`              | `$$\dots$$`                                                           | $$\dots$$
&nbsp;               | `$$x_1, \dots, x_n$$`                                                 | $$x_1, \dots, x_n$$
&nbsp;               | `$$x_1 + \dots + x_n$$`                                               | $$x_1 + \dots + x_n$$
`\doublebarwedge`    | `$$\doublebarwedge$$`                                                 | $$\doublebarwedge$$
`\doublecap`         | `$$\doublecap$$`                                                      | $$\doublecap$$
`\doublecup`         | `$$\doublecup$$`                                                      | $$\doublecup$$
`\downarrow`         | `$$\downarrow$$`                                                      | $$\downarrow$$
`\Downarrow`         | `$$\Downarrow$$`                                                      | $$\Downarrow$$
`\downdownarrows`    | `$$\downdownarrows$$`                                                 | $$\downdownarrows$$
`\downharpoonleft`   | `$$\downharpoonleft$$`                                                | $$\downharpoonleft$$
`\downharpoonright`  | `$$\downharpoonright$$`                                               | $$\downharpoonright$$

Come on. what is the deal.

### E

\(\LaTeX\) Command  | Syntax Examples                                                        | `MathJax.js` Output
--------------------|------------------------------------------------------------------------|--------------------------------------
`\ell`              | `$$\ell$$`                                                             | $$\ell$$
`\emptyset`         | `$$\emptyset$$`                                                        | $$\emptyset$$
`\epsilon`          | `$$\epsilon$$`                                                         | $$\epsilon$$
`\eqalign`          | `$$\eqalign{3x - 4y &= 5\cr x  +  7 &= -2y}$$`                         | $$\eqalign{3x - 4y &= 5\cr x  +  7 &= -2y}$$
`\eqalignno`        | `$$\eqalignno{3x - 4y &= 5   &(\dagger) \cr x  +  7 &= -2y &(\ddagger)\cr z &= 2}$$` | $$\eqalignno{3x - 4y &= 5   &(\dagger) \cr x  +  7 &= -2y &(\ddagger)\cr z &= 2}$$
`\eqcirc`           | `$$\eqcirc$$`                                                          | $$\eqcirc$$
`\eqsim`            | `$$\eqsim$$`                                                           | $$\eqsim$$
`\eqslantgtr`       | `$$\eqslantgtr$$`                                                      | $$\eqslantgtr$$
`\eqslantless`      | `$$\eqslantless$$`                                                     | $$\eqslantless$$
`\equiv`            | `$$\equiv$$`                                                           | $$\equiv$$
`\eta`              | `$$\eta$$`                                                             | $$\eta$$
`\eth`              | `$$\eth$$`                                                             | $$\eth$$
`\exists`           | `$$\exists$$`                                                          | $$\exists$$
`\exp`              | `$$\exp$$`                                                             | $$\exp$$

### F

\(\LaTeX\) Command  | Syntax Examples                                                        | `MathJax.js` Output
--------------------|------------------------------------------------------------------------|--------------------------------------
`\fallingdotseq`    | `$$\fallingdotseq$$`                                                   | $$\fallingdotseq$$
`\fbox`             | `$$\fbox{Hi there!}$$`                                                 | $$\fbox{Hi there!}$$
`\Finv`             | `$$\Finv$$`                                                            | $$\Finv$$
`\flat`             | `$$\flat$$`                                                            | $$\flat$$
`\forall`           | `$$\forall$$`                                                          | $$\forall$$
`\frac`             | `$$\frac a b$$`                                                        | $$\frac a b$$
&nbsp;              | `$$\frac{a-1}b-1$$`                                                    | $$\frac{a-1}b-1$$
&nbsp;              | `$$\frac{a-1}{b-1}$$`                                                  | $$\frac{a-1}{b-1}$$
`\frak`             | `$$\frak ABCDEFGHIJKLMNOPQRSTUVWXYZ$$`                                 | $$\frak ABCDEFGHIJKLMNOPQRSTUVWXYZ$$
&nbsp;              | `$$\frak 0123456789$$`                                                 | $$\frak 0123456789$$
&nbsp;              | `$$\frak abcdefghijklmnopqrstuvwxyz$$`                                 | $$\frak abcdefghijklmnopqrstuvwxyz$$
`\frown`            | `$$\frown$$`                                                           | $$\frown$$

### G

\(\LaTeX\) Command  | Syntax Examples                                                        | `MathJax.js` Output
--------------------|------------------------------------------------------------------------|--------------------------------------
`\Game`             | `$$\Game$$`                                                            | $$\Game$$
`\Gamma`            | `$$\Gamma$$`                                                           | $$\Gamma$$
`\gcd`              | `$$\gcd_{\rm sub}^{\rm sup}$$`                                         | $$\gcd_{\rm sub}^{\rm sup}$$
`\ge`               | `$$\ge$$`                                                              | $$\ge$$
`\geq`              | `$$\geq$$`                                                             | $$\geq$$
`\geqq`             | `$$\geqq$$`                                                            | $$\geqq$$
`\geqslatn`         | `$$\geqslatn$$`                                                        | $$\geqslant$$
`\genfrac`          | `$$\genfrac(]{0pt}{2}{a+b}{c+d}$$`                                     | $$\genfrac(]{0pt}{2}{a+b}{c+d}$$
`\gets`             | `$$\gets$$`                                                            | $$\gets$$
`\gg`               | `$$\gg$$`                                                              | $$\gg$$
`\ggg`              | `$$\ggg$$`                                                             | $$\ggg$$
`\gimel`            | `$$\gimel$$`                                                           | $$\gimel$$
`\gtrapprox`        | `$$\gtrapprox$$`                                                       | $$\gtrapprox$$
`\gnapprox`         | `$$\gnapprox$$`                                                        | $$\gnapprox$$
`\gneq`             | `$$\gneq$$`                                                            | $$\gneq$$
`\gneqq`            | `$$\gneqq$$`                                                           | $$\gneqq$$
`\gvertneqq`        | `$$\gvertneqq$$`                                                       | $$\gvertneqq$$
`\gtrsim`           | `$$\gtrsim$$`                                                          | $$\gtrsim$$
`\gnsim`            | `$$\gnsim$$`                                                           | $$\gnsim$$
`\grave`            | `$$\grave o$$`                                                         | $$\grave o$$
&nbsp;              | `$$\grave O$$`                                                         | $$\grave O$$
&nbsp;              | `$$\grave oe$$`                                                        | $$\grave oe$$
&nbsp;              | `$$\grave{oe}$$`                                                       | $$\grave{oe}$$
`\gt`               | `$$\gt$$`                                                              | $$\gt$$
`\gtrdot`           | `$$\gtrdot$$`                                                          | $$\gtrdot$$
`\gtreqless`        | `$$\gtreqless$$`                                                       | $$\gtreqless$$
`\gtreqqless`       | `$$\gtreqqless$$`                                                      | $$\gtreqqless$$
`\gtrless`          | `$$\gtrless$$`                                                         | $$\gtrless$$

### H

\(\LaTeX\) Command  | Syntax Examples                                                        | `MathJax.js` Output
--------------------|------------------------------------------------------------------------|--------------------------------------
`\hat`              | `$$\hat\imath$$`                                                       | $$\hat\imath$$
&nbsp;              | `$$\hat\jmath$$`                                                       | $$\hat\jmath$$
&nbsp;              | `$$\hat ab$$`                                                          | $$\hat ab$$
&nbsp;              | `$$\hat{ab}$$`                                                         | $$\hat{ab}$$
`\hbox`             | `$$\hbox{\alpha a }\alpha a$$`                                         | $$\hbox{\alpha a }\alpha a$$
`\hdashline`        | `$$\begin{matrix} \hdashline x_{11} & x_{12} \\ x_{21} & x_{22} \\ x_{31} & x_{32} \end{matrix}$$` | $$\begin{matrix} \hdashline x_{11} & x_{12} \\ x_{21} & x_{22} \\ x_{31} & x_{32} \end{matrix}$$
`\hline`            | `$$\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ \hline x_{31} & x_{32} \end{matrix}$$`     | $$\begin{matrix} x_{11} & x_{12} \\ x_{21} & x_{22} \\ \hline x_{31} & x_{32} \end{matrix}$$
`\heartsuit`        | `$$\heartsuit$$`                                                       | $$\heartsuit$$
`\hookleftarrow`    | `$$\hookleftarrow$$`                                                   | $$\hookleftarrow$$
`\hookrighttarrow`  | `$$\hookrighttarrow$$`                                                 | $$\hookrightarrow$$
`\hskip`            | `$$w\hskip1em i\hskip2em d\hskip3em e\hskip4em r$$`                    | $$w\hskip1em i\hskip2em d\hskip3em e\hskip4em r$$
`\hslash`           | `$$\hslash$$`                                                          | $$\hslash$$
`\hspace`           | `$$s\hspace7ex k\hspace6ex i\hspace5ex n\hspace4ex n\hspace3ex i\hspace2ex e\hspace1ex r$$`        | $$s\hspace7ex k\hspace6ex i\hspace5ex n\hspace4ex n\hspace3ex i\hspace2ex e\hspace1ex r$$
`\huge`             | `$$\huge AaBb\alpha\beta123\frac ab\sqrt x$$`                          | $$\huge AaBb\alpha\beta123\frac ab\sqrt x$$
&nbsp;              | `$${\huge A B} A B$$`                                                  | $${\huge A B} A B$$
&nbsp;              | `$$A\alpha\huge A\alpha \Huge A\alpha$$`                               | $$A\alpha\huge A\alpha \Huge A\alpha$$

### I

\(\LaTeX\) Command  | Syntax Examples                                                        | `MathJax.js` Output
--------------------|------------------------------------------------------------------------|--------------------------------------
`\idotsint`         | `$$\idotsint$$`                                                        | $$\idotsint$$
`\iff`              | `$$\iff$$`                                                             | $$\iff$$
`\int`              | `$$\int$$`                                                             | $$\int$$
`\iint`             | `$$\iint$$`                                                            | $$\iint$$
`\iiint`            | `$$\iiint$$`                                                           | $$\iiint$$
`\iiiint`           | `$$\iiiint$$`                                                          | $$\iiiint$$
`\int`              | `$$\int_a^b$$`                                                         | $$\int_a^b$$
`\intop`            | `$$\intop_a^b$$`                                                       | $$\intop_a^b$$
`\Im`               | `$$\Im$$`                                                              | $$\Im$$
`\imath`            | `$$\imath$$`                                                           | $$\imath$$
`\impliedby`        | `$$\impliedby$$`                                                       | $$\impliedby$$
`\implies`          | `$$\implies$$`                                                         | $$\implies$$
`\in`               | `$$\in$$`                                                              | $$\in$$
`\inf`              | `$$\inf$$`                                                             | $$\inf$$
`\infty`            | `$$\infty$$`                                                           | $$\infty$$
`\intercal`         | `$$\intercal$$`                                                        | $$\intercal$$
`\iota`             | `$$\iota$$`                                                            | $$\iota$$
`\it`               | `$$\it$$`                                                              | $$\it$$

### J

\(\LaTeX\) Command  | Syntax Examples                                                        | `MathJax.js` Output
--------------------|------------------------------------------------------------------------|--------------------------------------
`\Join`             | `$$\Join$$`                                                            | $$\Join$$

### K

\(\LaTeX\) Command  | Syntax Examples                                                        | `MathJax.js` Output
--------------------|------------------------------------------------------------------------|--------------------------------------
`\kappa`            | `$$\kappa$$`                                                           | $$\kappa$$
`\ker`              | `$$\ker$$`                                                             | $$\ker$$
`\kern`             | `$$\|\kern 2ex\|\kern 2em\|\kern 2pt\|$$`                              | $$\|\kern 2ex\|\kern 2em\|\kern 2pt\|$$
&nbsp;              | `$$\rm I\kern-2.5pt R$$`                                               | $$\rm I\kern-2.5pt R$$

### L

\(\LaTeX\) Command     | Syntax Examples                                                     | `MathJax.js` Output
-----------------------|---------------------------------------------------------------------|--------------------------------------
`\Lambda`              | `$$\Lambda$$`                                                       | $$\Lambda$$
`\lambda`              | `$$\lambda$$`                                                       | $$\lambda$$
`\land`                | `$$\land$$`                                                         | $$\land$$
`\langle`              | `$$\langle$$`                                                       | $$\langle$$
`\left`                | `$$\left\langle \matrix{a & b\cr c & d} \right\rangle$$`            | $$\left\langle \matrix{a & b\cr c & d} \right\rangle$$
`\Large`               | `$$\Large AaBb\alpha\beta123\frac ab$$`                             | $$\Large AaBb\alpha\beta123\frac ab$$
&nbsp;                 | `$${\Large A B} A B$$`                                              | $${\Large A B} A B$$
&nbsp;                 | `$$AB \large AB \Large AB \LARGE AB$$`                              | $$AB \large AB \Large AB \LARGE AB$$
&nbsp;                 | `$$\Large{AB}CD$$`                                                  | $$\Large{AB}CD$$
`\LaTeX`               | `$$\LaTeX$$`                                                        | $$\LaTeX$$
`\lbrace`              | `$$\lbrace$$`                                                       | $$\lbrace$$
&nbsp;                 | `$$\lbrace \frac ab, c \rbrace$$`                                   | $$\lbrace \frac ab, c \rbrace$$
&nbsp;                 | `$$\lbrack$$`                                                       | $$\lbrack$$
`\lbrack`              | `$$\lbrack \frac ab, c \rbrack$$`                                   | $$\lbrack \frac ab, c \rbrack$$
`\lceil`               | `$$\lceil$$`                                                        | $$\lceil$$
`\left`                | `$$\left\lceil \matrix{a & b\cr c & d} \right\rceil$$`              | $$\left\lceil \matrix{a & b\cr c & d} \right\rceil$$
`\le`                  | `$$\le$$`                                                           | $$\le$$
`\leq`                 | `$$\leq$$`                                                          | $$\leq$$
`\leqq`                | `$$\leqq$$`                                                         | $$\leqq$$
`\leqslant`            | `$$\leqslant$$`                                                     | $$\leqslant$$
`\leadsto`             | `$$\leadsto$$`                                                      | $$\leadsto$$
`\left`                | `$$\left( \frac12 \right)$$`                                        | $$\left( \frac12 \right)$$
&nbsp;                 | `$$\left\updownarrow \phantom{\frac12} \right\Updownarrow$$`        | $$\left\updownarrow \phantom{\frac12} \right\Updownarrow$$
`\leftarrow`           | `$$\leftarrow$$`                                                    | $$\leftarrow$$
`\Leftarrow`           | `$$\Leftarrow$$`                                                    | $$\Leftarrow$$
`\leftarrowtail`       | `$$\leftarrowtail$$`                                                | $$\leftarrowtail$$
`\leftharpoondown`     | `$$\leftharpoondown$$`                                              | $$\leftharpoondown$$
`\leftharpoonup`       | `$$\leftharpoonup$$`                                                | $$\leftharpoonup$$
`\leftleftarrows`      | `$$\leftleftarrows$$`                                               | $$\leftleftarrows$$
`\leftrightarrow`      | `$$\leftrightarrow$$`                                               | $$\leftrightarrow$$
`\Leftrightarrow`      | `$$\Leftrightarrow$$`                                               | $$\Leftrightarrow$$
`\leftrightarrows`     | `$$\leftrightarrows$$`                                              | $$\leftrightarrows$$
`\leftrightharpoons`   | `$$\leftrightharpoons$$`                                            | $$\leftrightharpoons$$
`\leftrightsquigarrow` | `$$\leftrightsquigarrow$$`                                          | $$\leftrightsquigarrow$$
`\leftroot1`           | `$$\sqrt[3\leftroot1]{x}$$`                                         | $$\sqrt[3\leftroot1]{x}$$
`\leftroot`            | `$$\root 3\leftroot{-1} \of x$$`                                    | $$\root 3\leftroot{-1} \of x$$
`\leftthreetimes`      | `$$\leftthreetimes$$`                                               | $$\leftthreetimes$$
`\leqalignno`          | `$$\leqalignno{3x - 4y &= 5 &(\dagger) \cr x + 7 &= -2y &(\ddagger)\cr z &= 2}$$` | $$\leqalignno{3x - 4y &= 5 &(\dagger) \cr x + 7 &= -2y &(\ddagger)\cr z &= 2}$$
`\lessapprox`          | `$$\lessapprox$$`                                                   | $$\lessapprox$$
`\lessdot`             | `$$\lessdot$$`                                                      | $$\lessdot$$
`\lesseqgtr`           | `$$\lesseqgtr$$`                                                    | $$\lesseqgtr$$
`\lesseqqgtr`          | `$$\lesseqqgtr$$`                                                   | $$\lesseqqgtr$$
`\lessgtr`             | `$$\lessgtr$$`                                                      | $$\lessgtr$$
`\lesssim`             | `$$\lesssim$$`                                                      | $$\lesssim$$
`\lfloor`              | `$$\lfloor$$`                                                       | $$\lfloor$$
`\lg`                  | `$$\lg$$`                                                           | $$\lg$$
`\lgroup`              | `$$\left\lgroup \matrix{a & b\cr c & d} \right\rgroup$$`            | $$\left\lgroup \matrix{a & b\cr c & d} \right\rgroup$$
`\lhd`                 | `$$\lhd$$`                                                          | $$\lhd$$
`\lim`                 | `$$\lim$$`                                                          | $$\lim$$
&nbsp;                 | `$$\lim_{n\rightarrow\infty} f(x) = \ell$$`                         | $$\lim_{n\rightarrow\infty} f(x) = \ell$$
&nbsp;                 | `$$\int_a^b f(x)\,dx$$`                                             | $$\int_a^b f(x)\,dx$$
`\limits`              | `$$\int\limits_a^b f(x)\,dx$$`                                      | $$\int\limits_a^b f(x)\,dx$$
&nbsp;                 | `$$\mathop{x}\limits_0^1$$`                                         | $$\mathop{x}\limits_0^1$$
`\ll`                  | `$$\ll$$`                                                           | $$\ll$$
`\llap`                | `$$a\mathrel{ {=}\llap{/}}b$$`                                      | $$a\mathrel{ {=}\llap{/}}b$$
&nbsp;                 | `$$a\mathrel{ {=}\llap{/\,}}b$$`                                    | $$a\mathrel{ {=}\llap{/\,}}b$$
`\llcorner`            | `$$\llcorner$$`                                                     | $$\llcorner$$
`\lrcorner`            | `$$\lrcorner$$`                                                     | $$\lrcorner$$
`\Lleftarrow`          | `$$\Lleftarrow$$`                                                   | $$\Lleftarrow$$
`\lll`                 | `$$\lll$$`                                                          | $$\lll$$
`\llless`              | `$$\llless$$`                                                       | $$\llless$$
`\lmoustache`          | `$$\lmoustache$$`                                                   | $$\lmoustache$$
`\ln`                  | `$$\ln$$`                                                           | $$\ln$$
`\lnapprox`            | `$$\lnapprox$$`                                                     | $$\lnapprox$$
`\lneq`                | `$$\lneq$$`                                                         | $$\lneq$$
`\lneqq`               | `$$\lneqq$$`                                                        | $$\lneqq$$
`\lnot`                | `$$\lnot$$`                                                         | $$\lnot$$
`\lnsim`               | `$$\lnsim$$`                                                        | $$\lnsim$$
`\log`                 | `$$\log$$`                                                          | $$\log$$
`\longleftarrow`       | `$$\longleftarrow$$`                                                | $$\longleftarrow$$
`\Longleftarrow`       | `$$\Longleftarrow$$`                                                | $$\Longleftarrow$$
`\longrightarrow`      | `$$\longrightarrow$$`                                               | $$\longrightarrow$$
`\Longrightarrow`      | `$$\Longrightarrow$$`                                               | $$\Longrightarrow$$
`\longleftrightarrow`  | `$$\longleftrightarrow$$`                                           | $$\longleftrightarrow$$
`\Longleftrightarrow`  | `$$\Longleftrightarrow$$`                                           | $$\Longleftrightarrow$$
`\longmapsto`          | `$$\longmapsto$$`                                                   | $$\longmapsto$$
`\looparrowleft`       | `$$\looparrowleft$$`                                                | $$\looparrowleft$$
`\looparrowright`      | `$$\looparrowright $$`                                              | $$\looparrowright$$
`\lor`                 | `$$\lor$$`                                                          | $$\lor$$
`\lower`               | `$$l\lower 2pt {owe} r$$`                                           | $$l\lower 2pt {owe} r$$
`\lozenge`             | `$$\lozenge$$`                                                      | $$\lozenge$$
`\lt`                  | `$$\lt$$`                                                           | $$\lt$$
`\ltimes`              | `$$\ltimes$$`                                                       | $$\ltimes$$
`\lvert`               | `$$\lvert$$`                                                        | $$\lvert$$
`\lVert`               | `$$\lVert$$`                                                        | $$\lVert$$
`\lvertneqq`           | `$$\lvertneqq$$`                                                    | $$\lvertneqq$$

### M

\(\LaTeX\) Command  | Syntax Examples                                                        | `MathJax.js` Output
--------------------|------------------------------------------------------------------------|--------------------------------------
`\maltese`          | `$$\maltese$$`                                                         | $$\maltese$$
`\mapsto`           | `$$\mapsto$$`                                                          | $$\mapsto$$
`\mathbb`           | `$$\mathbb R$$`                                                        | $$\mathbb R$$
&nbsp;              | `$$\mathbb ZR$$`                                                       | $$\mathbb ZR$$
&nbsp;              | `$$\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$`                              | $$\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$
`\mathbf`           | `$$\mathbf{AaBb\alpha\beta123}$$`                                      | $$\mathbf{AaBb\alpha\beta123}$$
`\mathbin`          | `$$a\mathbin{\Diamond}b$$`                                             | $$a\mathbin{\Diamond}b$$
`\mathcal`          | `$$\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$`                             | $$\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$
&nbsp;              | `$$\mathcal{0123456789}$$`                                             | $$\mathcal{0123456789}$$
&nbsp;              | `$$\mathcal{abcdefghijklmnopqrstuvwxyz}$$`                             | $$\mathcal{abcdefghijklmnopqrstuvwxyz}$$
&nbsp;              | `$$\mathcal{AB}AB$$`                                                   | $$\mathcal{AB}AB$$
`\mathfrak`         | `$$\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$`                            | $$\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$
&nbsp;              | `$$\mathfrak{0123456789}$$`                                            | $$\mathfrak{0123456789}$$
&nbsp;              | `$$\mathfrak{abcdefghijklmnopqrstuvwxyz}$$`                            | $$\mathfrak{abcdefghijklmnopqrstuvwxyz}$$
&nbsp;              | `$$\mathfrak{AB}AB$$`                                                  | $$\mathfrak{AB}AB$$
`\mathring`         | `$$\mathring A$$`                                                      | $$\mathring A$$
&nbsp;              | `$$\mathring{AB}C$$`                                                   | $$\mathring{AB}C$$
`\mathscr`          | `$$\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$`                             | $$\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$
&nbsp;              | `$$\mathscr{0123456789}$$`                                             | $$\mathscr{0123456789}$$
&nbsp;              | `$$\mathscr{abcdefghijklmnopqrstuvwxyz}$$`                             | $$\mathscr{abcdefghijklmnopqrstuvwxyz}$$
&nbsp;              | `$$\mathscr{AB}AB$$`                                                   | $$\mathscr{AB}AB$$
`\mathsf`           | `$$\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$`                              | $$\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$$
&nbsp;              | `$$\mathsf{0123456789}$$`                                              | $$\mathsf{0123456789}$$
&nbsp;              | `$$\mathsf{abcdefghijklmnopqrstuvwxyz}$$`                              | $$\mathsf{abcdefghijklmnopqrstuvwxyz}$$
&nbsp;              | `$$\mathsf{AB}AB$$`                                                    | $$\mathsf{AB}AB$$
`\matrix`           | `$$\matrix{ a & b \cr c & d }$$`                                       | $$\matrix{ a & b \cr c & d }$$
`\max`              | `$$\max_{\rm sub}$$`                                                   | $$\max_{\rm sub}$$
`\measuredangle`    | `$$\measuredangle$$`                                                   | $$\measuredangle$$
`\mho`              | `$$\mho$$`                                                             | $$\mho$$
`\mid`              | `$$\{x \mid x\gt 1\}$$`                                                | $$\{x \mid x\gt 1\}$$
`\models`           | `$$\models$$`                                                          | $$\models$$
`\mp`               | `$$\mp$$`                                                              | $$\mp$$
`\mu`               | `$$\mu$$`                                                              | $$\mu$$
`\multimap`         | `$$\multimap$$`                                                        | $$\multimap$$

### N

\(\LaTeX\) Command  | Syntax Examples                                                        | `MathJax.js` Output
--------------------|------------------------------------------------------------------------|--------------------------------------
`\nabla`            | `$$\nabla$$`                                                           | $$\nabla$$
`\natural`          | `$$\natural$$`                                                         | $$\natural$$
`\ncong`            | `$$\ncong$$`                                                           | $$\ncong$$
`\ne`               | `$$\ne$$`                                                              | $$\ne$$
`\nearrow`          | `$$\nearrow$$`                                                         | $$\nearrow$$
`\neg`              | `$$\neg$$`                                                             | $$\neg$$
`\neq`              | `$$\neq$$`                                                             | $$\neq$$
`\nexists`          | `$$\nexists$$`                                                         | $$\nexists$$
`\ngeq`             | `$$\ngeq$$`                                                            | $$\ngeq$$
`\ngeqq`            | `$$\ngeqq$$`                                                           | $$\ngeqq$$
`\ngeqslant`        | `$$\ngeqslant$$`                                                       | $$\ngeqslant$$
`\ngtr`             | `$$\ngtr$$`                                                            | $$\ngtr$$
`\ni`               | `$$\ni$$`                                                              | $$\ni$$
`\nleftarrow`       | `$$\nleftarrow$$`                                                      | $$\nleftarrow$$
`\nLeftarrow`       | `$$\nLeftarrow$$`                                                      | $$\nLeftarrow$$
`\nleftrightarrow`  | `$$\nleftrightarrow$$`                                                 | $$\nleftrightarrow$$
`\nLeftrightarrow`  | `$$\nLeftrightarrow$$`                                                 | $$\nLeftrightarrow$$
`\nleq`             | `$$\nleq$$`                                                            | $$\nleq$$
`\nleqq`            | `$$\nleqq$$`                                                           | $$\nleqq$$
`\nleqslant`        | `$$\nleqslant$$`                                                       | $$\nleqslant$$
`\nless`            | `$$\nless$$`                                                           | $$\nless$$
`\nmid`             | `$$\nmid$$`                                                            | $$\nmid$$
`\not`              | `$$\not$$`                                                             | $$\not$$
`\notin`            | `$$\notin$$`                                                           | $$\notin$$
`\nparallel`        | `$$\nparallel$$`                                                       | $$\nparallel$$
`\nprec`            | `$$\nprec$$`                                                           | $$\nprec$$
`\npreceq`          | `$$\npreceq$$`                                                         | $$\npreceq$$
`\nrightarrow`      | `$$\nrightarrow$$`                                                     | $$\nrightarrow$$
`\nRightarrow`      | `$$\nRightarrow$$`                                                     | $$\nRightarrow$$
`\nshortmid`        | `$$\nshortmid$$`                                                       | $$\nshortmid$$
`\nshortparallel`   | `$$\nshortparallel$$`                                                  | $$\nshortparallel$$
`\nsim`             | `$$\nsim$$`                                                            | $$\nsim$$
`\nsubseteq`        | `$$\nsubseteq$$`                                                       | $$\nsubseteq$$
`\nsubseteqq`       | `$$\nsubseteqq$$`                                                      | $$\nsubseteqq$$
`\nsucc`            | `$$\nsucc$$`                                                           | $$\nsucc$$
`\nsucceq`          | `$$\nsucceq$$`                                                         | $$\nsucceq$$
`\nsupseteq`        | `$$\nsupseteq$$`                                                       | $$\nsupseteq$$
`\nsupseteqq`       | `$$\nsupseteqq$$`                                                      | $$\nsupseteqq$$
`\ntriangleleft`    | `$$\ntriangleleft$$`                                                   | $$\ntriangleleft$$
`\ntrianglelefteq`  | `$$\ntrianglelefteq$$`                                                 | $$\ntrianglelefteq$$
`\ntriangleright`   | `$$\ntriangleright$$`                                                  | $$\ntriangleright$$
`\ntrianglerighteq` | `$$\ntrianglerighteq$$`                                                | $$\ntrianglerighteq$$
`\nu`               | `$$\nu$$`                                                              | $$\nu$$
`\nVDash`           | `$$\nVDash$$`                                                          | $$\nVDash$$
`\nVdash`           | `$$\nVdash$$`                                                          | $$\nVdash$$
`\nvDash`           | `$$\nvDash$$`                                                          | $$\nvDash$$
`\nvdash`           | `$$\nvdash$$`                                                          | $$\nvdash$$
`\nwarrow`          | `$$\nwarrow$$`                                                         | $$\nwarrow$$

### O

\(\LaTeX\) Command    | Syntax Examples                                                      | `MathJax.js` Output
----------------------|----------------------------------------------------------------------|--------------------------------------
`\odot`               | `$$\odot$$`                                                          | $$\odot$$
`\oplus`              | `$$\oplus$$`                                                         | $$\oplus$$
`\ominus`             | `$$\ominus$$`                                                        | $$\ominus$$
`\oslash`             | `$$\oslash$$`                                                        | $$\oslash$$
`\otimes`             | `$$\otimes$$`                                                        | $$\otimes$$
`\oint`               | `$$\oint$$`                                                          | $$\oint$$
`\omega`              | `$$\omega$$`                                                         | $$\omega$$
`\Omega`              | `$$\Omega$$`                                                         | $$\Omega$$
`\omicron`            | `$$\omicron$$`                                                       | $$\omicron$$
`\over`               | `$$a \over b$$`                                                      | $$a \over b$$
&nbsp;                | `$${a+1 \over b+2}+c$$`                                              | $${a+1 \over b+2}+c$$
`\overbrace`          | `$$\overbrace{x+ \cdots +x}_{\text{(text note)}}^{n\text{ times}}$$` | $$\overbrace{x+ \cdots +x}_{\text{(text note)}}^{n\text{ times}}$$
`\overleftarrow`      | `$$\overleftarrow{\text{the argument}}$$`                            | $$\overleftarrow{\text{the argument}}$$
`\overrighttarrow`    | `$$\overrighttarrow{AB}$$`                                           | $$\overrightarrow{AB}$$
`\overleftrightarrow` | `$$\overleftrightarrow{\hspace1in}$$`                                | $$\overleftrightarrow{\hspace1in}$$
`\overline`           | `$$\overline{AB}$$`                                                  | $$\overline{AB}$$
`\overline`           | `$$\overline{\text{a long argument}}$$`                              | $$\overline{\text{a long argument}}$$
`\overset`            | `$$\overset{\rm top}{\rm bottom}$$`                                  | $$\overset{\rm top}{\rm bottom}$$
`\overset`            | `$$a\,\overset{?}{=}\,b$$`                                           | $$a\,\overset{?}{=}\,b$$
`\overwithdelims`     | `$$a \overwithdelims [ ] b$$`                                        | $$a \overwithdelims [ ] b$$
`\overwithdelims`     | `$${a+1 \overwithdelims \{ \} b+2}+c$$`                              | $${a+1 \overwithdelims \{ \} b+2}+c$$

### P

\(\LaTeX\) Command    | Syntax Examples                                                      | `MathJax.js` Output
----------------------|----------------------------------------------------------------------|--------------------------------------
`\parallel`           | `$$\parallel$$`                                                      | $$\parallel$$
`\partial`            | `$$\partial$$`                                                       | $$\partial$$
`\perp`               | `$$\perp$$`                                                          | $$\perp$$
`\phantom`            | `$$\sqrt{\phantom{\frac ab}}$$`                                      | $$\sqrt{\phantom{\frac ab}}$$
&nbsp;                | `$$\Gamma^{\phantom{i}j}_{i\phantom{j}k}$$`                          | $$\Gamma^{\phantom{i}j}_{i\phantom{j}k}$$
`\phi`                | `$$\phi$$`                                                           | $$\phi$$
`\Phi`                | `$$\Phi$$`                                                           | $$\Phi$$
`\pi`                 | `$$\pi$$`                                                            | $$\pi$$
`\Pi`                 | `$$\Pi$$`                                                            | $$\Pi$$
`\pitchfork`          | `$$\pitchfork$$`                                                     | $$\pitchfork$$
`\pm`                 | `$$\pm$$`                                                            | $$\pm$$
`\pmatrix`            | `$$A = \pmatrix{a_{11} & a_{12} & \ldots & a_{1n} \cr a_{21} & a_{22} & \ldots & a_{2n} \cr \vdots & \vdots & \ddots & \vdots \cr a_{m1} & a_{m2} & \ldots & a_{mn} \cr}$$` | $$A = \pmatrix{a_{11} & a_{12} & \ldots & a_{1n} \cr a_{21} & a_{22} & \ldots & a_{2n} \cr \vdots & \vdots & \ddots & \vdots \cr a_{m1} & a_{m2} & \ldots & a_{mn} \cr}$$
`\prec`               | `$$\prec$$`                                                          | $$\prec$$
`\precapprox`         | `$$\precapprox$$`                                                    | $$\precapprox$$
`\precnapprox`        | `$$\precnapprox$$`                                                   | $$\precnapprox$$
`\preccurlyeq`        | `$$\preccurlyeq$$`                                                   | $$\preccurlyeq$$
`\preceq`             | `$$\preceq$$`                                                        | $$\preceq$$
`\precneqq`           | `$$\precneqq$$`                                                      | $$\precneqq$$
`\precsim`            | `$$\precsim$$`                                                       | $$\precsim$$
`\precnsim`           | `$$\precnsim$$`                                                      | $$\precnsim$$
`\prime`              | `$$\prime$$`                                                         | $$\prime$$
`\prod`               | `$$\prod_{j=1}^n$$`                                                  | $$\prod_{j=1}^n$$
`\propto`             | `$$\propto$$`                                                        | $$\propto$$
`\psi`                | `$$\psi$$`                                                           | $$\psi$$
`\Psi`                | `$$\Psi$$`                                                           | $$\Psi$$

### Q

\(\LaTeX\) Command    | Syntax Examples                                                      | `MathJax.js` Output
----------------------|----------------------------------------------------------------------|--------------------------------------
`\quad`               | `$$\|\quad\|\quad\|$$`                                               | $$\|\quad\|\quad\|$$

### R

\(\LaTeX\) Command    | Syntax Examples                                                      | `MathJax.js` Output
----------------------|----------------------------------------------------------------------|--------------------------------------
`\raise`              | `$$h\raise 2pt {ighe} r$$`                                           | $$h\raise 2pt {ighe} r$$
`\rangle`             | `$$\left\langle \matrix{a & b\cr c & d} \right\rangle$$`             | $$\left\langle \matrix{a & b\cr c & d} \right\rangle$$
`\rbrace`             | `$$\left\lbrace \matrix{a & b\cr c & d} \right\rbrace$$`             | $$\left\lbrace \matrix{a & b\cr c & d} \right\rbrace$$
`\rceil`              | `$$\left\lceil \matrix{a & b\cr c & d} \right\rceil$$`               | $$\left\lceil \matrix{a & b\cr c & d} \right\rceil$$
`\Re`                 | `$$\Re$$`                                                            | $$\Re$$
`\restriction`        | `$$\restriction$$`                                                   | $$\restriction$$
`\rfloor`             | `$$\rfloor$$`                                                        | $$\rfloor$$
`\rhd`                | `$$\rhd$$`                                                           | $$\rhd$$
`\rho`                | `$$\rho$$`                                                           | $$\rho$$
`\right`              | `$$\left( \frac12 \right)$$`                                         | $$\left( \frac12 \right)$$
`\rightarrow`         | `$$\rightarrow$$`                                                    | $$\rightarrow$$
`\Rightarrow`         | `$$\Rightarrow$$`                                                    | $$\Rightarrow$$
`\rightarrowtail`     | `$$\rightarrowtail$$`                                                | $$\rightarrowtail$$
`\rightharpoondown`   | `$$\rightharpoondown$$`                                              | $$\rightharpoondown$$
`\rightharpoonup`     | `$$\rightharpoonup$$`                                                | $$\rightharpoonup$$
`\rightleftarrows`    | `$$\rightleftarrows$$`                                               | $$\rightleftarrows$$
`\rightleftharpoons`  | `$$\rightleftharpoons$$`                                             | $$\rightleftharpoons$$
`\rightrightarrows`   | `$$\rightrightarrows$$`                                              | $$\rightrightarrows$$
`\rightsquigarrow`    | `$$\rightsquigarrow$$`                                               | $$\rightsquigarrow$$
`\rightthreetimes`    | `$$\rightthreetimes$$`                                               | $$\rightthreetimes$$
`\risingdotseq`       | `$$\risingdotseq$$`                                                  | $$\risingdotseq$$
`\rlap`               | `$$a\mathrel{\rlap{\;/}{=}}b$$`                                      | $$a\mathrel{\rlap{\;/}{=}}b$$
`\rmoustache`         | `$$\rmoustache$$`                                                    | $$\rmoustache$$
`\root`               | `$$\root 3 \of x$$`                                                  | $$\root 3 \of x$$
&nbsp;                | `$$\root 13 \of {\frac 12} $$`                                       | $$\root 13 \of {\frac 12}$$
`\Rrightarrow`        | `$$\Rrightarrow$$`                                                   | $$\Rrightarrow$$
`\Rsh`                | `$$\Rsh$$`                                                           | $$\Rsh$$
`\rtimes`             | `$$\rtimes$$`                                                        | $$\rtimes$$
`\rvert`              | `$$\left\lvert\frac{\frac ab}{\frac cd}\right\rvert$$`               | $$\left\lvert\frac{\frac ab}{\frac cd}\right\rvert$$

### S

\(\LaTeX\) Command    | Syntax Examples                                                      | `MathJax.js` Output
----------------------|----------------------------------------------------------------------|--------------------------------------
`\searrow`            | `$$\searrow$$`                                                       | $$\searrow$$
`\sec`                | `$$\sec$$`                                                           | $$\sec$$
`\setminus`           | `$$A\setminus B$$`                                                   | $$A\setminus B$$
`\sharp`              | `$$\sharp$$`                                                         | $$\sharp$$
`\shortmid`           | `$$\shortmid$$`                                                      | $$\shortmid$$
`\shortparallel`      | `$$\shortparallel$$`                                                 | $$\shortparallel$$
`\shoveleft`          | `$$\begin{multline} (a+b+c+d)^2 \\ \shoveleft{+ (e+f)^2 + (g+h)^2 + (i+j)^2 + (k+l)^2} \\ + (m+n)^2 + (o+p)^2 + (q+r)^2 + (s+t)^2 + (u+v)^2 \\ + (w+x+y+z)^2 \end{multline}$$` | $$\begin{multline} (a+b+c+d)^2 \\ + (e+f)^2 + (g+h)^2 + (i+j)^2 + (k+l)^2 \\ + (m+n)^2 + (o+p)^2 + (q+r)^2 + (s+t)^2 + (u+v)^2 \\ + (w+x+y+z)^2 \end{multline}$$
`\sideset`            | `$$\sideset{_1^2}{_3^4}\sum$$`                                       | $$\sideset{_1^2}{_3^4}\sum$$
`\sigma`              | `$$\sigma$$`                                                         | $$\sigma$$
`\Sigma`              | `$$\Sigma$$`                                                         | $$\Sigma$$
`\sim`                | `$$\sim$$`                                                           | $$\sim$$
`\simeq`              | `$$\simeq$$`                                                         | $$\simeq$$
`\sin`                | `$$\sin$$`                                                           | $$\sin$$
`\sinh`               | `$$\sinh$$`                                                          | $$\sinh$$
`\sinh `              | `$$\sinh$$`                                                          | $$\sinh$$
`\small`              | `$$\rm\tiny tiny \Tiny Tiny \small small \normalsize normal \large lg \Large Lg \LARGE LG \huge hg \Huge Hg$$` | $$\rm\tiny tiny \Tiny Tiny \small small \normalsize normal \large lg \Large Lg \LARGE LG \huge hg \Huge Hg$$
`\smallfrown`         | `$$\smallfrown$$`                                                    | $$\smallfrown$$
`\smallint`           | `$$\smallint$$`                                                      | $$\smallint$$
`\smallsetminus`      | `$$\smallsetminus$$`                                                 | $$\smallsetminus$$
`\smallsmile`         | `$$\smallsmile$$`                                                    | $$\smallsmile$$
`\smile`              | `$$\smile$$`                                                         | $$\smile$$
`\spadesuit`          | `$$\spadesuit$$`                                                     | $$\spadesuit$$
`\sphericalangle`     | `$$\sphericalangle$$`                                                | $$\sphericalangle$$
`\sqcap`              | `$$\sqcap$$`                                                         | $$\sqcap$$
`\sqcup`              | `$$\sqcup$$`                                                         | $$\sqcup$$
`\sqrt`               | `$$\sqrt x$$`                                                        | $$\sqrt x$$
&nbsp;                | `$$\sqrt xy$$`                                                       | $$\sqrt xy$$
&nbsp;                | `$$\sqrt{xy}$$`                                                      | $$\sqrt{xy}$$
&nbsp;                | `$$\sqrt[3]{x+1}$$`                                                  | $$\sqrt[3]{x+1}$$
`\sqsubset`           | `$$\sqsubset$$`                                                      | $$\sqsubset$$
`\sqsupset`           | `$$\sqsupset$$`                                                      | $$\sqsupset$$
`\sqsubseteq`         | `$$\sqsubseteq$$`                                                    | $$\sqsubseteq$$
`\sqsupseteq`         | `$$\sqsupseteq$$`                                                    | $$\sqsupseteq$$
`\square`             | `$$\square$$`                                                        | $$\square$$
`\stackrel`           | `$$\stackrel{\rm def}{=}$$`                                          | $$\stackrel{\rm def}{=}$$
`\star`               | `$$\star$$`                                                          | $$\star$$
`\strut`              | `$$\sqrt{(\ )} \sqrt{\mathstrut\rm mathstrut} \sqrt{\strut\rm strut}$$`| $$\sqrt{(\ )} \sqrt{\mathstrut\rm mathstrut} \sqrt{\strut\rm strut}$$
`\subset`             | `$$\subset$$`                                                        | $$\subset$$
`\Subset`             | `$$\Subset$$`                                                        | $$\Subset$$
`\subseteq`           | `$$\subseteq$$`                                                      | $$\subseteq$$
`\subsetneq`          | `$$\subsetneq$$`                                                     | $$\subsetneq$$
`\subseteqq`          | `$$\subseteqq$$`                                                     | $$\subseteqq$$
`\subsetneqq`         | `$$\subsetneqq$$`                                                    | $$\subsetneqq$$
`\substack`           | `$$\sum_{ \substack{ 1\lt i\lt 3, 1\le j\lt 5 }} a_{ij}$$`           | $$\sum_{ \substack{ 1\lt i\lt 3, 1\le j\lt 5 }} a_{ij}$$
`\succ`               | `$$\succ$$`                                                          | $$\succ$$
`\succapprox`         | `$$\succapprox$$`                                                    | $$\succapprox$$
`\succnapprox`        | `$$\succnapprox$$`                                                   | $$\succnapprox$$
`\succcurlyeq`        | `$$\succcurlyeq$$`                                                   | $$\succcurlyeq$$
`\succeq`             | `$$\succeq$$`                                                        | $$\succeq$$
`\succneqq`           | `$$\succneqq$$`                                                      | $$\succneqq$$
`\succsim`            | `$$\succsim$$`                                                       | $$\succsim$$
`\succnsim`           | `$$\succnsim$$`                                                      | $$\succnsim$$
`\sum`                | `$$\sum$$`                                                           | $$\sum$$
`\sup`                | `$$\sup$$`                                                           | $$\sup$$
`\supset`             | `$$\supset$$`                                                        | $$\supset$$
`\Supset`             | `$$\Supset$$`                                                        | $$\Supset$$
`\supseteq`           | `$$\supseteq$$`                                                      | $$\supseteq$$
`\supsetneq`          | `$$\supsetneq$$`                                                     | $$\supsetneq$$
`\supseteqq`          | `$$\supseteqq$$`                                                     | $$\supseteqq$$
`\supsetneqq`         | `$$\supsetneqq$$`                                                    | $$\supsetneqq$$
`\surd`               | `$$\surd$$`                                                          | $$\surd$$
`\swarrow`            | `$$\swarrow$$`                                                       | $$\swarrow$$

### T

\(\LaTeX\) Command    | Syntax Examples                                                      | `MathJax.js` Output
----------------------|----------------------------------------------------------------------|--------------------------------------
`\tag`                | `$$\eqalign{3x - 4y &= 5\cr x + 7 &= -2y} \tag{3.1c}$$`              | $$\eqalign{3x - 4y &= 5\cr x + 7 &= -2y} \tag{3.1c}$$
`\tan`                | `$$\tan$$`                                                           | $$\tan$$
`\tanh`               | `$$\tanh$$`                                                          | $$\tanh$$
`\tau`                | `$$\tau$$`                                                           | $$\tau$$
`\TeX`                | `$$\TeX$$`                                                           | $$\TeX$$
`\therefore`          | `$$\therefore$$`                                                     | $$\therefore$$
`\theta`              | `$$\theta$$`                                                         | $$\theta$$
`\Theta`              | `$$\Theta$$`                                                         | $$\Theta$$
`\thickapprox`        | `$$approx\ \ \thickapprox$$`                                         | $$approx\ \ \thickapprox$$
`\thicksim`           | `$$sim\ \ \thicksim $$`                                              | $$sim\ \ \thicksim$$
`\tilde`              | `$$\tilde e$$`                                                       | $$\tilde e$$
 &nbsp;               | `$$\tilde E$$`                                                       | $$\tilde E$$
 &nbsp;               | `$$\tilde eu$$`                                                      | $$\tilde eu$$
 &nbsp;               | `$$\tilde{eu}$$`                                                     | $$\tilde{eu}$$
`\times`              | `$$\times$$`                                                         | $$\times$$
`\to`                 | `$$\to$$`                                                            | $$\to$$
`\top`                | `$$\top$$`                                                           | $$\top$$
`\triangle`           | `$$\triangle$$`                                                      | $$\triangle$$
`\triangledown`       | `$$\triangledown$$`                                                  | $$\triangledown$$
`\triangleleft`       | `$$\triangleleft$$`                                                  | $$\triangleleft$$
`\triangleright`      | `$$\triangleright$$`                                                 | $$\triangleright$$
`\trianglelefteq`     | `$$\trianglelefteq$$`                                                | $$\trianglelefteq$$
`\trianglerighteq`    | `$$\trianglerighteq$$`                                               | $$\trianglerighteq$$
`\triangleq`          | `$$\triangleq$$`                                                     | $$\triangleq$$
`\tt`                 | `$$\tt$$`                                                            | $$\tt$$
`\twoheadleftarrow`   | `$$\twoheadleftarrow$$`                                              | $$\twoheadleftarrow$$
`\twoheadrightarrow`  | `$$\twoheadrightarrow$$`                                             | $$\twoheadrightarrow$$

### U

\(\LaTeX\) Command     | Syntax Examples                                                      | `MathJax.js` Output
-----------------------|----------------------------------------------------------------------|--------------------------------------
`\ulcorner`            | `$$\ulcorner$$`                                                      | $$\ulcorner$$
`\urcorner`            | `$$\urcorner$$`                                                      | $$\urcorner$$
`\underbrace`          | `$$\underbrace{x+ \cdots +x}^{\text{(note here)}}_{n\text{ times}}$$`| $$\underbrace{x +\cdots +x}^{\text{(note here)}}_{n\text{ times}}$$
`\underleftarrow`      | `$$\underleftarrow{\text{the argument}}$$`                           | $$\underleftarrow{\text{the argument}}$$
`\underrightarrow`     | `$$\underrightarrow{AB}$$`                                           | $$\underrightarrow{AB}$$
&nbsp;                 | `$$\underrightarrow{AB\strut}$$`                                     | $$\underrightarrow{AB\strut}$$
`\underleftrightarrow` | `$$\underleftrightarrow{\hspace1in}$$`                               | $$\underleftrightarrow{\hspace1in}$$
`\underline`           | `$$\underline{AB}$$`                                                 | $$\underline{AB}$$
&nbsp;                 | `$$\underline{\text{a long argument}}$$`                             | $$\underline{\text{a long argument}}$$
`\underset`            | `$$\underset{\rm bottom}{\rm top}$$`                                 | $$\underset{\rm bottom}{\rm top}$$
`\unicode`             | `$$\unicode{x263a}$$`                                                | $$\unicode{x263a}$$
&nbsp;                 | `$$\unicode[.55,0.05]{x22D6}$$`                                      | $$\unicode[.55,0.05]{x22D6}$$
`\unlhd`               | `$$\unlhd$$`                                                         | $$\unlhd$$
`\unrhd`               | `$$\unrhd$$`                                                         | $$\unrhd$$
`\uparrow`             | `$$\uparrow$$`                                                       | $$\uparrow$$
`\Uparrow`             | `$$\Uparrow$$`                                                       | $$\Uparrow$$
`\updownarrow`         | `$$\updownarrow$$`                                                   | $$\updownarrow$$
`\Updownarrow`         | `$$\Updownarrow$$`                                                   | $$\Updownarrow$$
`\upharpoonleft`       | `$$\upharpoonleft$$`                                                 | $$\upharpoonleft$$
`\upharpoonright`      | `$$\upharpoonright$$`                                                | $$\upharpoonright$$
`\uplus`               | `$$\uplus$$`                                                         | $$\uplus$$
`\uproot`              | `$$\sqrt[3]{x}$$`                                                    | $$\sqrt[3]{x}$$
&nbsp;                 | `$$\sqrt[3\uproot2]{x}$$`                                            | $$\sqrt[3\uproot2]{x}$$
&nbsp;                 | `$$\root 3 \of x$$`                                                  | $$\root 3 \of x$$
&nbsp;                 | `$$\root 3\uproot{-2} \of x$$`                                       | $$\root 3\uproot{-2} \of x$$
`\upsilon`             | `$$\upsilon$$`                                                       | $$\upsilon$$
`\Upsilon`             | `$$\Upsilon$$`                                                       | $$\Upsilon$$
`\upuparrows`          | `$$\upuparrows$$`                                                    | $$\upuparrows$$

### V

\(\LaTeX\) Command     | Syntax Examples                                                      | `MathJax.js` Output
-----------------------|----------------------------------------------------------------------|--------------------------------------
`\varDelta`            | `$$\varDelta$$`                                                      | $$\varDelta$$
`\varepsilon`          | `$$\varepsilon$$`                                                    | $$\varepsilon$$
`\varGamma`            | `$$\varGamma$$`                                                      | $$\varGamma$$
`\varinjlim`           | `$$\varinjlim$$`                                                     | $$\varinjlim$$
`\varkappa`            | `$$\varkappa$$`                                                      | $$\varkappa$$
`\varLambda`           | `$$\varLambda$$`                                                     | $$\varLambda$$
`\varlimsup`           | `$$\varlimsup$$`                                                     | $$\varlimsup$$
`\varliminf`           | `$$\varliminf$$`                                                     | $$\varliminf$$
`\varnothing`          | `$$\varnothing$$`                                                    | $$\varnothing$$
`\varOmega`            | `$$\varOmega$$`                                                      | $$\varOmega$$
`\varphi`              | `$$\varphi$$`                                                        | $$\varphi$$
`\varPhi`              | `$$\varPhi$$`                                                        | $$\varPhi$$
`\varpi`               | `$$\varpi$$`                                                         | $$\varpi$$
`\varPi`               | `$$\varPi$$`                                                         | $$\varPi$$
`\varprojlim`          | `$$\varprojlim$$`                                                    | $$\varprojlim$$
`\varpropto`           | `$$\varpropto$$`                                                     | $$\varpropto$$
`\varPsi`              | `$$\varPsi$$`                                                        | $$\varPsi$$
`\varrho`              | `$$\varrho$$`                                                        | $$\varrho$$
`\varsigma`            | `$$\varsigma$$`                                                      | $$\varsigma$$
`\varSigma`            | `$$\varSigma$$`                                                      | $$\varSigma$$
`\varsubsetneq`        | `$$\varsubsetneq$$`                                                  | $$\varsubsetneq$$
`\varsubsetneqq`       | `$$\varsubsetneqq$$`                                                 | $$\varsubsetneqq$$
`\varsupsetneq`        | `$$\varsupsetneq$$`                                                  | $$\varsupsetneq$$
`\varsupsetneqq`       | `$$\varsupsetneqq$$`                                                 | $$\varsupsetneqq$$
`\vartheta`            | `$$\vartheta$$`                                                      | $$\vartheta$$
`\varTheta`            | `$$\varTheta$$`                                                      | $$\varTheta$$
`\vartriangle`         | `$$\vartriangle$$`                                                   | $$\vartriangle$$
`\vartriangleleft `    | `$$\vartriangleleft$$`                                               | $$\vartriangleleft$$
`\vartriangleright`    | `$$\vartriangleright$$`                                              | $$\vartriangleright$$
`\varUpsilon`          | `$$\varUpsilon$$`                                                    | $$\varUpsilon$$
`\varXi`               | `$$\varXi$$`                                                         | $$\varXi$$
`\vcenter`             | `$$\left(\Rule{1ex}{2em}{0pt}\right)$$`                              | $$\left(\Rule{1ex}{2em}{0pt}\right)$$
&nbsp;                 | `$$\left(\vcenter{\Rule{1ex}{2em}{0pt}}\right)$$`                    | $$\left(\vcenter{\Rule{1ex}{2em}{0pt}}\right)$$
&nbsp;                 | `$$\left(\frac{a+b}{\dfrac{c}{d}}\right)$$`                          | $$\left(\frac{a+b}{\dfrac{c}{d}}\right)$$
&nbsp;                 | `$$\left(\vcenter{\frac{a+b}{\dfrac{c}{d}}}\right)$$`                | $$\left(\vcenter{\frac{a+b}{\dfrac{c}{d}}}\right)$$
`\vdash`               | `$$\vdash$$`                                                         | $$\vdash$$
`\Vdash`               | `$$\Vdash$$`                                                         | $$\Vdash$$
`\vDash`               | `$$\dVash$$`                                                         | $$\vDash$$
`\vec`                 | `$$\vec v$$`                                                         | $$\vec v$$
&nbsp;                 | `$$\vec{AB}$$`                                                       | $$\vec{AB}$$
`\vee`                 | `$$\vee$$`                                                           | $$\vee$$
`\veebar`              | `$$\veebar$$`                                                        | $$\veebar$$
`\verb`                | `$$\verb*$x^2\sqrt y$* \text{ yields } x^2\sqrt y$$`                 | $$\verb*$x^2\sqrt y$* \text{ yields } x^2\sqrt y$$
&nbsp;                 | `$$\verb!Text and $\frac ab$ in \verb mode!$$`                       | $$\verb!Text and $\frac ab$ in \verb mode!$$
`\vert`                | `$$\vert$$`                                                          | $$\vert$$
`\Vert`                | `$$\Vert$$`                                                          | $$\Vert$$
`\vphantom`            | `$$\binom{\frac ab}c \binom{\vphantom{\frac ab}?}c$$`                | $$\binom{\frac ab}c \binom{\vphantom{\frac ab}?}c$$
`\Vvdash`              | `$$\Vvdash$$`                                                        | $$\Vvdash$$

### W

\(\LaTeX\) Command     | Syntax Examples                                                      | `MathJax.js` Output
-----------------------|----------------------------------------------------------------------|--------------------------------------
`\wedge`               | `$$\wedge$$`                                                         | $$\wedge$$
`\widehat`             | `$$\widehat a$$`                                                     | $$\widehat a$$
&nbsp;                 | `$$\widehat{AB}$$`                                                   | $$\widehat{AB}$$
`\widetilde`           | `$$\widetilde a$$`                                                   | $$\widetilde a$$
&nbsp;                 | `$$\widetilde{AB}$$`                                                 | $$\widetilde{AB}$$
`\wp`                  | `$$\wp$$`                                                            | $$\wp$$
`\wr`                  | `$$\wr$$`                                                            | $$\wr$$

### X

\(\LaTeX\) Command     | Syntax Examples                                                      | `MathJax.js` Output
-----------------------|----------------------------------------------------------------------|--------------------------------------
`\Xi`                  | `$$\Xi$$`                                                            | $$\Xi$$
`\xi`                  | `$$\xi$$`                                                            | $$\xi$$
`\xrightarrow`         | `$$\xrightarrow ab$$`                                                | $$\xrightarrow ab$$
`\xleftarrow`          | `$$\xleftarrow{\text{see equation (1)}}$$`                           | $$\xleftarrow{\text{see equation (1)}}$$

### Y   

\(\LaTeX\) Command     | Syntax Examples                                                      | `MathJax.js` Output
-----------------------|----------------------------------------------------------------------|--------------------------------------
`\yen`                 | `$$\yen$$`                                                           | $$\yen$$

### Z   

\(\LaTeX\) Command     | Syntax Examples                                                      | `MathJax.js` Output
-----------------------|----------------------------------------------------------------------|--------------------------------------
`\zet`                 | `$$\zeta$$`                                                          | $$\zeta$$

</div>
