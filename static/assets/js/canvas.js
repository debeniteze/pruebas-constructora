// Create two drawing tools.
  // tool1 will draw straight lines, tool2 will draw clouds.

  // Both share the mouseDown event:
  var path;
  function onMouseDown(event) {
      path = new Path();
      path.strokeColor = 'black';
      path.add(event.point);
  }
  window.app = {
      tool1: new Tool({
          onMouseDown: onMouseDown,
          onMouseDrag: function(event) {
              path.add(event.point);
          }
      }),

      tool2: new Tool({
          minDistance: 20,
          onMouseDown: onMouseDown,
          onMouseDrag: function(event) {
              // Use the arcTo command to draw cloudy lines
              path.arcTo(event.point);
          }
      })
  };
