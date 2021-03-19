{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img style=\"float: left;\" src=\"earth-lab-logo-rgb.png\" width=\"150\" height=\"150\" />\n",
    "\n",
    "# Earth Analytics Education - EA  Python Course Spring 2021"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Important  - Assignment Guidelines\n",
    "\n",
    "1. Before you submit your assignment to GitHub, make sure to run the entire notebook with a fresh kernel. To do this first, **restart the kernel** (in the menubar, select Kernel$\\rightarrow$Restart & Run All)\n",
    "2. Always replace the `raise NotImplementedError()` code with your code that addresses the activity challenge. If you don't replace that code, your notebook will not run.\n",
    "\n",
    "```\n",
    "# YOUR CODE HERE\n",
    "raise NotImplementedError()\n",
    "```\n",
    "\n",
    "3. Any open ended questions will have a \"YOUR ANSWER HERE\" within a markdown cell. Replace that text with your answer also formatted using Markdown.\n",
    "4. **DO NOT RENAME THIS NOTEBOOK File!** If the file name changes, the autograder will not grade your assignment properly.\n",
    "6. When you create a figure, comment out `plt.show()` to ensure the autograder can grade your plots. For figure cells, DO NOT DELETE the code that says `DO NOT REMOVE LINE BELOW`.\n",
    "\n",
    "```\n",
    "### DO NOT REMOVE LINE BELOW ###\n",
    "student_plot1_ax = nb.convert_axes(plt)\n",
    "```\n",
    "\n",
    "* Only include the package imports, code, and outputs that are required to run your homework assignment.\n",
    "* Be sure that your code can be run on any operating system. This means that:\n",
    "   1. the data should be downloaded in the notebook to ensure it's reproducible\n",
    "   2. all paths should be created dynamically using the `os.path.join`\n",
    "\n",
    "## Follow to PEP 8 Syntax Guidelines & Documentation\n",
    "\n",
    "* Run the `autopep8` tool on all cells prior to submitting (HINT: hit shift + the tool to run it on all cells at once!\n",
    "* Use clear and expressive names for variables. \n",
    "* Organize your code to support readability.\n",
    "* Check for code line length\n",
    "* Use comments and white space sparingly where it is needed\n",
    "* Make sure all python imports are at the top of your notebook and follow PEP 8 order conventions\n",
    "* Spell check your Notebook before submitting it.\n",
    "\n",
    "For all of the plots below, be sure to do the following:\n",
    "\n",
    "* Make sure each plot has a clear TITLE and, where appropriate, label the x and y axes. Be sure to include UNITS in your labels.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Add Your Name Below \n",
    "**Your Name:** Libby Ives"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img style=\"float: left;\" src=\"colored-bar.png\"/>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "482b6a6fad5a6b7297cd1f14b52b28e1",
     "grade": false,
     "grade_id": "hw-instructions",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# Week 04 and 05 Homework - Automate NDVI Workflow\n",
    "\n",
    "For this assignment, you will write code to generate a plot of the mean normalized difference vegetation index (NDVI) for two different sites in the United States across one year of data:\n",
    "\n",
    "* San Joaquin Experimental Range (SJER) in Southern California, United States\n",
    "* Harvard Forest (HARV) in the Northeastern United States\n",
    "\n",
    "The data that you will use for this week is available from **earthpy** using the following download: \n",
    "\n",
    "`et.data.get_data('ndvi-automation')`\n",
    "\n",
    "## Assignment Goals\n",
    "\n",
    "Your goal in this assignment is to create the most efficient and concise workflow that you can that allows for:\n",
    "\n",
    "1. The code to scale if you added new sites or more time periods to the analysis.\n",
    "2. Someone else to understand your workflow.\n",
    "3. The LEAST and most efficient (i.e. runs fast, minimize repetition) amount of code that completes the task.\n",
    "\n",
    "### HINTS\n",
    "\n",
    "* Remove values outside of the landsat valid range of values as specified in the metadata, as needed.\n",
    "* Keep any output files SEPARATE FROM input files. Outputs should be created in an outputs directory that is created in the code (if needed) and/or tested for.\n",
    "* Use the functions that we demonstrated during class to make your workflow more efficient.\n",
    "* BONUS - if you  chose - you can export your data as a csv file. You will get bonus points for doing this.\n",
    "\n",
    "\n",
    "## Assignment Requirements\n",
    "\n",
    "Your submission to the GitHub repository should include:\n",
    "* This Jupyter Notebook file (.ipynb) with:\n",
    "    * The code to create a plot of mean NDVI across a year for  2 NEON Field Sites:\n",
    "        * NDVI on the x axis and formatted dates on the y for both NEON sites on one figure/axis object\n",
    "    * The **data should be cleaned to remove the influence of clouds**. See the [earthdatascience website for an example of what your plot might look like with and without removal of clouds](https://www.earthdatascience.org/courses/earth-analytics-python/create-efficient-data-workflows/).\n",
    "* BONUS: Create one output `.csv` file that has 3 columns - NDVI, Date and Site Name - with values for SJER and HARV.\n",
    "\n",
    "Your notebook should:\n",
    "* Have *at least* 2 well documented and well named functions with docstrings.\n",
    "* Include a Markdown cell at the top of the notebook that outlines the overall workflow using pseudocode (i.e. plain language, not code)\n",
    "* Include additional Markdown cells throughout the notebook to describe: \n",
    "    * the data that you used - and where it is from\n",
    "    * how data are being processing\n",
    "    * how the code is optimized to run fast and be more concise"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "ca51bc48f62e7d3602d0567f742e1b15",
     "grade": false,
     "grade_id": "pseudo-code",
     "locked": true,
     "points": 15,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "# Replace this cell with your pseudocode  for this workflow\n",
    "\n",
    "If you happen to be a diagram person a diagram is ok too\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pseudocode And Outline for Landsat8 NDVI Difference Workflow\n",
    "\n",
    "The purpose of this code is to calcuate the **Nomalized Difference Vegetation Index** (__[NDVI](http://earthobservatory.nasa.gov/features/MeasuringVegetation/measuring_vegetation_2.php)__) for 1 or more discrete sites, for some period of time based on Landsat8 data.\n",
    "\n",
    "### Primary Code Output:\n",
    "* Panda dataframe with columns for:\n",
    "    * Site name\n",
    "    * Date (in time-series format!)\n",
    "    * Mean NDVI for site\n",
    "* This dataframe can be used to make plots and output files\n",
    "\n",
    "### Code Steps\n",
    "1. Open bands needed for NDVI: red and infrared\n",
    "    * go into each scene directory and open bands 4 and 5 (i.e. index 3 and 4)\n",
    "2. Crop bands to study site boundary\n",
    "    * there is a site boundary for each site under vector (e.g. `data/ndvi-automation/sites/SJER/vector/`)\n",
    "3. Calculate NDVI for the scene (i.e. scene - set of bands for a particular spatial area).\n",
    "    * result is numpy array that contains all NDVI values for all pixels\n",
    "4. Calculate mean of the NDVI array.\n",
    "    * result is one mean NDVI value for the scene (to be stored in the Mean NDVI column)\n",
    "5. Parse directory name for site name.\n",
    "    * see the cells in the section below on os and glob to help with this task. \n",
    "6. Parse directory name or file name for an individual band for the date.\n",
    "    * see the cells in the section below on os and glob to help with this task. \n",
    "7. Add site name, date, and mean_ndvi values to a pandas dataframe.\n",
    "    * add them to a list and then convert that list to a pandas dataframe\n",
    "    * add them to individual lists and then create the pandas dataframe by converting each list into a column within the pandas dataframe.\n",
    "        * add values to list:\n",
    "        * `.append()`\n",
    "        * `list_name += [value]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "9c7cd3e2e5089092e06ba301f2719a63",
     "grade": false,
     "grade_id": "core-imports",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Autograding imports - do not modify this cell\n",
    "import matplotcheck.autograde as ag\n",
    "import matplotcheck.notebook as nb\n",
    "import matplotcheck.timeseries as ts\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "3c4d1141999885a9a9b09772962b180a",
     "grade": true,
     "grade_id": "student-imports-answer",
     "locked": false,
     "points": 10,
     "schema_version": 3,
     "solution": true,
     "task": false
    },
    "tags": [
     "hide",
     "hide_output"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your working directory is C:\\Users\\libby\\earth-analytics\\data\n"
     ]
    }
   ],
   "source": [
    "# Import needed packages in PEP 8 order\n",
    "import os\n",
    "from glob import glob\n",
    "\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "pd.options.mode.use_inf_as_na = True\n",
    "import geopandas as gpd\n",
    "from shapely.geometry import mapping\n",
    "import rasterio as rio\n",
    "import xarray as xr\n",
    "import rioxarray as rxr\n",
    "import earthpy as et\n",
    "import earthpy.spatial as es\n",
    "import earthpy.plot as ep\n",
    "import earthpy.mask as em\n",
    "from matplotlib.dates import DateFormatter\n",
    "\n",
    "# Set working directory to 'HOME/earth-analytics/data'\n",
    "earth_analytics_directory_path = os.path.join(\n",
    "    et.io.HOME, \"earth-analytics\", \"data\")\n",
    "\n",
    "os.chdir(earth_analytics_directory_path)\n",
    "\n",
    "print ('Your working directory is', earth_analytics_directory_path)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "deletable": false,
    "editable": false,
    "hideCode": false,
    "hidePrompt": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "dcf5b59326bf066172ff61520b658a3d",
     "grade": true,
     "grade_id": "student-download-tests",
     "locked": true,
     "points": 0,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Great - it looks like your working directory is set correctly to ~/earth-analytics/data\n"
     ]
    }
   ],
   "source": [
    "# DO NOT MODIFY THIS CELL\n",
    "# Tests that the working directory is set to earth-analytics/data\n",
    "\n",
    "path = os.path.normpath(os.getcwd())\n",
    "student_wd_parts = path.split(os.sep)\n",
    "\n",
    "if student_wd_parts[-2:] == ['earth-analytics', 'data']:\n",
    "    print(\"\\u2705 Great - it looks like your working directory is set correctly to ~/earth-analytics/data\")\n",
    "else:\n",
    "    print(\"\\u274C Oops, the autograder will not run unless your working directory is set to earth-analytics/data\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Use the cell below to download your data to your working directory\n",
    "\n",
    "\n",
    "* There should be a unique folder for each site you want to analyze\n",
    "    - The name of the each site's folder should be the name you want to label the site\n",
    "    \n",
    "    \n",
    "* Each site folder should contain two subfolders:\n",
    "    - ***vector***: contains a shape file of the site AOI\n",
    "    - ***landsat-crop***: contains subfolders with landsat8 files for each time slice from that site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\libby\\\\earth-analytics\\\\data\\\\ndvi-automation\\\\.\\\\sites'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Download datasets in this cell to your current working directory\n",
    "ndvi_data = et.data.get_data('ndvi-automation')\n",
    "ndvi_path = os.path.join(ndvi_data,'sites')\n",
    "ndvi_path"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "35205d12dc9e8fa05a26fb927c0a2307",
     "grade": false,
     "grade_id": "ndvi-mean-site-instructions",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# Figure 1: Plot 1 - Mean NDVI For Each Site Across the Year (50 points)\n",
    "\n",
    "Create a plot of the mean normalized difference vegetation index (NDVI) for the two different sites in the United States across the year: \n",
    "\n",
    "* NDVI on the x axis and formatted dates on the y for both NEON sites on one figure/axis object.\n",
    "* Each site should be identified with a different color in the plot and legend.\n",
    "* The final plot **data should be cleaned to remove the influence of clouds**.\n",
    "* Be sure to include appropriate title and axes labels.\n",
    "\n",
    "Add additional cells as needed for processing data (e.g. defining functions, etc), but be sure to:\n",
    "* follow the instructions in the code cells that have been provided to ensure that you are able to use the sanity check tests that are provided. \n",
    "* include only the plot code in the cell identified for the final plot code below"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "ce17d4d685cd4c7034bd7b0bb389342a",
     "grade": false,
     "grade_id": "single-scene-instructions",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "## Task 1: \n",
    "\n",
    "In the cell below, create a single dataframe containing MEAN NDVI, the site name, \n",
    "and the date of the data for the HARV site \n",
    "scene `HARV/landsat-crop/LC080130302017031701T1-SC20181023151837`.  The column names for the  final\n",
    "DataFrame should be`mean_ndvi`, and `site`, and the data should be **indexed on the date**. \n",
    "\n",
    "Use the functions that we reviewed in class (or create your own versions of them) to implement your code\n",
    "\n",
    "### In the Cell below Place  All Functions Needed to Run this Notebook (20 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "0ee340cd9af6c949a08eb4b325716ae0",
     "grade": false,
     "grade_id": "cell-618e3588853f3ed8",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "### DO NOT REMOVE THIS LINE OR EDIT / MOVE THIS CELL ###\n",
    "start_time = datetime.now()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "653ebd5db668245408615979f6c20944",
     "grade": true,
     "grade_id": "function-definitions-check",
     "locked": false,
     "points": 40,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "def calculate_mean_ndvi_clouds(folder_path):\n",
    "    '''\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    input_folder: string\n",
    "        this is a string to the file path containing all site folders you wish\n",
    "        to analyze\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    results: pandas dataframe\n",
    "        a date-time indexed dataframe with columns for \"mean_ndvi\" and \"site\"\n",
    "\n",
    "    '''\n",
    "    # Define paths to data\n",
    "    landsat_path = folder_path\n",
    "\n",
    "    # Get site name from folder title\n",
    "    path_components = landsat_path.split(os.sep)\n",
    "    sitename = path_components[8]\n",
    "\n",
    "    # Open site boundary shapefile\n",
    "    site_boundary_path = os.path.commonpath(\n",
    "        glob(os.path.join(ndvi_path, sitename, '*', '*.shp')))\n",
    "    site_boundary = gpd.read_file(site_boundary_path)\n",
    "\n",
    "    # Remove clouds\n",
    "    bands_path_pre = glob(os.path.join(landsat_path, \"*band[4-5]*.tif\"))\n",
    "    bands_path_pre.sort()\n",
    "    bands_pre_cloud = combine_tifs(bands_path_pre)\n",
    "    cloud_mask = mask_clouds(landsat_path)\n",
    "    bands_post_cloud = bands_pre_cloud.where(~cloud_mask)\n",
    "\n",
    "    # Open Landsat8 data bands 4 (red) & 5 (near infrared)\n",
    "    red_band = bands_post_cloud[0]\n",
    "    nir_band = bands_post_cloud[1]\n",
    "\n",
    "    # Crop Landsat Data (make sure projections match!)\n",
    "    red_band_clip = red_band.rio.clip(\n",
    "        site_boundary.geometry.apply(mapping), site_boundary.crs)\n",
    "    nir_band_clip = nir_band.rio.clip(\n",
    "        site_boundary.geometry.apply(mapping), site_boundary.crs)\n",
    "\n",
    "    # Calculate NDVI\n",
    "    top = (nir_band_clip-red_band_clip)\n",
    "    bottom = (nir_band_clip+red_band_clip)\n",
    "    site_ndvi = top/bottom\n",
    "\n",
    "    # Calculate mean NDVI\n",
    "    ndvi_mean = site_ndvi.mean()\n",
    "    if isinstance(ndvi_mean, float) == True:\n",
    "        next\n",
    "    else:\n",
    "        ndvi_mean = xr.DataArray.to_pandas(ndvi_mean)\n",
    "\n",
    "    # Find date and site name\n",
    "    slice_name = os.path.basename(os.path.normpath(landsat_path))\n",
    "    date_name = slice_name[10:18]\n",
    "\n",
    "    # Add values to Dataframe\n",
    "    temp_df = pd.DataFrame({\"site\": [sitename],\n",
    "                            \"mean_ndvi\": [ndvi_mean],\n",
    "                            \"date\": [date_name]})\n",
    "\n",
    "    temp_df['date'] = pd.to_datetime(temp_df['date'])\n",
    "    temp_df = temp_df.set_index('date')\n",
    "\n",
    "    return temp_df\n",
    "\n",
    "\n",
    "\n",
    "def combine_tifs(tif_list):\n",
    "    \"\"\"A function that combines a list of tifs in the same CRS\n",
    "    and of the same extent into an xarray object\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    tif_list : list\n",
    "        A list of paths to the tif files that you wish to combine.\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    An xarray object with all of the tif files in the listmerged into \n",
    "    a single object.\n",
    "\n",
    "    \"\"\"\n",
    "\n",
    "    out_xr = []\n",
    "    for i, tif_path in enumerate(tif_list):\n",
    "        out_xr.append(rxr.open_rasterio(tif_path, masked=True).squeeze())\n",
    "        out_xr[i][\"band\"] = i+1\n",
    "\n",
    "    return xr.concat(out_xr, dim=\"band\")\n",
    "\n",
    "\n",
    "def mask_clouds(input_path):\n",
    "    \"\"\"\n",
    "    This function uses the landsat qa.tif to mask areas on the image that are\n",
    "    likely clouds, cloud shadows, or shadows.\n",
    "    \n",
    "    Parameter\n",
    "    ---------\n",
    "    input_path: an os-formatted path\n",
    "        Path to a folder that includes a qa.tif landsat file\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    cloud mask: list\n",
    "        A list of masked values. This list  can then be used to masked stacked\n",
    "        landsat tifs of the same dimensions of the qa file using the function:\n",
    "        `stacked_tifs_masks = stacked_tifs.where(~cloud_mask)`\n",
    "\n",
    "    \"\"\"\n",
    "    # Mask Clouds\n",
    "    sample = os.path.commonpath(glob(os.path.join(input_path, \"*qa*.tif\")))\n",
    "    landsat_qa = rxr.open_rasterio(sample).squeeze()\n",
    "    high_cloud_confidence = em.pixel_flags[\"pixel_qa\"][\"L8\"][\"High Cloud Confidence\"]\n",
    "    cloud = em.pixel_flags[\"pixel_qa\"][\"L8\"][\"Cloud\"]\n",
    "    cloud_shadow = em.pixel_flags[\"pixel_qa\"][\"L8\"][\"Cloud Shadow\"]\n",
    "    all_masked_values = cloud_shadow + cloud + high_cloud_confidence\n",
    "\n",
    "    cloud_mask = landsat_qa.isin(all_masked_values)\n",
    "    \n",
    "    return cloud_mask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "d124eef1d9cf2d0063ab450c9a20dc8e",
     "grade": false,
     "grade_id": "single-scene-answer",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    },
    "tags": [
     "hide"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>site</th>\n",
       "      <th>mean_ndvi</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-03-17</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.2821579051696485</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            site           mean_ndvi\n",
       "date                                \n",
       "2017-03-17  HARV  0.2821579051696485"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Define paths to data\n",
    "landsat_path = os.path.join(ndvi_path,\n",
    "    'HARV', 'landsat-crop', 'LC080130302017031701T1-SC20181023151837')\n",
    "\n",
    "temp_df = calculate_mean_ndvi_clouds(landsat_path)\n",
    "temp_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "6121e3a0293ed64f09521b5d248496c3",
     "grade": true,
     "grade_id": "single-scene-tests",
     "locked": true,
     "points": 15,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Your data is stored in a DataFrame!\n",
      "✅ You have the index set to the date column!\n",
      "✅ The data in your date column is datetime!\n",
      "✅ You have the correct site name!\n",
      "❌ You do not have the correct mean ndvi value.\n",
      "\n",
      " ➡ You received 10 out of 15 points for creating a dataframe.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# This cell  is testing your data output above\n",
    "\n",
    "student_ndvi_ts_single_site = _\n",
    "\n",
    "single_scene_points = 0\n",
    "\n",
    "# Ensure the data is stored in a dataframe.\n",
    "if isinstance(student_ndvi_ts_single_site, pd.DataFrame):\n",
    "    print('\\u2705 Your data is stored in a DataFrame!')\n",
    "    single_scene_points += 1\n",
    "else:\n",
    "    print('\\u274C It appears your data is not stored in a DataFrame. ',\n",
    "          'To see what type of object your data is stored in, check its type with type(object)')\n",
    "\n",
    "# Ensure that the date column is the index\n",
    "if isinstance(student_ndvi_ts_single_site.index, pd.core.indexes.datetimes.DatetimeIndex):\n",
    "    print('\\u2705 You have the index set to the date column!')\n",
    "    single_scene_points += 2\n",
    "else:\n",
    "    print('\\u274C You do not have the index set to the date column.')\n",
    "\n",
    "# Ensure that the date column is datetime\n",
    "if isinstance(student_ndvi_ts_single_site.index[0], pd._libs.tslibs.timestamps.Timestamp):\n",
    "    print('\\u2705 The data in your date column is datetime!')\n",
    "    single_scene_points += 2\n",
    "else:\n",
    "    print('\\u274C The data in your date column is not datetime.')\n",
    "\n",
    "# Ensure the site name is correct\n",
    "if student_ndvi_ts_single_site.site.values[0] == 'HARV':\n",
    "    print('\\u2705 You have the correct site name!')\n",
    "    single_scene_points += 5\n",
    "else:\n",
    "    print('\\u274C You do not have the correct site name.')\n",
    "\n",
    "if np.allclose(0.281131628228094, student_ndvi_ts_single_site.mean_ndvi.values[0]):\n",
    "    print('\\u2705 You have the correct mean NDVI value!')\n",
    "    single_scene_points += 5\n",
    "else:\n",
    "    print('\\u274C You do not have the correct mean ndvi value.')\n",
    "\n",
    "print(\"\\n \\u27A1 You received {} out of 15 points for creating a dataframe.\".format(\n",
    "    single_scene_points))\n",
    "single_scene_points"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Task 2:\n",
    "\n",
    "In the cell below, process all of the landsat scenes. Create a DataFrame that contains the following \n",
    "information for each scene\n",
    "\n",
    "\n",
    "|   | index  | site  | mean_ndvi  | \n",
    "|---|---|---|---|\n",
    "| Date  |   |   |   |\n",
    "|  2017-01-07  | 0  | SJER  | .4  |  \n",
    "\n",
    "Be sure to call your dataframe at the end of the cell to ensure autograding works.\n",
    "HINT: FOR THIS STEP, leave any rows containing missing values (`NAN`)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "848dd486333246e15b6b8f0dff745a4b",
     "grade": false,
     "grade_id": "cleaned_dataframes_answer",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    },
    "scrolled": false,
    "tags": [
     "hide"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>site</th>\n",
       "      <th>mean_ndvi</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017-01-12</th>\n",
       "      <td>HARV</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-28</th>\n",
       "      <td>HARV</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-02-13</th>\n",
       "      <td>HARV</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-03-01</th>\n",
       "      <td>HARV</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-03-17</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.2821579051696485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-04-02</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.2512478931112462</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-04-18</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.5410801238000957</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-04</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.5689237374289202</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-20</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.8113103647212354</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-06-05</th>\n",
       "      <td>HARV</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-06-21</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.882129129215848</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-07-07</th>\n",
       "      <td>HARV</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-07-23</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.8197676274401585</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-08-08</th>\n",
       "      <td>HARV</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-08-24</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.8644636913732269</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-09-09</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.8579065920436171</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-09-25</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.8406390348962894</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-10-11</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.6524352989898703</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-10-27</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.6883822168605687</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-12</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.6133210869444865</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-28</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.6179475536564982</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-12-14</th>\n",
       "      <td>HARV</td>\n",
       "      <td>0.5221778902330447</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-12-30</th>\n",
       "      <td>HARV</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-07</th>\n",
       "      <td>SJER</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-01-23</th>\n",
       "      <td>SJER</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-02-08</th>\n",
       "      <td>SJER</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-02-24</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.6634320200679064</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-03-12</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.6641088612677682</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-03-28</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.7028516749424963</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-04-13</th>\n",
       "      <td>SJER</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-04-29</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.6102087366686794</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-15</th>\n",
       "      <td>SJER</td>\n",
       "      <td>inf</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-05-31</th>\n",
       "      <td>SJER</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-06-16</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.3585510407181815</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-07-02</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.3345591761068122</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-07-18</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.3197955314428465</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-08-03</th>\n",
       "      <td>SJER</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-08-19</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.3274550105686022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-09-04</th>\n",
       "      <td>SJER</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-09-20</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.33091990897508644</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-10-06</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.3053313262263613</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-10-22</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.3170060052971081</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-07</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.3134937348789093</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-11-23</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.32465042087640067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-12-09</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.3520404606444396</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2017-12-25</th>\n",
       "      <td>SJER</td>\n",
       "      <td>0.27173781907807704</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            site            mean_ndvi\n",
       "date                                 \n",
       "2017-01-12  HARV                  nan\n",
       "2017-01-28  HARV                  nan\n",
       "2017-02-13  HARV                  nan\n",
       "2017-03-01  HARV                  nan\n",
       "2017-03-17  HARV   0.2821579051696485\n",
       "2017-04-02  HARV   0.2512478931112462\n",
       "2017-04-18  HARV   0.5410801238000957\n",
       "2017-05-04  HARV   0.5689237374289202\n",
       "2017-05-20  HARV   0.8113103647212354\n",
       "2017-06-05  HARV                  nan\n",
       "2017-06-21  HARV    0.882129129215848\n",
       "2017-07-07  HARV                  nan\n",
       "2017-07-23  HARV   0.8197676274401585\n",
       "2017-08-08  HARV                  nan\n",
       "2017-08-24  HARV   0.8644636913732269\n",
       "2017-09-09  HARV   0.8579065920436171\n",
       "2017-09-25  HARV   0.8406390348962894\n",
       "2017-10-11  HARV   0.6524352989898703\n",
       "2017-10-27  HARV   0.6883822168605687\n",
       "2017-11-12  HARV   0.6133210869444865\n",
       "2017-11-28  HARV   0.6179475536564982\n",
       "2017-12-14  HARV   0.5221778902330447\n",
       "2017-12-30  HARV                  nan\n",
       "2017-01-07  SJER                  nan\n",
       "2017-01-23  SJER                  nan\n",
       "2017-02-08  SJER                  nan\n",
       "2017-02-24  SJER   0.6634320200679064\n",
       "2017-03-12  SJER   0.6641088612677682\n",
       "2017-03-28  SJER   0.7028516749424963\n",
       "2017-04-13  SJER                  nan\n",
       "2017-04-29  SJER   0.6102087366686794\n",
       "2017-05-15  SJER                  inf\n",
       "2017-05-31  SJER                  nan\n",
       "2017-06-16  SJER   0.3585510407181815\n",
       "2017-07-02  SJER   0.3345591761068122\n",
       "2017-07-18  SJER   0.3197955314428465\n",
       "2017-08-03  SJER                  nan\n",
       "2017-08-19  SJER   0.3274550105686022\n",
       "2017-09-04  SJER                  nan\n",
       "2017-09-20  SJER  0.33091990897508644\n",
       "2017-10-06  SJER   0.3053313262263613\n",
       "2017-10-22  SJER   0.3170060052971081\n",
       "2017-11-07  SJER   0.3134937348789093\n",
       "2017-11-23  SJER  0.32465042087640067\n",
       "2017-12-09  SJER   0.3520404606444396\n",
       "2017-12-25  SJER  0.27173781907807704"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create dataframe of NDVI including the cleaning data to deal with clouds\n",
    "\n",
    "# Test Cell\n",
    "sites = glob(ndvi_path + '/*/')\n",
    "results = pd.DataFrame()\n",
    "\n",
    "for site in sites:\n",
    "    ls_data_list = glob(site + 'landsat-crop'+'/*/')\n",
    "\n",
    "    for folder in ls_data_list:\n",
    "        temp_df = calculate_mean_ndvi_clouds(folder)\n",
    "        results = results.append(temp_df)\n",
    "\n",
    "results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "1ce5d7d7519d5e569e6cf7c5927c6ffb",
     "grade": true,
     "grade_id": "cleaned_dataframes_test",
     "locked": true,
     "points": 10,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Your data is stored in a DataFrame!\n",
      "❌ The amount of null data in your dataframe is incorrect.\n",
      "✅ You have the index set to the date column!\n",
      "✅ The data in your date column is datetime!\n",
      "Your total run time for processing the data was 0:00:50.651716.\n",
      "\n",
      " ➡ You received 8 out of 10 points for creating a dataframe.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Last sanity check before creating your plot (10 points)\n",
    "\n",
    "# Ensure that you call your dataframe at the bottom of the cell above\n",
    "# and that it has columns called: mean_ndvi and site\n",
    "\n",
    "# Ensure the data is stored in a dataframe.\n",
    "student_ndvi_df = _\n",
    "\n",
    "df_points = 0\n",
    "\n",
    "if isinstance(student_ndvi_df, pd.DataFrame):\n",
    "    print('\\u2705 Your data is stored in a DataFrame!')\n",
    "    df_points += 2\n",
    "else:\n",
    "    print('\\u274C It appears your data is not stored in a DataFrame. ',\n",
    "          'To see what type of object your data is stored in, check its type with type(object)')\n",
    "\n",
    "# Check that dataframe contains the appropriate number of NAN values\n",
    "if student_ndvi_df.mean_ndvi.isna().sum() == 15:\n",
    "    print('\\u2705 Correct number of masked data values!')\n",
    "    df_points += 2\n",
    "else:\n",
    "    print('\\u274C The amount of null data in your dataframe is incorrect.')\n",
    "\n",
    "\n",
    "# Ensure that the date column is the index\n",
    "if isinstance(student_ndvi_df.index, pd.core.indexes.datetimes.DatetimeIndex):\n",
    "    print('\\u2705 You have the index set to the date column!')\n",
    "    df_points += 3\n",
    "else:\n",
    "    print('\\u274C You do not have the index set to the date column.')\n",
    "\n",
    "# Ensure that the date column is datetime\n",
    "if isinstance(student_ndvi_df.index[0], pd._libs.tslibs.timestamps.Timestamp):\n",
    "    print('\\u2705 The data in your date column is datetime!')\n",
    "    df_points += 3\n",
    "else:\n",
    "    print('\\u274C The data in your date column is not datetime.')\n",
    "\n",
    "# Output for timer, # DO NOT MODIFY\n",
    "end_time = datetime.now()\n",
    "total_time = end_time - start_time\n",
    "print(\n",
    "    \"Your total run time for processing the data was {0}.\".format(total_time))\n",
    "\n",
    "print(\"\\n \\u27A1 You received {} out of 10 points for creating a dataframe.\".format(\n",
    "    df_points))\n",
    "\n",
    "df_points"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "caption": "Plot showing NDVI for each time period at both NEON Sites. In this example the cloudy pixels were removed using the pixel_qa cloud mask. Notice that this makes a significant different in the output values. Why do you think this difference is so significant?",
    "deletable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "f9d5ebf0557e366fa6f1727fd85a7e45",
     "grade": false,
     "grade_id": "plot_cleaned_dataframes_answer",
     "locked": false,
     "schema_version": 3,
     "solution": true,
     "task": false
    },
    "tags": [
     "hide"
    ]
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-11-c449129f7bac>:29: UserWarning: FixedFormatter should only be used together with FixedLocator\n",
      "  ax.set_xticklabels(month_names)\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot Cloud-corrected mean NDVI by month\n",
    "\n",
    "# Drop Nans\n",
    "results_noNan = results.dropna(axis=0, how='any')\n",
    "\n",
    "month_names = ['Jan', 'Feb', 'March', 'April', 'May',\n",
    "               'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']\n",
    "sites = results.site.unique()\n",
    "fig, ax = plt.subplots(figsize=(15, 10))\n",
    "ax.set_title(\n",
    "    'Mean Normalized Different Vegetation Index (NDVI)\\nJan 2017 - Dec 2017\\nLandsat8 with Clouds Removed')\n",
    "\n",
    "for site in sites:\n",
    "    temp_df = results[results[\"site\"] == site]\n",
    "    ax.plot(temp_df.index.values,\n",
    "            temp_df['mean_ndvi'],\n",
    "            'o-',\n",
    "            label=site)\n",
    "\n",
    "# Format Y-axis\n",
    "ax.set_ylabel('Mean NDVI')\n",
    "ax.set_ylim(0.2, 0.9)\n",
    "\n",
    "# Format X-axis\n",
    "date_form = DateFormatter('%m')\n",
    "ax.xaxis.set_major_formatter(date_form)\n",
    "ax.set_xlabel('Month')\n",
    "ax.set_xlim('2017-01', '2017-12-31')\n",
    "ax.set_xticklabels(month_names)\n",
    "\n",
    "# Plot Legend\n",
    "plt.legend()\n",
    "\n",
    "\n",
    "### DO NOT REMOVE LINES BELOW ###\n",
    "final_masked_solution = nb.convert_axes(plt, which_axes=\"current\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "d2bc7d91b553a74e6382776fface9c70",
     "grade": true,
     "grade_id": "plot_cleaned_dataframes_test_answers",
     "locked": true,
     "points": 0,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Ignore this cell for the autograding tests\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "code",
     "checksum": "23a1c68916e304be754ea15d9495e781",
     "grade": true,
     "grade_id": "plot_cleaned_dataframes_tests",
     "locked": true,
     "points": 50,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "outputs": [],
   "source": [
    "# Ignore this cell for the autograding tests\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "c660ce8da16752276c4b16e35c7d2726",
     "grade": false,
     "grade_id": "question-1",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# Question 1 (10 points)\n",
    "\n",
    "Imagine that you are planning NEON’s upcoming flight season to capture remote sensing data in these locations and want to ensure that you fly the area when the vegetation is the most green.\n",
    "\n",
    "When would you recommend the flights take place for each site? \n",
    "\n",
    "Answer the question in 2-3 sentences in the Markdown cell below."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "26a85257b913135d401b6dc4fd2a4fc3",
     "grade": true,
     "grade_id": "question-1-answer",
     "locked": false,
     "points": 10,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "source": [
    "The flights for the SJER site should take place sometime in th early spring (late March - early April) in order to capture the maximum green vegetation. For the HARV site, the flights could take place any time during the summer (Memorial day - Labor day)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "603922a2076d0940962432ebc5069ef9",
     "grade": false,
     "grade_id": "question-2",
     "locked": true,
     "schema_version": 3,
     "solution": false,
     "task": false
    }
   },
   "source": [
    "# Question 2 (10 points)\n",
    "\n",
    "How could you modify your workflow to look at vegetation changes over time in each site? \n",
    "\n",
    "Answer the question in 2-3 sentences in the Markdown cell below."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "f4ae5b1f3a47c9bf44714a2de486da54",
     "grade": true,
     "grade_id": "question-2-answer",
     "locked": false,
     "points": 10,
     "schema_version": 3,
     "solution": true,
     "task": false
    }
   },
   "source": [
    "If you wanted to look at these changes from year to year, the workflow could be mostlt kept the same for the import of the landsat data and calculation of the mean NDVI, but how data is subsetted for the plotting of data would have to change. One could also add a date range when importing landsat data (for emaple, if you only wanted to see images from 15-March to 30-April for any given year)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "df53001e9821bf3baef478a3b29bde33",
     "grade": false,
     "grade_id": "additional-markdown-cell-check",
     "locked": true,
     "points": 10,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "# Do not edit this cell! (10 points)\n",
    "\n",
    "The notebook includes:\n",
    "* additional Markdown cells throughout the notebook to describe: \n",
    "    * the data that you used - and where it is from\n",
    "    * how data are being processing\n",
    "    * how the code is optimized to run fast and be more concise"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "bcc0e446306a9db445d1ab243227c563",
     "grade": false,
     "grade_id": "pep8-formatting-check",
     "locked": true,
     "points": 30,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "# Do not edit this cell! (20 points)\n",
    "\n",
    "The notebook will also be checked for overall clean code requirements as specified at the **top** of this notebook. Some of these requirements include (review the top cells for more specifics): \n",
    "\n",
    "* Notebook begins at cell [1] and runs on any machine in its entirety.\n",
    "* PEP 8 format is applied throughout (including lengths of comment and code lines).\n",
    "* No additional code or imports in the notebook that is not needed for the workflow.\n",
    "* Notebook is fully reproducible. This means:\n",
    "   * reproducible paths using the os module.\n",
    "   * data downloaded using code in the notebook.\n",
    "   * all imports at top of notebook."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "editable": false,
    "nbgrader": {
     "cell_type": "markdown",
     "checksum": "67969627ed2d8a81a168d0ed1831224d",
     "grade": false,
     "grade_id": "cell-bf1766fe2443b94a",
     "locked": true,
     "points": 0,
     "schema_version": 3,
     "solution": false,
     "task": true
    }
   },
   "source": [
    "## BONUS - Export a  .CSV File to Share (10 points possible)\n",
    "\n",
    "This is optional - if you export a **.csv** file with the columns specified above: Site, Date and NDVI Value you can get an additional 10 points.\n",
    "\n",
    "* FULL CREDIT: File exists in csv format and contains the columns specified.\n",
    "We will check your github repo for this file!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Export CSV file\n",
    "# Create an output path for file\n",
    "output_csv = os.path.join('H:', 'earth-analytics', 'earth-analytics-python',\n",
    "                          'ea-2021-04-ndvi-automation-lrwives', 'final.csv')\n",
    "results.to_csv(output_csv)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.6"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": true
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}