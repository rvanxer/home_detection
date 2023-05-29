using Dates

const global MK = "/home/umni2/a/umnilab/users/verma99/mk"
const global ROOT = "$MK/home_detection/julia"

# Unit conversion factors
const global M2FT = 3.28084 # meter to feet
const global FT2M = 1 / 3.28084 # feet to meter
const global MI2M = 1609.34  # mile to meter
const global M2MI = 1 / 1609.34  # meter to mile
const global MI2KM = 1.60934  # mile to kilometer
const global KM2MI = 1 / 1.60934  # kilometer to mile
const global SQMI2SQM = 2.58998811e6  # sq. mile to sq. meter
const global SQM2SQMI = 1 / 2.58998811e6  # sq. meter to sq. mile

toDate(x::Date) = x

"Convert a string to date"
toDate(x::String, fmt = "y-m-d") = Date(x, DateFormat(fmt))

"Convert a date to string"
toStr(x::Date, fmt = "yyyy-mm-dd") = Dates.format(x, fmt)

"Normalize an array of values to fit in the range [0, 1]"
function normalize(x::Vector, vmin = nothing, vmax = nothing)
    vmin = vmin == nothing ? minimum(x) : vmin
    vmax = vmax == nothing ? maximum(x) : vmax
    (x .- vmin) ./ (vmax - vmin)
end

"Create parent directory of file"
mkfile(path::AbstractString) = joinpath(mkpath(dirname(path)), basename(path))
# mkfile = lambda path: Path(path).mkdir(parents=True, recurse=True) / Path(path).name

