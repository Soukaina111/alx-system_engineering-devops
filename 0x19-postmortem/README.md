****************************Issue Summary*********************************************

During the period from April 5, 2022, to May 10, 2022, our software prototype experienced an outage that prevented users from adding any records. The error message "User-ID not found in the Users table" was consistently displayed, affecting only the developer during the experimental phase. The root cause of this issue was identified as an extra space in the variable name "User_ID". This oversight in naming conventions led to the system's inability to detect and process user IDs correctly.

********************************Duration of the Outage**************************************

The outage lasted from April 5, 2022, to May 10, 2022, spanning approximately one month. The start and end times are not specified due to the nature of the issue being a persistent problem rather than a single event.

**************************************Impact**********************************************************

The impact was limited to the developer's ability to add patient records to the database. The error message "User-ID not found in the Users table" was displayed, indicating a failure in the system's ability to recognize user IDs. This issue did not affect other users or services, as it was specific to the development environment.

********************************Timeline************************************************

- Issue detected: Upon attempting to add a patient record to the database.
- Detection method: Developer encountered the error message.
- Actions taken: Investigation into the database, variable types, lengths, and names within the framework.
- Misleading paths: Initial investigation focused on the database and variable properties, overlooking the naming convention.
- Incident escalated to: A university mentor.
- Resolution: The mentor identified the extra space in the variable name "User_ID".

******************************Root Cause and Resolution*************************************

The root cause of the issue was an extra space in the variable name "User_ID". This subtle naming convention error prevented the system from correctly identifying and processing user IDs. The resolution involved removing the extra space from the variable name, which immediately resolved the issue.

**********************Corrective and Preventive Measures****************************

To prevent similar issues in the future, we propose implementing automated variable naming conventions. This approach will help eliminate human error in naming variables. Additionally, we recommend fostering a culture of peer review and seeking fresh perspectives to catch potential issues early. Specific tasks include:

- Implementing automated variable naming conventions in the development environment.
- Encouraging peer code reviews to catch naming and other potential issues.
- Conducting regular code audits to identify and address naming conventions and other coding standards.

This incident underscores the importance of meticulous attention to detail and the value of external perspectives in software development. By implementing these corrective and preventive measures, we aim to enhance the reliability and robustness of our software development process.

