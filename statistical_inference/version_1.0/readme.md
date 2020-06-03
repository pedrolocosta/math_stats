# Statinfer

## Definiticon
Estimation of statistical parameters is the process of using sample data to estimate the values of unknown population parameters. Essentially, any
characteristic of a population can be estimated from a random sample.
Among the most common estimators are the sample mean, the sample standard deviation and the sample proportion as estimators of the population average, the population standard deviation and the population proportion, respectively.

## if population standard deviation is known:
### Object Instatiation
object_name = Statinfer(sm = sample_mean,
						 ss = sample_size,
						 tl = trust_level,
						 psd = population_standard_deviation)

### Base attributes

#### stdkme
##### object_name.stdkme
Returns the value for the margin of error for known population standard deviation

#### stdkie
##### object_name.stdkie
Returns the interval estimate for the sample mean with a known population standard deviation

### Base function

#### describe
##### object_name.describe()
Returns the summary of everything

## if population standard deviation is not known:
### Object Instatiation
object_name = Statinfer(sm = sample_mean,
						 ss = sample_size,
						 tl = trust_level,
						 psd = population_standard_deviation = 0,
						 ssd = sample_standard_deviation)

### Base attributes

#### stdnkme
##### object_name.stdnkme
Returns the value for the margin of error for not known population standard deviation

#### stdnkie
##### object_name.stdnkie
Returns the interval estimate for the sample mean with a not known population standard deviation

### Base function

#### describe
##### object_name.describe()
Returns the summary of everything


## Updates
initial version