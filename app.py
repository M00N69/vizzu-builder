from __future__ import annotations
import streamlit as st

from src.data.loader import CsvFileUploader
from src.data.filter import filter_dataframe
from src.chart import ChartBuilder

if "filters" not in st.session_state:
    st.session_state["filters"] = None


class App:
    def __init__(self):
        self._df = None
        self._file_name = None
        self._filters = None
        st.set_page_config(page_title="Vizzu Chart Builder", page_icon="🏗️")
        self._add_title()
        self._init_csv_file_loader()
        self._init_builders()

    def _add_title(self):
        st.title("🏗️ Vizzu Chart Builder")

    def _init_csv_file_loader(self):
        csv_file_uploader = CsvFileUploader()
        self._df = csv_file_uploader.df
        self._file_name = csv_file_uploader.file_name
        if self._df is not None:
            filter_dataframe(self._df)

    def _init_builders(self):
        ChartBuilder(self._file_name, self._df, st.session_state["filters"])


App()
