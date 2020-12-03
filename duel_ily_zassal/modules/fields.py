import vectors.py

class Field():
    def __init__(self, Bx, By, Bz, Ex, Ey ,Ez):
    """Field class                             
    """
    
    self.B = Vector(Bx, By, Bz)
    """Magnetic field induction
    """
    
    self.E = Vector(Ex, Ey, Ez)
    """Electric field strength
    """        
    
 	
    def calculate_force(self, bullets):
    '''Calculate force that move all objects in list of bullets.  
                                  
    Parameters:
            
    **buletts** - list of bullets.
    '''
        local = bullets
        for body in local:
            body.force = 0 * body.force
                    
            body.force = body.force + body.m_c * body.vel @ self.E 
            body.force = body.force - body.m_c * self.B
                
            body.force = body.force + body.e_c * body.vel @ self.B 
            body.force = body.force + body.e_c * self.E
            
        return local
        
        
            
                     
        