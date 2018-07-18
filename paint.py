def paint_fill( canvas, target_color, x, y ):
    # CHECK THAT THE POINT WAS IN THE CANVAS
    if not 0 <= x < canvas.shape[0]:
        return
    if not 0 <= y < canvas.shape[1]:
        return
    
    # GET THE COLOR TO CHANGE
    base_color = canvas[x][y]
    
    if (base_color == target_color):
    	return
    
    recursive_paint( canvas, x, y, base_color, target_color )
    
def recursive_paint( canvas, x, y, base_color, target_color ):
    # CHECK THAT THE POINT WAS IN THE CANVAS
    if not 0 <= x < canvas.shape[0]:
        return
    if not 0 <= y < canvas.shape[1]:
        return
    
    # GET THIS SPOT'S COLOR
    color = canvas[x][y]
    
    if (color == base_color):
        canvas[x][y] = target_color
         
        # RECURSE UP, RIGHT, DOWN, LEFT
        recursive_paint(canvas, x - 1, y, base_color, target_color )
        recursive_paint(canvas, x + 1, y, base_color, target_color )
        recursive_paint(canvas, x, y - 1, base_color, target_color )
        recursive_paint(canvas, x, y + 1, base_color, target_color )
        
    else:
        return