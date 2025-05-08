from Data.repository import Repo
import pandas as pd

class SalesService:
    def __init__(self):
        self.repo = Repo()
    
    def prodaja_po_produktnih_linijah(self) -> pd.DataFrame:
        """
        Vrne podatke o prodaji po produktnih linijah.
        """
        df = self.repo.prodaja_po_produktnih_linijah()
        return df