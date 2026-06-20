# Introduction to Payments Cockpit

> Source: https://docs.temenos.com/docs/Solutions/Payments/User_Agent/Payments_Operations_User_Agent/Payments_Operations_User_Agent/Introduction.htm

---

2. [Payments](../../../content/payments.html)
3. You are here:
   [Payments Cockpit](../Payments_Operations_User_Agent/Introduction.htm) > Introduction

- [Payments Cockpit Payments Cockpit](../Payments_Operations_User_Agent/Introduction.htm)
  - [Introduction](../Payments_Operations_User_Agent/Introduction.htm)
  - [Configuration](../Payments_Operations_User_Agent/Configuration.htm)
  - [Dashboard Dashboard](../Payments_Operations_User_Agent/Dashboard.htm)
  - [Operational Queues](../Payments_Operations_User_Agent/Operational_Queues.htm)
  - [Case Management](../Payments_Operations_User_Agent/Case_Management.htm)
  - [Search Payments](../Payments_Operations_User_Agent/SearchPayments.htm)
  - [Routing Data and Rules](../Payments_Operations_User_Agent/RoutingDataAndRules.htm)
  - [Extensibility](../Payments_Operations_User_Agent/Extensibility.htm)

Payments

# Introduction to Payments Cockpit

Updated On 10 July 2025 |
 5 Min(s) read

Feedback
Summarize

The Payments Cockpit allows users to interact with Temenos Payments Hub. It provides a holistic and end-to-end view of the transactions, including any associated items such as payment returns, payment recalls, and so on. It is designed to access accurate information with fewer clicks. It is a role-based interface that provides different views for Payments Operator, Manager, and Admin roles, respectively. The Payments Cockpit views provide data split per the current day, past, and future. Payments can be displayed as processing dated or value dated view. It is also possible to download payments data in CSV format from the listing screens.

The Payments Cockpit fetches data quickly by utilizing Unified User Experience (UUX-based) and Holdings Microservice (replicated data via event streaming).

The Payments Cockpit provides the following features,

- **Cut-off Monitor** – Displays payments and their cut-off times.
- **Case Management** – Displays pending cases, cases awaiting a response, and so on. Includes both MT and MX format case management messages and enables a case view for each payment.
- **Business Activity Monitor** – Displays ACH, RTGS, Instant, and Cross Border payments that are both processed and unprocessed.
- **STP Rate** – Displays STP and non-STP payments for the current day and the past 30 days.
- **Queues** - Provides the list of payments pending for action, authorisation, or response from external systems. It also contains payments in warehouse (Future dated payments) as well as payments awaiting to be sent to clearing or payments awaiting acknowledgement from clearing or SWIFT.
- **Track payments** – Efficiently monitors and accesses payments.
- **Initiate payments** – Initiates outward and book payments.
- **Configure payments** – Configures Temenos Payments Hub to suit custom needs.

Payments Cockpit would be available under a PPUAGT license code.

This user guide is intended for users who are familiar with the basics of payments processing.

Payments Cockpit is a plug-in User Agent that is part of Temenos Explorer. Read [Temenos Explorer User Guide](https://developer.temenos.com/temenos-explorer/docs/framework/overview/introduction/) for more information on the usage of the general functions of Temenos Explorer.

## Architecture

The below flow chart depicts how the Payments Cockpit accesses data from,

- Holdings microservice - Holds basic payments data consumed from events of Temenos Payments Hub. It is primarily used to enable faster search and tracking of payments. Read [Holdings Overview](https://docs.temenos.com/docs/Solutions/Infinity/Microservices/Modules/Microservices/holdings/c_Overview.htm) for more information on Holdings microservices. This is optional. The bank can retrieve information from holding MS or Transact. Read [Configuring the Database for Screens](Configuration.htm#Configur) for more details on configuring the database.

  It is recommended to use Holdings microservice to retrieve real time data in the **Dashboard** and **Search Payments** screens. Fetching data from Transact may result in delays when displaying information on the **Business Activity Monitor**, **Instant Payments Status**, **STP Rates**, and **Search Payments** screens.
- Temenos Payments Hub (including Payment initiations)



## Role-Based User Access

As the Payments Cockpit provides role-based views, a user can access the Payments Cockpit tabs based on the following roles.

Payments Manager

Payments Operator

Payments Admin

- [Dashboard](Dashboard.htm)
- [Operational Queues](Operational_Queues.htm)
- [Case Management](Case_Management.htm)
- [Search Payments](SearchPayments.htm)
- [Routing Data and Rules](RoutingDataAndRules.htm)

- [Dashboard](Dashboard.htm)
- [Operational Queues](Operational_Queues.htm)
- [Case Management](Case_Management.htm)
- [Search Payments](SearchPayments.htm)
- [Routing Data and Rules](RoutingDataAndRules.htm)

- [Routing Data and Rules](RoutingDataAndRules.htm)

## Switch Company Option For Users

The Payments Cockpit provides the user to switch between the accessible companies using the 'Switch Company' feature. When the user selects a company using the 'Switch Company' feature, the system updates the data displayed on the User Agent screen to reflect the selected company.



The table below shows the tabs and the data displayed by them.

| Tabs | Data Displayed |
| --- | --- |
| Dashboard and Search Payments | Display the data of the user logged in or the selected company records.  If user searches with different company from Advance Filter in 'Search Payments' tab, then system lists the other company records. |
| Operational Queues and Case Management | Display the records according to the file type, such as Int or Fin, based on the company's access permissions for the user. |
| Routing Data and Rules and Quick Actions | Display the data of the user logged-in or the selected company records. |

In this topic

- [Introduction to Payments Cockpit](#IntroductiontoPaymentsCockpit)

- [Architecture](#Architecture)
- [Role-Based User Access](#RoleBasedUserAccess)
- [Switch Company Option For Users](#SwitchCompanyOptionForUsers)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:40:13 PM IST