import datetime as dt

class Std:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property    
    def n(self):
        return len(self.x)
    
    @property    
    def x_avg(self):
        return sum(self.x)/self.n

    @property    
    def y_avg(self):
        return sum(self.y)/self.n
    
    @property
    def sigmaXY(self):
        return sum((xi * yi for xi, yi in zip(self.x, self.y)))
    
    @property
    def sigmaXsq(self):
        return sum((xi**2 for xi in self.x))

    @property
    def sigmaYsq(self):
        return sum((yi**2 for yi in self.y))

    @property    
    def x_variance(self):
        de = sum([(xi - self.x_avg)**2 for xi in self.x])
        return de/self.n
    
    @property    
    def x_quasi_variance(self):
        de = sum([(xi - self.x_avg)**2 for xi in self.x])
        return de/(self.n - 1)

    @property    
    def y_variance(self):
        de = sum([(yi - self.y_avg)**2 for yi in self.y])
        return de/self.n


    @property    
    def y_quasi_variance(self):
        de = sum([(yi - self.y_avg)**2 for yi in self.y])
        return de/(self.n - 1)     
    

    @property
    def covariance(self):
        first_term = self.sigmaXY/self.n
        return first_term - self.x_avg * self.y_avg
    
    @property
    def r(self):
        de = self.covariance
        nu = ((self.x_variance) ** 0.5) * ((self.y_variance) ** 0.5)
        return de/nu

    @property
    def B(self):
        de = self.n*self.sigmaXY - sum(self.x)*sum(self.y)
        nu = self.n*self.sigmaXsq - sum(self.x)**2
        return de/nu
    
    @property
    def B0(self):
        return self.y_avg - self.B*self.x_avg
    
    def y_prediction(self, xi):
        return self.B * xi + self.B0

    @property
    def lineals(self):
        return tuple(self.y_prediction(week) for week in self.x)
    
    def get_prediction_day(self, last_date, prediction_date):
        delta = dt.date.fromisoformat(prediction_date) - dt.date.fromisoformat(last_date)
        days_on_weeks = delta.days / 7
        delta = self.n + days_on_weeks
        return self.y_prediction(delta)  

    def __str__(self):
        return f"x: {self.x }\ny: {self.y }\nn: {self.n}\n"

