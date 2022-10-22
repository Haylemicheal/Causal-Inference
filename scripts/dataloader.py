#!/usr/bin/env python3
import logging as log
import pandas as pd
import sys, os, io
import dvc.api
sys.path.append(os.path.abspath(os.path.join('..')))

log.basicConfig(filename='../logs/log.txt', format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')


class DataLoader:
    """A class for data loading
    """
    def __init__(self):
        log.info("The data loader instance is created")
    
    def read_csv(self, path):
        """Read csv file
           Args:
                path: location of the csv file
           Return:
                df: pandas dataframe
        """
        df = pd.read_csv(path, sep=",", low_memory=False)
        log.info("Read the file: "+ str(path))
        return df

    def load_from_dvc(self, path, repo, tag):
        """
        Load the data from dvc
        Args:
            path: Path of the data
            repo: Github repo link
            tag: git tag of the data
        Return:
            content: dvc content of the data
        """
        content = dvc.api.read(path=path, repo=repo, rev=tag)
        log.info("Read the dvc data from "+ repo + " "+ tag)
        return content

