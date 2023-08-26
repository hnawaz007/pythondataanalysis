from dagster import file_relative_path
from dagstermill import define_dagstermill_asset

#

# Asset backed by a Jupyter notebook
analysis_jupyter_notebook = define_dagstermill_asset(
    name="analysis_jupyter_notebook",
    notebook_path=file_relative_path(__file__, "/notebooks/SQL Data Analysis.ipynb"),
    group_name="Notebooks",
    io_manager_key="output_notebook_io_manager"
)
