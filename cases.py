class Case:
    def _init_(self,FIPS,Admin2,Province_State,Country_Region,Last_Update,Lat,Long_,Confirmed,Deaths,Recovered,Active,Combined_Key,Incident_Rate,Case_Fatality_Ratio):
        self.FIPS = FIPS
        self.Admin2 = Admin2
        self.Province = Province_State
        self.Country_Region = Country_Region
        self.Last_Update = Last_Update
        self.Lat = Lat
        self.Long_ = Long_
        self.Confirmed = Confirmed
        self.Deaths = Deaths
        self.Recovered = Recovered
        self.Active = Active
        self.Combined_Key = Combined_Key
        self.Incident_Reate = Incident_Rate
        self.Case_Fatality_Ratio = Case_Fatality_Ratio

