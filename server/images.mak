<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>Image List</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="../static/css/image.css?v=1.0">
  </head>
  <body>
  <!-- <script type="text/javascript" src="static/js/tosrus/jquery.js"></script> -->
  <!-- <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script> -->
  <!-- <script type="text/javascript" src="http://cdn.jsdelivr.net/hammerjs/2.0.3/hammer.min.js"></script> -->
  <!-- <script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js"></script> -->
  <!-- <script type="text/javascript" src="static/js/tosrus/js/jquery.tosrus.min.all.js"></script> -->
  <!--  <script type="text/javascript" src="static/js/imagelist.js"></script> -->
  <script type="text/javascript">
    var _gaq = _gaq || [];

    function showViewportDimensions() {
        var width = window.innerWidth;
        var height = window.innerHeight;
        alert('Viewport Width: ' + width + 'px\nViewport Height: ' + height + 'px');
    }
    (function() {
      //showViewportDimensions();
    })();

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

  <h1>Alarms</h1>
  <div id="kumalinks" class="kumaimages">
    % for i in images:
      <a href="${i['full']}">
        <img src="${i['thumb']}" width="8.5%" height="16%" />
      </a>
    % endfor
  </div>
  </body>
</html>
