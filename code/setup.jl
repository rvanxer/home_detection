using Dates
using YAML

include("utils.jl")

struct Region
    """ A simple class for handling study regions (mostly MSAs). """
    key::String
    name::String
    state::String
    geocode::String
    counties::Array{String}
    root::String
    datasets::Set{Any}

    function Region(key::String, root = "$ROOT/regions")
        x = YAML.load_file("$root/$key/info.yaml")
        Region(x["name"], x["state"], x["counties"])
    end
    
    function Region(name, state, counties, geocode = nothing, 
            root = "$ROOT/regions")
        key = lowercase(replace(name, " " => "_"))
        geocode = geocode == nothing ? "$name, $state" : geocode
        root = "$root/$key"
        info = Dict(:name => name, :state => state, :counties => counties)
        YAML.write_file(mkfile("$root/info.yaml"), info)
        new(key, name, state, geocode, counties, root)
    end
end

Base.show(io::IO, r::Region) = print(io, "Region($(r.geocode))")

struct Dataset
    """ A container of a combination of region and analysis period. """
    key::String
    region::Region
    startDate::Union{String, Date}
    endDate::Union{String, Date}
    dates::StepRange{Date, Day}
    root::String

    function Dataset(key::String, root = "$ROOT/datasets")
        x = YAML.load_file("$root/$key/info.yaml")
        Dataset(key, x["region"], x["startDate"], x["endDate"])
    end
    
    function Dataset(key, region::Union{String, Region}, 
            startDate::Union{String, Date}, endDate::Union{String, Date},
            root = "$ROOT/datasets")
        startDate = toDate(startDate)
        endDate = toDate(endDate)
        dates = startDate: Day(1): endDate
        root = "$root/$key"
        region = typeof(region) == String ? Region(region) : region
        info = Dict(:region => region.key, :startDate => toStr(startDate), 
            :endDate => toStr(endDate))
        YAML.write_file(mkfile("$root/info.yaml"), info)
        new(key, region, startDate, endDate, dates, root)
    end
end

Base.show(io::IO, ds::Dataset) = print(io, "Dataset($(ds.key))")
