from dagster import ConfigurableResource 

import dlt

class DltResource(ConfigurableResource):
    pipeline_name: str
    dataset_name: str
    destination: str

    def create_pipeline(self, resource_data, table_name):

        # configure the pipeline with your destination details
        pipeline = dlt.pipeline(
        pipeline_name=self.pipeline_name, destination=self.destination, dataset_name=self.dataset_name
        )

        # run the pipeline with your parameters
        load_info = pipeline.run(resource_data, table_name=table_name)

        return load_info