

def water_column_height(tower_height, tank_height):
    column_height = tower_height + (3*tank_height/4)
    return column_height


def pressure_gain_from_water_height(height):
    water_density = 998.2
    gravity = 9.80665
    pressure   = water_density * gravity * height / 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    water_density = 998.2 
    pressure_loss = ((-1)*friction_factor*pipe_length*water_density*fluid_velocity**2)/(pipe_diameter * 2000)
    return pressure_loss

