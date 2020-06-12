# Size_sample

## Definiticon
Estimation of statistical parameters is the process of using sample data to estimate the values of unknown population parameters. Essentially, any
characteristic of a population can be estimated from a random sample.
Among the most common estimators are the sample mean, the sample standard deviation and the sample proportion as estimators of the population average, the population standard deviation and the population proportion, respectively.

## if population size is known:
### Object Instatiation
object_name = Size_sample(tl = trust_level,
						 me = margin of error,
						 sp = sample_proportion = 50,
						 ps = polulation size)

### Base attributes

#### ss
##### object_name.ss
Returns the value of the sample size

### Base function

#### describe
##### object_name.describe()
Returns the summary of everything

## if population size is not known:
### Object Instatiation
object_name = Size_sample(tl = trust_level,
						 me = margin of error,
						 sp = sample_proportion = 50,
						 ps = polulation size = 0)

#### Base attributes

#### ss
##### object_name.ss
Returns the value of the sample size

### Base function

#### describe
##### object_name.describe()
Returns the summary of everything


## Updates
initial version