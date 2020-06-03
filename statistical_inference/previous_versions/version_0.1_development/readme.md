# Statinfer

## Definiticon
Estimation of statistical parameters is the process of using sample data to estimate the values of unknown population parameters. Essentially, any
characteristic of a population can be estimated from a random sample.
Among the most common estimators are the sample mean, the sample standard deviation and the sample proportion as estimators of the population average, the population standard deviation and the population proportion, respectively.

## Object Instatiation
object_name = Statinfer(sm = sample_mean,
						 ss = sample_size,
						 tl = trust_level,
						 psd = population_standard_deviation)

## Base attributes

### stdkme
#### object_name.stdkme
Returns the value for the margin of error for known population standard deviation

### iestdk
#### object_name.iestdk
Returns the interval estimate for the sample mean with a known population standard deviation

## Base function

### describe
#### object_name.describe()
Returns the summary of everything

## Updates
developmet...