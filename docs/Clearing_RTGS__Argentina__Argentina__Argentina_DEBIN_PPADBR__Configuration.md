# Configuring DEBIN Registration Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Argentina/Argentina/Argentina_DEBIN_PPADBR/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Argentina > DEBIN Registration Clearing > Configuration

- Argentina;)
  - DEBIN Registration Clearing;)
    - [Introduction](../../Argentina/Argentina_DEBIN_PPADBR/Introduction.htm)
    - [Configuration](../../Argentina/Argentina_DEBIN_PPADBR/Configuration.htm)
    - [Working with](../../Argentina/Argentina_DEBIN_PPADBR/Working_with.htm)
    - [Tasks](../../Argentina/Argentina_DEBIN_PPADBR/Tasks.htm)
    - [Outputs](../../Argentina/Argentina_DEBIN_PPADBR/Outputs.htm)
  - CT & DD (ACH) Clearing;)
  - Instant Clearing;)

Payments

# Configuring DEBIN Registration Clearing

Updated On 23 May 2023 |
 3 Min(s) read

Feedback
Summarize

This section helps the user to understand the configuration of these DEBIN records that are available in Temenos Payments Hub.

## Configuring the PPADEB.DEBIT.ORDER.PRODUCT Application

This table helps to create new product (DEBIN) and update its characteristics. It also has a provision to attach L2/L3 validation and auto-acceptance criteria APIs.

Enter the required details in the following fields:

| Field | Description |
| --- | --- |
| *Allow FX* | Indicates whether FX transaction is allowed or not |
| *Allowed Currency* | Currency that is allowed for the product |
| *Minimum Expiry* | Minimum validity period of the product |
| *Maximum Expiry* | Maximum validity period of the product |
| *Validate API* | Additional validation for the product |
| *Auto acceptance API* | Allows to attach the conditions for auto accepting the incoming DEBIN order |



## Configuring the PP.CLEARING.SETTING Application

This table helps to configure the fields to reject a transaction automatically.

1. Go to **Admin Menu**>**Payment Hub**>**Local Clearing**>**Clearing Setting**.
2. Configure the following fields in the ARGDBN record:
   - *Automated* *Return* as ‘Yes’
   - *Create* *Return* *Message* as ‘N’
   - *Create* *Return* *Booking* as ‘Ignore’



## Configuring the PPADEB.DEBIT.ORDER.PRODUCT Application

The PPADEB.DEBIT.ORDER.PRODUCT application allows users to set the *Retention Period* after which the Debin orders to be moved from live to history.

1. Configure the PPADEB.DEBIT.ORDER.PRODUCT application as per below.
2. Set the *Retention Period* to 35D. The records older than the retention period will then be moved from live to history.



## Configuring the ARCHIVE Application

The ARCHIVE application allows users to set the *Retention Period* after which the Debin orders to be moved from history to archive. The application that needs to be archived has to have an entry in the ARCHIVE application.

1. Configure the ARCHIVE application as per below.
2. Set the *Retention Period* to 1M. The records older than the retention period will then be archived.


3. All the records matching the status below and the *Retention Period* will be moved to history and then to archived.
   - Chargebacked.
   - Credited.
   - Crediting error.
   - Data error.
   - Deleted.
   - Expired.
   - Rejection From Customer.
   - Reject-pending Confirmation.

In this topic

- [Configuring DEBIN Registration Clearing](#ConfiguringDEBINRegistrationClearing)

- [Configuring the PPADEB.DEBIT.ORDER.PRODUCT Application](#ConfiguringthePPADEBDEBITORDERPRODUCTApplication)
- [Configuring the PP.CLEARING.SETTING Application](#ConfiguringthePPCLEARINGSETTINGApplication)
- [Configuring the PPADEB.DEBIT.ORDER.PRODUCT Application](#ConfiguringthePPADEBDEBITORDERPRODUCTApplication1)
- [Configuring the ARCHIVE Application](#ConfiguringtheARCHIVEApplication)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:51:40 PM IST