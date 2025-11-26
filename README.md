# Express Entry Case Study

A comprehensive data analysis project focused on Canada's Express Entry immigration system, designed to help international students and temporary workers understand their path to Permanent Residence (PR) in Canada.

## Overview

This project analyzes publicly available data from Immigration, Refugees and Citizenship Canada (IRCC) to provide insights into:
- 2026-2028 Immigration Plans for Permanent Residents
- Express Entry Rounds of Invitations
- Express Entry Invitation Trends
- Express Entry Invitation Draw Details

The analysis includes interactive Power BI dashboards and exploratory data analysis to help applicants make informed decisions about their immigration strategy.

## Purpose

After completing studies as an international student and obtaining a Post Graduation Work Permit, many individuals seek to understand their odds of obtaining Permanent Residence in Canada. This dashboard builds on top of IRCC's open data to help international students and temporary workers make sense of their immigration path.

## Project Structure

```
express_entry_case_study/
├── script1.py                          # Fetches Express Entry rounds data from IRCC JSON API
├── script2.py                          # Scrapes 2026-2028 immigration targets from Canada.ca
├── exploratory_data_analysis.ipynb     # Jupyter notebook for data exploration and analysis
├── express_entry_analysis.pbip         # Power BI project file
├── express_entry_analysis.SemanticModel/ # Power BI semantic model definitions
├── express_entry_analysis.Report/       # Power BI report definitions
├── notes.txt                           # Key insights and recommendations
├── tableau_colors.json                 # Color scheme configuration
└── icons/                              # Custom icons for visualizations
```

## Data Sources

1. **Express Entry Rounds Data**
   - Source: `https://www.canada.ca/content/dam/ircc/documents/json/ee_rounds_123_en.json`
   - Contains historical data on Express Entry invitation rounds

2. **Express Entry Candidates Data**
   - Source: `https://www.ircc.canada.ca/opendata-donneesouvertes/data/ODP-EE_candidates-ITA_score.csv`
   - Contains detailed candidate invitation data with CRS scores

3. **Immigration Targets (2026-2028)**
   - Source: `https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/corporate-initiatives/levels/supplementary-immigration-levels-2026-2028.html`
   - Contains official immigration targets by category

## Key Insights

### Immigration Plans (2026-2028)
- Top 3 targets for permanent residents include Economic, Family, and Refugees and Protected Persons categories
- Economic immigration category (particularly Federal High Skilled) offers high targets with less complicated processing
- French-speaking Permanent Resident Admissions outside Quebec targets are significant at ~30k/year

### Express Entry Invitations
- **Most Competitive Categories (2025):**
  - Trade Occupations: 40.40% CRS-to-Invitation Ratio (1,250 invitations, lowest CRS: 505)
  - Education Occupations: 13.20% CRS-to-Invitation Ratio (3,500 invitations, lowest CRS: 462)
  
- **Most Favorable Categories:**
  - French Language Proficiency: 1.05% CRS-to-Invitation Ratio
  - Canadian Experience Class: 2.17% CRS-to-Invitation Ratio

### Recommendations
1. **Focus on Economic Immigration**: Federal High Skilled category offers high targets and doesn't require employer support
2. **Learn French**: Increases CRS score for both Canadian Experience Class and French Language Proficiency routes
3. **Consider French Language Proficiency**: Offers the most favorable path based on invitation volume and CRS score trends

## Technologies Used

- **Python**: Data collection and processing
  - `pandas`: Data manipulation and analysis
  - `requests`: HTTP requests for API and web scraping
  - `beautifulsoup4`: HTML parsing
  - `jupyter`: Interactive data exploration

- **Power BI**: Data visualization and interactive dashboards
  - Semantic models for data modeling
  - Interactive reports with multiple pages
  - Custom visualizations and themes

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Jupyter Notebook or JupyterLab
- Power BI Desktop (for viewing/editing reports)

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd express_entry_case_study
```

2. Install required Python packages:
```bash
pip install pandas requests beautifulsoup4 jupyter
```

3. Run the data collection scripts:
```bash
python script1.py  # Fetches Express Entry rounds data
python script2.py  # Scrapes immigration targets
```

4. Open the Jupyter notebook for exploratory analysis:
```bash
jupyter notebook exploratory_data_analysis.ipynb
```

5. Open the Power BI project:
   - Open `express_entry_analysis.pbip` in Power BI Desktop
   - Ensure data sources are properly configured

## Usage

### Data Collection

Run the Python scripts to fetch the latest data:

```python
# script1.py - Fetches Express Entry rounds data
# Output: DataFrame with rounds data

# script2.py - Scrapes immigration targets
# Output: DataFrame with 2026-2028 targets
```

### Data Analysis

1. Open `exploratory_data_analysis.ipynb` in Jupyter
2. Run cells sequentially to:
   - Load and clean Express Entry candidate data
   - Extract minimum CRS scores
   - Scrape immigration targets from Canada.ca
   - Perform exploratory analysis

### Power BI Dashboards

The Power BI project includes multiple pages:
- **Overview**: Summary of immigration plans and Express Entry rounds
- **Trends**: Monthly trends across Express Entry round types
- **Details**: Detailed breakdown of invitation rounds

## Features

- **Real-time Data**: Scripts fetch data directly from official IRCC sources
- **Interactive Visualizations**: Power BI dashboards with filters and slicers
- **Comprehensive Analysis**: Multiple perspectives on Express Entry data
- **Actionable Insights**: Clear recommendations for immigration strategy

## Notes

- The immigration office publishes low-end and high-end targets; this analysis uses the targets to set appropriate expectations
- CRS-to-Invitation Ratio is calculated by dividing the lowest CRS score by the number of invitations issued
- Higher ratio indicates more competition (higher CRS score needed for fewer invitations)

## License

This project is for educational and informational purposes. Data sources are publicly available from IRCC and Canada.ca.

## Contributing

Contributions, issues, and feature requests are welcome. Please feel free to check the issues page.

## Disclaimer

This analysis is based on publicly available data and is intended for informational purposes only. It should not be considered as official immigration advice. Always consult with a licensed immigration consultant or lawyer for personalized immigration guidance.

