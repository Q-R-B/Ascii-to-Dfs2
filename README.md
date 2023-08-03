# Ascii-to-Dfs2
Converts Ascii files to dfs2 format 

This script converts ascii file created by the Qgis model file builder into dfs2 and will merge the Infiltration components into a single dfs2 file named Infiltration.
In order to work, the input ascii files need to be named with at least the three first letters of the following names (First letter must be upper case): /n 
	- Infiltration /n
	- Leakage /n
	- Depth below ground /n
	- Initial water content /n
	- Rainfall /n
	- Manning /n
	
The Dfs2 files will be saved in the same folder.

After running the script, the folder should looks something like:

![image](https://github.com/Q-R-B/Ascii-to-Dfs2/assets/103583383/97c509da-67db-4636-9a07-29b419f5995b)

