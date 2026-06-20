# Introduction to Debit Collection - Illustratingmodelparameters

> Source: https://docs.temenos.com/docs/Solutions/Payments/Orders/DB/Debit_Collection_Initiation_(DB)/Misc/Debit_Collection_Application.htm#IllustratingModelParameters

---

# Introduction to Debit Collection

Updated On 22 March 2025 |
 6 Min(s) read

Feedback
Summarize

Debit Collection (DB) application allows initiation of single direct debit collection requests for processing through Temenos Payments Hub. It performs the following function:

- Capture DD collection requests (manual)
- Validate and pre-process DD initiations
- Route the DD requests to Temenos Payments Hub
- Receive the debit collection requests from the Channel through APIs

DB supports capturing collection request for different types of clearings, such as Automated Clearing Houses (ACH) and Instant Payments. It supports only creation and capture of single DD collection requests. DB does not deal with inward collection processing (that is, collection requests initiated in another bank and received in DB bank through clearing or bilateral partner bank).

Collection requests initiated through the DB module are executed through Temenos Payments Hub only.

DD module of Temenos Transact allows initiating collection requests from the Transact modules that can be processed through Temenos Payments Hub or any third-party payment system. Thus, the DD module enables other applications in Transact to send collection requests to Temenos Payments Hub or any third-party payment system. Since the purpose of the DD module and the DB application are not the same, they continue to co-exist.

### Architecture of DB Application



| Item | Description |
| --- | --- |
| Collection Initiation Source | DB module can accept collection requests from various collection initiation sources as:   - Electronic Banking Channels: These are bank’s retail and corporate customer facing systems (such as internet banking portals), or STP feeder channels that aggregate payments from Corporate systems (such as ERP) or mobile banking channels. - Branch: There are payments initiated by a bank’s branch user in response to an over-the-counter instruction, or by a back-office user. |
| Debit Collection Application | The functionalities of the DB application are as follows:   - Receive debit collection requests through standard Temenos Transact interfaces, validate, enrich and route them to the payment system (Temenos Payments Hub) - Send the request status to the initiating source, when requested for the status update. - User can only initiate same-day collection requests (future dated collection requests are not allowed) |
| Payment Processing System | Validates, books and routes collection requests to an appropriate clearing system.  - Payment system can only be Temenos Payments Hub. - In-house collection requests are settled directly within the bank’s core banking instead of sending it to clearing. |
| Clearing Systems | Captures collection requests that can be cleared using different domestic clearings. Domestic clearings can be an instant payment clearing system or Automated Clearing Houses (ACH) that process bulk payments. |

## Configuring Debit Collection

Debit Collection (DB) module allows the user to configure the following:

### Parameter

This allows to configure the payment system to which the user needs to send the payment request.

Go to **Admin Menu** > **Payments** > **Debit Collection** > **Debit Collection Parameter Setup** to set up Debit Collection Parameter.

*Payment Connection Method*: This field allows to configure payment system to which the user needs to send the collection request.



It only supports Temenos Payments Hub.

### Product

Every collection request is assigned a ‘product’ attribute that determines the characteristics of the collection and manner in which the collection is processed. One of the generic product available in Model Bank is: Domestic – Collection request processed using domestic clearing.

To set up a debit collection product, go to **Admin Menu** > **Payments** > **Debit Collection** > **Debit Collection Product Setup**.



Either the user can select the Debit Collection product (during manual capture) or attach to the Debit Collection Order page to initiate the collection request. It allows the users to set the characteristics for capturing, validating, and processing collection request. The following are the important fields:

| Field | Description |
| --- | --- |
| *Allowed Payment Ccy* | Indicates the list of currencies allowed to initiate the collection request. |
| *Transaction limit* | Indicates the maximum collection amount allowed to initiate the collection request. |
| *Duplicate check* | Indicates the validation of the captured collection request for duplication. |
| *Allowed Future Date* | Indicates whether the collection request can be initiated using a future Requested Collection Date.  It only supports the value ‘No’. |
| *Allowed Charge Options* | Indicates the charge bearer options allowed for the product |
| *Default Charge Option* | Indicates the default charger bearer for the debit collection product |
| *Reachability Check* | Indicates whether reachability check is required or not |
| *Clearing Channel* | Indicates the preferred clearing channel for routing |
| *Clearing Code Format* | Indicates the format of the clearing code. The debit collection order is validated based on the clearing code entered in DB.DEBIT.COLLECTION.ORDER. |

## Illustrating Model Parameters

This section covers the below model parameters for the Debit Collection (DB) module.

| S.No. | Parameters | Description |
| --- | --- | --- |
| 1. | DB.DEBIT.COLLECTION.PARAMETER | It consists of high-level Debit Collection order configuration at the company level. This application facilitates the definition of the Payment Connection method. |
| 2. | DB.DEBIT.COLLECTION.PRODUCT | It captures the features that are specific to a collection product. |

## Illustrating Model Products

This section covers the below model products for the Debit Collection (DB) module.

| S.No. | Product Name | Product Attributes |
| --- | --- | --- |
| 1. | DB.DEBIT.COLLECTION.ORDER | Payment connection method in DB.DEBIT.COLLECTION.PARAMETER is set to TPH. Hence, all the Debit collections initiated from DB.DEBIT.COLLECTION.ORDER are routed to TPH for further processing. |