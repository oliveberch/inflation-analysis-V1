# Inflation Analysis (Version 1.0)

This is the second version of the Inflation Analysis CLI Application, which has been enhanced with cloud deployment and improved database scalability. The project now leverages Google Cloud Platform (GCP) and BigQuery for better performance and scalability in handling large volumes of inflation data.

## What's New in V2

- **Database Migration to BigQuery**: Successfully migrated the application's database from MySQL to Google BigQuery, ensuring schema compatibility and maintaining data integrity. This migration allows for improved performance and better scalability.
  
- **Cloud Deployment on GCP**: The application is now deployed on Google Cloud Platform (GCP), utilizing services such as Compute Engine to handle the hosting and deployment. This cloud infrastructure enables secure, scalable, and efficient operations.

- **Modified CRUD Operations**: Adapted database schema and CRUD operations to align with BigQuery's data structure, ensuring smooth integration and effective data management.

- **Enhanced Security**: Implemented security measures as part of the cloud deployment, ensuring that the system remains secure in a cloud-based environment.

- **Non-Functional Improvements**:
  - **Scalability**: BigQuery enables the system to handle larger datasets and offers improved performance for data queries and analysis.
  - **Performance**: Optimized for fast data retrieval and analysis, even as the data grows in size.
  - **Documentation**: Comprehensive documentation has been added, covering the migration to BigQuery, GCP deployment, and modifications to the database structure.

## Technologies Used in V2

- **Programming Language**: Python
- **Libraries**: 
  - Matplotlib (for visualizations)
  - BigQuery Client (for database operations)
- **Database**: Google BigQuery (migrated from MySQL)
- **Cloud Platform**: Google Cloud Platform (GCP)
  - **Services Used**: Compute Engine, BigQuery
- **Version Control**: GitHub

## Installation

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/inflation-analysis-cli.git
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up GCP and BigQuery:
   - Configure a GCP project and enable BigQuery API.
   - Update the application settings with GCP credentials and BigQuery dataset information.
   - Set up your BigQuery dataset and import the inflation data (SQL scripts located in the `/database` folder).

4. Run the application:
   ```bash
   python main.py
   ```

### Cloud Deployment

1. **Google Cloud Platform Setup**:
   - Deploy the application on GCP using Compute Engine. You can follow the GCP documentation to create and configure the necessary instances.

2. **Connect to BigQuery**:
   - Ensure that the Compute Engine instance has appropriate permissions to interact with BigQuery.

3. **Deploy and Run**:
   - Once the environment is configured, deploy the application to the Compute Engine instance and ensure that it can interact with the BigQuery dataset.

## Usage

The CLI offers the same commands as in Version 1, but now with improved performance thanks to BigQuery integration:

- **Filter by Country**: Analyze inflation data for a specific country.
- **Filter by Time Period**: Specify a range of years for trend analysis.
- **View Visualizations**: Display line charts and bar graphs based on filtered criteria.

Example:
```bash
python main.py --country "United Kingdom" --start-year 2010 --end-year 2021
```
