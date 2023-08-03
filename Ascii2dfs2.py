from tkinter import Tk, filedialog
import os
import mikeio
import numpy as np

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
print("Select folder with Ascii Files")
folder = filedialog.askdirectory() # retrieve the folder directory

# for every ascii file within the forlder run the script
for file in os.listdir(folder):
    if file.endswith(".asc"):
        if file.startswith("Inf"):
            print("Import Infiltration file")
            # Read the ASCII file
            AsciiFile = f'{folder}/{file}'
            data = np.loadtxt(AsciiFile, skiprows=6)
            with open(AsciiFile, 'r') as file:
                ncols = int(file.readline().split()[1])
                nrows = int(file.readline().split()[1])
                xllcorner = float(file.readline().split()[1])
                yllcorner = float(file.readline().split()[1])
                cellsize = float(file.readline().split()[1])
                NODATA_value = float(file.readline().split()[1])
            # Reshape the data into a 2D array
            array = np.reshape(data, (nrows, -ncols))
            # Inverse the y axis
            array = array[::-1, :]
            # Define the geometry and as Mike uses the center of the fist cell for its origin, add a shift equal to half the cellsize
            geometry = mikeio.Grid2D(nx = ncols, ny= nrows, dx=cellsize, dy= cellsize,
                                    origin = (xllcorner+(cellsize/2), yllcorner+(cellsize/2)),
                                    projection= 'PROJCS["SWEREF99_12_00",GEOGCS["GCS_SWEREF99",DATUM["D_SWEREF99",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",150000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",12.0],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

            da_Inf = mikeio.DataArray(data=array,
                item=mikeio.ItemInfo("Infiltration", mikeio.EUMType.Infiltration),
                geometry=geometry,
                dims=("y","x") # No time dimension
                )
            
        elif file.startswith("Lea"):
            print("Import Leakage file")    
            # Read the ASCII file
            AsciiFile = f'{folder}/{file}'
            data = np.loadtxt(AsciiFile, skiprows=6)
            with open(AsciiFile, 'r') as file:
                ncols = int(file.readline().split()[1])
                nrows = int(file.readline().split()[1])
                xllcorner = float(file.readline().split()[1])
                yllcorner = float(file.readline().split()[1])
                cellsize = float(file.readline().split()[1])
                NODATA_value = float(file.readline().split()[1])
            # Reshape the data into a 2D array
            array = np.reshape(data, (nrows, -ncols))
            # Inverse the y axis
            array = array[::-1, :]
            # Define the geometry and as Mike uses the center of the fist cell for its origin, add a shift equal to half the cellsize
            geometry = mikeio.Grid2D(nx = ncols, ny= nrows, dx=cellsize, dy= cellsize,
                                    origin = (xllcorner+(cellsize/2), yllcorner+(cellsize/2)),
                                    projection= 'PROJCS["SWEREF99_12_00",GEOGCS["GCS_SWEREF99",DATUM["D_SWEREF99",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",150000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",12.0],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

            da_Lea = mikeio.DataArray(data=array,
                item=mikeio.ItemInfo("Leakage", mikeio.EUMType.Leakage),
                geometry=geometry,
                dims=("y","x") # No time dimension
                )
        elif file.startswith("Dep"):
            print("Import Depth Below Ground file")      
            # Read the ASCII file
            AsciiFile = f'{folder}/{file}'
            data = np.loadtxt(AsciiFile, skiprows=6)
            with open(AsciiFile, 'r') as file:
                ncols = int(file.readline().split()[1])
                nrows = int(file.readline().split()[1])
                xllcorner = float(file.readline().split()[1])
                yllcorner = float(file.readline().split()[1])
                cellsize = float(file.readline().split()[1])
                NODATA_value = float(file.readline().split()[1])
            # Reshape the data into a 2D array
            array = np.reshape(data, (nrows, -ncols))
            # Inverse the y axis
            array = array[::-1, :]
            # Define the geometry and as Mike uses the center of the fist cell for its origin, add a shift equal to half the cellsize
            geometry = mikeio.Grid2D(nx = ncols, ny= nrows, dx=cellsize, dy= cellsize,
                                    origin = (xllcorner+(cellsize/2), yllcorner+(cellsize/2)),
                                    projection= 'PROJCS["SWEREF99_12_00",GEOGCS["GCS_SWEREF99",DATUM["D_SWEREF99",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",150000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",12.0],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

            da_Dep = mikeio.DataArray(data=array,
                item=mikeio.ItemInfo("Depth Below Ground", mikeio.EUMType.Depth_Below_Ground),
                geometry=geometry,
                dims=("y","x") # No time dimension
                )
        
        elif file.startswith("Ini"):
            print("Import Initial Water Level file")  
            # Read the ASCII file
            AsciiFile = f'{folder}/{file}'
            data = np.loadtxt(AsciiFile, skiprows=6)
            with open(AsciiFile, 'r') as file:
                ncols = int(file.readline().split()[1])
                nrows = int(file.readline().split()[1])
                xllcorner = float(file.readline().split()[1])
                yllcorner = float(file.readline().split()[1])
                cellsize = float(file.readline().split()[1])
                NODATA_value = float(file.readline().split()[1])
            # Reshape the data into a 2D array
            array = np.reshape(data, (nrows, -ncols))
            # Inverse the y axis
            array = array[::-1, :]
            # Define the geometry and as Mike uses the center of the fist cell for its origin, add a shift equal to half the cellsize
            geometry = mikeio.Grid2D(nx = ncols, ny= nrows, dx=cellsize, dy= cellsize,
                                    origin = (xllcorner+(cellsize/2), yllcorner+(cellsize/2)),
                                    projection= 'PROJCS["SWEREF99_12_00",GEOGCS["GCS_SWEREF99",DATUM["D_SWEREF99",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",150000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",12.0],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

            da_Ini = mikeio.DataArray(data=array,
                item=mikeio.ItemInfo("Initial Water Content", mikeio.EUMType.Percentage),
                geometry=geometry,
                dims=("y","x") # No time dimension
                )
        elif file.startswith("Man"):
            print("Import Manning file")      
            # Read the ASCII file
            AsciiFile = f'{folder}/{file}'
            data = np.loadtxt(AsciiFile, skiprows=6)
            with open(AsciiFile, 'r') as file:
                ncols = int(file.readline().split()[1])
                nrows = int(file.readline().split()[1])
                xllcorner = float(file.readline().split()[1])
                yllcorner = float(file.readline().split()[1])
                cellsize = float(file.readline().split()[1])
                NODATA_value = float(file.readline().split()[1])
            # Reshape the data into a 2D array
            array = np.reshape(data, (nrows, -ncols))
            # Inverse the y axis
            array = array[::-1, :]
            # Define the geometry and as Mike uses the center of the fist cell for its origin, add a shift equal to half the cellsize
            geometry = mikeio.Grid2D(nx = ncols, ny= nrows, dx=cellsize, dy= cellsize,
                                    origin = (xllcorner+(cellsize/2), yllcorner+(cellsize/2)),
                                    projection= 'PROJCS["SWEREF99_12_00",GEOGCS["GCS_SWEREF99",DATUM["D_SWEREF99",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",150000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",12.0],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

            da_Man = mikeio.DataArray(data=array,
                item=mikeio.ItemInfo("Manning", mikeio.EUMType.Mannings_M),
                geometry=geometry,
                dims=("y","x") # No time dimension
                )
            print("Save Manning.dfs2 file")
            da_Man.to_dfs(f'{folder}/Manning.dfs2')
        elif file.startswith("Rai"):
            print("Import Rainfall file")      
            # Read the ASCII file
            AsciiFile = f'{folder}/{file}'
            data = np.loadtxt(AsciiFile, skiprows=6)
            with open(AsciiFile, 'r') as file:
                ncols = int(file.readline().split()[1])
                nrows = int(file.readline().split()[1])
                xllcorner = float(file.readline().split()[1])
                yllcorner = float(file.readline().split()[1])
                cellsize = float(file.readline().split()[1])
                NODATA_value = float(file.readline().split()[1])
            # Reshape the data into a 2D array
            array = np.reshape(data, (nrows, -ncols))
            # Inverse the y axis
            array = array[::-1, :]
            # Define the geometry and as Mike uses the center of the fist cell for its origin, add a shift equal to half the cellsize
            geometry = mikeio.Grid2D(nx = ncols, ny= nrows, dx=cellsize, dy= cellsize,
                                    origin = (xllcorner+(cellsize/2), yllcorner+(cellsize/2)),
                                    projection= 'PROJCS["SWEREF99_12_00",GEOGCS["GCS_SWEREF99",DATUM["D_SWEREF99",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",150000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",12.0],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

            da_Rai = mikeio.DataArray(data=array,
                item=mikeio.ItemInfo("Grid Data", mikeio.EUMType.Grid_Codes),
                geometry=geometry,
                dims=("y","x") # No time dimension
                )
            print("Save Rainfall_base.dfs2 file")
            da_Rai.to_dfs(f'{folder}/Rainfall_base.dfs2')
# Creating the array for porosity equal to 0,4
print("Create Porosity file")  
da_Por = mikeio.DataArray(data=(array>0)*0.4,
                item=mikeio.ItemInfo("Porosity", mikeio.EUMType.Porosity),
                geometry=geometry,
                dims=("y","x") # No time dimension
                )
# merging the dataarrays
# Convert the first array into dataset
ds_Inf = da_Inf._to_dataset()
# Add the subsequent arrays to the dataset
print("Merge Infiltration components into one file")  
ds_Inf["Leakage"]= da_Lea
ds_Inf["Initial water Contant"]= da_Ini
ds_Inf["Depth Below Ground"]= da_Dep
ds_Inf["Porosity"]= da_Por

# Save the dataset into a dfs2
print("Save Infiltration.dfs2 file")
ds_Inf.to_dfs(f'{folder}/Infiltration.dfs2')

print("Done")
