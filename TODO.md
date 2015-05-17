Todo
====

Issues found while using in the wild

Functionallity
--------------

- [x] don't override patch `id` if `id` is already defined by the element
- [ ] create warning for removing empty elements with id or class

Error Handling
--------------

- [ ] missing required files:
    - [ ] `patch` files
        1. [ ] `index.html`

Robust Regex
------------

- [x] allow whitespace in pagevars:

      turn 
        FIRST_KEY_RE = re.compile(r'[A-Za-z0-9_-]+:')
        KEY_VALUE_RE = re.compile(r'^[ ]{0,3}(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.*)')
      
      into 
        FIRST_KEY_RE = re.compile(r'[A-Za-z0-9_-]+[ \t]*:')
        KEY_VALUE_RE = re.compile(r'^[ ]{0,3}(?P<key>[A-Za-z0-9_-]+)[ \t]*:\s*(?P<value>.*)')

      