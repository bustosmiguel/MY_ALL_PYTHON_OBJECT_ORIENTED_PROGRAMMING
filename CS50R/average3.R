# Message about returning NA

average <- function(x) {
  if (!is.numeric(x)) {
    message("`x` must be a numeric vector. Returning NA instead.")
    return(NA)
  }
  sum(x) / length(x)
}
