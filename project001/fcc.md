# free code camp - django

- [source](https://www.youtube.com/watch?v=o0XbHvKxw7Y&t=6540s)
- [repo](https://github.com/csev/dj4e-samples/)

## html

source code - what's in the file. what's originally downloaded

DOM: not the same as source code; after the browser has loaded the source code. the browser took the source code, parsed it and produced the DOM. it fixes minor html source code mistakes. prettier version. we can change what is displayed in the DOM, but it doesn't chagne the DOM.

on file `broken.htm` we have a source code that is _broken_ but what happens is that the DOM fixes our mistakes and closes our missings tags

## CSS

selector: which part of the document does this rule apply to

```css
body {
  font-family: arial, sans-serif;
}
```

the closer it is, the more priority it has (unless they use !important - further away has priority)

```html
<head>
  <link type="text/css" rel="stylesheet" href="rules.css">
</head>
```

- `<span>` tag defined as having no default styling
- `<div>` tag is a block tag without inheriting styles
- `id` attribute is called from css with `#`
- `class` attributed is called from css with `.`

```html
<style>
  #first {
    font-family: monospace;
  }
  .second {
    background-color: yellow;
  }
  #third p {
    background-color: red;
  }
</style>
```

<https://youtu.be/o0XbHvKxw7Y?t=9372>






