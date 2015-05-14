Todo
====

Issues found while using in the wild

Functionallity
--------------

- [x] don't override patch `id` if `id` is already defined by the element

Error Handling
--------------

- [ ] missing required files:
    - [ ] `patch` files
        1. [ ] `index.html`

Robust Regex
------------

- [x] allow whitespace in pagevars:

      turn `FIRST_KEY_RE = re.compile(r'[A-Za-z0-9_-]+:')`
      
      into `FIRST_KEY_RE = re.compile(r'[A-Za-z0-9_-]+[ \t]*:')`

      