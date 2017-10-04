import logging

import pytest
from sn_agent.log import setup_logging
from sn_agent import ontology
from sn_agent.ontology.service_descriptor import ServiceDescriptor
from sn_agent.job.job_descriptor import JobDescriptor
from sn_agent.job.job_descriptor import init_test_jobs

log = logging.getLogger(__name__)



# Tests

# Test performance of services - all of them
def test_jobs():
    print()
    setup_logging()
    init_test_jobs()
    test_jobs = JobDescriptor.get_test_jobs(ontology.DOCUMENT_SUMMARIZER_ID)
    for job in test_jobs:
        service_id = 0
        if str(job) != "NO_JOB":
            service_id = ontology.DOCUMENT_SUMMARIZER_ID

        job_parameters = {'input_type': 'file',
                          'input_url': 'http://test.com/inputs/test_input.txt',
                          'output_type': 'file_url_put',
                          'output_url': 'test_output.txt'}
        service_id = ontology.DOCUMENT_SUMMARIZER_ID
        new_job = JobDescriptor(ServiceDescriptor(service_id), job_parameters)
        test_jobs.append(new_job)
        total_jobs = len(test_jobs)
        del test_jobs[total_jobs-1]
