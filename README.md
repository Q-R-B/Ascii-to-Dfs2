# Ascii-to-Dfs2
Converts Ascii files to dfs2 format 

This script import the folowing ascii files, will save the Manning and Rainfall file as .dfs2 and will merge the Infiltration components (infiltration, Leakage, depth below ground, initial water content and porosity) into a single dfs2 file named Infiltration.
In order to work, the input ascii files need to be named with at least the three first letters of the following names (First letter must be upper case):
- Infiltration
- Leakage
- Depth below ground
- Initial water content
- Rainfall
- Manning
	
The Dfs2 files will be saved in the same folder.

After running the script, the folder should looks something like:

![image](https://github.com/Q-R-B/Ascii-to-Dfs2/assets/103583383/97c509da-67db-4636-9a07-29b419f5995b)

