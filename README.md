# Comparison of Home Detection Algorithms using Smartphone GPS Data
**[Rajat Verma](https://github.com/rvanxer), Shagun Mittal, [Zengxiang Lei](https://github.com/tjleizeng), Xiaowei Chen, [Satish Ukkusuri](https://github.com/umnilab)**

## Abstract
Estimation of people's home locations using large-scale location-based services data from smartphones is a common task in many applications in human mobility assessment. However, commonly used home location algorithms (HDAs) are often arbitrary and unexamined.
In this study, we review existing HDAs and examine five (four prominent and one by ourselves) HDAs using eight high-quality mobile phone geolocation datasets. 
Among these HDAs, four of them are used by influential studies, and one is proposed in this work which involves the consideration of temporal continuity. 
To make quantitative comparisons, we propose three novel metrics to assess the quality of detected homes by different HDAs. 
We find that all three metrics show a consistent rank of HDAs' performances among all datasets, which suggests that the temporal and spatial continuity of the geolocation data points matters more than the overall number of points, and our proposed HDA that utilizes this outperforms the other HDAs.
We further show that these metrics decrease with decreasing data quality yet the patterns of relative performance persist.
Finally, we show how the differences in the homes detected from these HDAs can lead to substantial differences in subsequent inferences using two case studies. It is also found that HDAs with high (and similar) performance metrics tend to create results with better consistency and closer to common expectations.
Our results will help promote transparency and reliability in human mobility assessment.

## Framework
<img src="fig/Overall%20framework%20-%20Simple.png" width=1000>

## Algorithms comparison
<img src="fig/Algorithms%20flowchart.png" width=800>

## References
* S. Jiang, J. Ferreira and M. C. Gonzalez, "Activity-Based Human Mobility Patterns Inferred from Mobile Phone Data: A Case Study of Singapore," in IEEE Transactions on Big Data, vol. 3, no. 2, pp. 208-219, 1 June 2017, DOI: [10.1109/TBDATA.2016.2631141](https://doi.org/10.1109/TBDATA.2016.2631141).

* H. Kanasugi, Y. Sekimoto, M. Kurokawa, T. Watanabe, S. Muramatsu and R. Shibasaki, "Spatiotemporal route estimation consistent with human mobility using cellular network data," 2013 IEEE International Conference on Pervasive Computing and Communications Workshops (PERCOM Workshops), San Diego, CA, USA, 2013, pp. 267-272, DOI: [https://doi.org/10.1109/PerComW.2013.6529493](10.1109/PerComW.2013.6529493).

* Yabe, T., Jones, N. K., Rao, P. S. C., Gonzalez, M. C., & Ukkusuri, S. V. (2022). Mobile phone location data for disasters: A review from natural hazards and epidemics. Computers, Environment and Urban Systems, 94, 101777, DOI: [10.1016/j.compenvurbsys.2022.101777](https://doi.org/10.1016/j.compenvurbsys.2022.101777).

* Sadeghinasr, B., Akhavan, A., & Wang, Q. (2019). Estimating commuting patterns from high resolution phone GPS data. In Computing in Civil Engineering 2019: Data, Sensing, and Analytics (pp. 9-16). Reston, VA: American Society of Civil Engineers, DOI: [10.1061/9780784482438.002](https://doi.org/10.1061/9780784482438.002).

* Zhao, X., Xu, Y., Lovreglio, R., Kuligowski, E., Nilsson, D., Cova, T. J. & Yan, X. (2022). Estimating wildfire evacuation decision and departure timing using large-scale GPS data. Transportation research part D: transport and environment, 107, 103277, DOI: [10.1016/j.trd.2022.103277](https://doi.org/10.1016/j.trd.2022.103277).
