<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>Image List</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="static/css/image.css">
  </head>
  <body>

  <script type="text/javascript">

    function showViewportDimensions() {
        var width = window.innerWidth;
        var height = window.innerHeight;
        alert('Viewport Width: ' + width + 'px\nViewport Height: ' + height + 'px');
    }

    /*
    (function() {
      var ga = document.createElement("script");
      ga.type = "text/javascript";
      ga.async = true;
      ga.src = ("https:" == document.location.protocol ? "https://ssl" : "http://www") + ".google-analytics.com/ga.js";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(ga, s);

      //showViewportDimensions();
    })();
    */

  </script>

  <h1>Day's</h1>
  <div id="brunodir" class="brunodirs">
    <p class="direntry">
    % for d in directories:
      <a href="dir/${d}" class="no-underline">
        ${d}<br>
      </a>
    % endfor
    </p>
  </div>
  </body>
</html>
