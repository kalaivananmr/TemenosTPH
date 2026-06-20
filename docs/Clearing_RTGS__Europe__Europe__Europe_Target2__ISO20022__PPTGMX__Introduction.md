# Introduction to TARGET2 RTGS (ISO20022)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_Target2_(ISO20022)_PPTGMX/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [TARGET2 Clearing (ISO20022)](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
  - [InterGIRO2 Credit Transfer InterGIRO2 Credit Transfer](../../Europe/Europe_InterGIRO2_Hungary_CT_PPHIG2/Introduction.htm)
  - [Equens (NL) Instant Payments Equens (NL) Instant Payments](../../Europe/Europe_NL_Instant_Payments_PPINCT/Introduction.htm)
  - [Swiss Interbank Clearing Swiss Interbank Clearing](../../Europe/Europe_Swiss_Clearing_PPSICH/Introduction.htm)
  - [SEPA Instant Clearing-EBA INST SEPA Instant Clearing-EBA INST](../../Europe/Europe_SEPA_EBA_Instant_Clearing_PPIEBA/Introduction.htm)
  - [SEPA Credit Transfer SEPA Credit Transfer](../../Europe/Europe_SEPA_Credit_Transfer_PPSPCT/Introduction.htm)
  - [SEPA Direct Debit SEPA Direct Debit](../../Europe/Europe_SEPA_Direct_Debit_PPSPDD/Introduction.htm)
  - [TARGET2 Clearing TARGET2 Clearing](../../Europe/Europe_Target2_PPTGTC/Introduction.htm)
  - [EPC SEPA Credit Transfer EPC SEPA Credit Transfer](../../Europe/EPC_SEPA_Credit_Transfer/Introduction.htm)
  - [EPC SEPA Direct Debit EPC SEPA Direct Debit](../../Europe/EPC_Direct_Debit/Introduction.htm)
  - [RPS German Cheque Processing RPS German Cheque Processing](../../Europe/Europe_RPS_German_Cheque_Processing_PPRPCQ/Introduction.htm)
  - [VIBER Payments VIBER Payments](../../Europe/Europe_VIBER_Payments_PPVIBR/Introduction.htm)
  - [MAV Payments MAV Payments](../../Europe/Europe_MAV_Payment_PPCLIT/Introduction.htm)
  - [Equens SEPA Direct Debit Equens SEPA Direct Debit](../../Europe/Europe_Equens_SEPA_Direct_Debit_PPEWSP/Introduction.htm)
  - [Equens SEPA Credit Transfer Equens SEPA Credit Transfer](../../Europe/Europe_Equens_SEPA_Credit_Transfer_PPEWSP/Introduction.htm)
  - [TARGET2 Clearing (ISO20022) TARGET2 Clearing (ISO20022)](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Introduction.htm)
    - [Introduction](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Introduction.htm)
    - [Configuration](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Configuration.htm)
    - [Working with](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Working_with.htm)
    - [Tasks](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Tasks.htm)
    - [Outputs](../../Europe/Europe_Target2_(ISO20022)_PPTGMX/Outputs.htm)
  - [Nordic Credit Transfer Payments Nordic Credit Transfer Payments](../../Europe/Europe_NCT_Payments_PPNPCT/Introduction.htm)
  - [Nordic Instant Credit Transfer Nordic Instant Credit Transfer](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm)
  - [Euro Swiss Interbank Clearing Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Introduction to TARGET2 RTGS (ISO20022)

Updated On 12 April 2026 |
 228 Min(s) read

Feedback
Summarize

Trans-European Automated Real-time Gross Settlement Express Transfer System (TARGET2) is a Real-Time Gross Settlement (RTGS) system owned and operated by the Eurosystem. It processes and settles payment orders (in EUR) submitted by central and commercial banks. The message exchange between participant bank and settlement system is based on Society for Worldwide Interbank Financial Telecommunications (SWIFT) Y-copy service and uses MT standard messages.

As part of the Target Services Consolidation project, the TARGET2 system is migrating from SWIFT MT to ISO20022 message standard. The migration is using big bang approach, hence there is no coexistence of SWIFT MT and ISO20022 messages for TARGET2 payments processing. The following changes occur due to the migration:

- TARGET 2 moves from Y-Copy to V-Shape processing
- SWIFT MT payment messages are not supported and replaced with corresponding ISO20022 standard XML messages
- New messages are introduced to support case management for RTGS payments (payment recalls, resolution of investigation, and so on)

TARGET2 services (RTGS, TIPS, and so on) can be accessed through ESMIG (new gateway). Participant banks are enabled to access TARGET2 ESMIG using SWIFT and SIA COLT network service providers. Participant banks can use one of these gateways for connecting to TARGET2 RTGS.

Temenos Payments Hub (TPH) supports TARGET2 ISO20022 (MX) messages and workflows relating to interbank RTGS payments (pacs messages), payment cancellation requests and resolution of investigation under a new licensable module (PPTGMX). It also provides a connector to TARGET2 using SWIFT interact and can be made available (optionally) under a separate license (SWFTAL).

TARGET2 ISO20022 (MX) solution is compliant with the ‘T2 Release R2026.JUNE’ specifications.

PPTGMX module has to be deployed on top of the existing T2 RTGS module (PPTGT).

## Types of Participants

There are three type of participants in TARGET2 scheme:

| Type of Participant | Description |
| --- | --- |
| Direct Participant | They have direct access to RTGS and can provide indirect access for other credit institutions, and offer additional services. They are responsible for the following:   - Own reference data - Liquidity management in RTGS - Monitoring the settlement process - All cash transfers sent or received on their cash account by any entity registered through them |
| Indirect Participant | Indirect member bank does not hold a settlement account in TARGET2. They have specific arrangements with a direct participant bank to process their payments. Each indirect participant needs a published BIC11.  An indirect participant can initiate SWIFT payments (such as MT103 or MT202) to their direct participants, who redirect the payment to TARGET2 in ISO20022 format (as pacs.008 or pacs.009). |
| Multi-addressee | RTGS Account Holders are able to authorise their branches and credit institutions belonging to their group to channel payments through the linked RTGS DCA without their involvement by submitting/receiving cash transfers directly to/from RTGS.  The cash transfer order is settled on the linked RTGS DCA. |

## Payment Instruments

TPH supports TARGET2 Credit Transfer (CT) and Return payment (RT).

- Customer Transfer: A customer transfer is a payment in which the ordering customer or the beneficiary customer or both are non-financial institutions.

- pacs.008 messages is used for customer transfer
- Only single transaction per message is allowed

- Bank Transfer: A bank transfer is a payment in which the ordering institution and the beneficiary institution are both financial institutions.

- pacs.009 messages is used for bank transfer and cover
- Only single transaction per message is allowed
- pacs.010 message is used for Financial Institutions direct debit

- Return Payment: Participant banks can return an incoming payment to the sender when incoming payment can’t be processed successfully due to errors (such as creditor account is closed) or as a response to a recall request.

- pacs.004 message is used for return
- Only single transaction per message is allowed

TARGET2 also supports pacs.010 (direct debit) and various payment or liquidity related messages. TPH does not support processing of TARGET2 messages.

## Types of Messages

TPH supports processing of the following TARGET2 messages in ISO20022 format:

Since TARGET2 is an RTGS system, each message (in ISO20022 XML format) has one payment (no bulking).

| Message | Description | Outward (To TARGET2) | Inward (From TARGET2) |
| --- | --- | --- | --- |
| pacs.008.001.08 | Customer transfer |  |  |
| pacs.009.001.08 CORE | Bank transfer |  |  |
| pacs.009.001.08 COVER | Bank transfer – cover |  |  |
| pacs.010. 001.03 | Financial Institutions direct debit initiation |  |  |
| pacs.004.001.09 | Return payment |  |  |
| pacs.002.001.10 | Payment status report | × |  |
| camt.056.001.08 | Payment cancellation request |  |  |
| camt.029.001.09 | Resolution of investigation |  |  |
| camt.025.001.07 | Receipt (against outward camt.029) | × |  |
| admi.007.001.01 | Receipt acknowledgement (from ESMIG) | × |  |
| camt.054.001.12 | Liquidity Transfer Advice | × |  |
| camt.050.001.07 | Liquidity Credit Transfer |  | × |

TARGET2 supports several other messages for various functions (such as liquidity management, account management, direct debit). The table lists only payments relevant to TPH and messages that support payment processing. TPH supports redirection of payments (pacs.008, pacs.009, pacs.004) between TARGET2 and SWIFT CBPR+. Read the International Payments (MX) user guide for more details on CBPR+ cross border payment processing features and configurations.

## Payment Direction

Depending on the direction of flow of the funds, the system supports processing of following types of TARGET2 payments:

| Payment Type | Description |
| --- | --- |
| Incoming | The originating party (Debtor) of the payment does not reside in the processing bank’s ledger. The beneficiary party (Creditor) of the payment resides in the processing bank’s ledger.  Incoming payment from TARGET2 to a direct participant. |
| Outgoing | The originating party (Debtor) of the payment resides in the processing bank’s ledger. The beneficiary party (Creditor) of the payment does not reside in the processing bank’s ledger.  Payment captured by a direct participant and sent to TARGET2. |
| Redirect | Neither the originating party (Debtor) nor the beneficiary party (Creditor) of the payment resides in the processing bank’s ledger.  Incoming payment from correspondent bank received through SWIFT by direct participant and redirected through TARGET2 (and vice versa). |

TPH supports redirection of CBPR+ payments to TARGET2 and vice versa. Redirection message format is decided based on the following configurations:

With SWIFT migrating from MT to CBPR+ MX format, a configuration is provided in the Company Properties application to decide if the bank wants to send out cross border payments using SWIFT MT format or MX format. SWIFT payments are routed using LORO or NOSTRO or Account channel. This is configured by setting a date in the *SWIFTMX Effective Date* field in the Company Properties application. This configuration is applicable for all cross border payments, the system cannot selectively send MT or MX format for specific messages or for specific correspondents.

| Configuration in Company Properties | Message Format |
| --- | --- |
| Effective date configured. The current business date is greater than or equal to the effective date. | Company configured to send cross border payments in MX format. |
| Effective date configured. The current business date is less than the effective date. | Company configured to send cross border payments in MX format at a future date. Until the future date is reached, MT messages are sent. |
| Effective date is not configured (blank). | Company configured to send cross border payments in MT format. |

Cross border payments can also be redirected through SWIFT based local RTGS clearings (for example, TARGET2, CHAPS and so on). These SWIFT based RTGS systems can either use MT format or MX format. For such redirections through the clearings, the system refers to the *SWIFT Based* and *Effective Date* fields configured at the clearing level to decide whether to send the message in MT or MX format.

| Configuration in Clearing (PP.CLEARING application) | Message Format |
| --- | --- |
| The *Swift Based* field is configured as MX  The *Effective Date* field is blank | Clearing is configured to send messages in MX format |
| The *Swift Based* field is configured as MX  The *Effective Date* field is configured and the current business date is greater than or equal to the effective date. | Clearing is configured to send messages in MX format |
| The Swift Based flag is configured as MX  The *Effective Date* field is configured and the current business date is less than the effective date. | Clearing is configured to send messages in MX format at a future date  Until the future date is reached, MT messages are sent |
| The Swift Based flag is configured as Y  The *Effective Date* field is blank. | Clearing is configured to send messages in MT format |

Based on the above mentioned configurations in company properties and clearing level, the system supports the following message conversions:

| MT to MX | MX to MT |
| --- | --- |
| - MT 103 to pacs.008 - MT 101 to pacs.008 - MT 202 to pacs.009 - M 202 COV to pacs.009 COV | - pacs.008 to MT103 - pacs.009 to MT202 - pacs.009 COV to MT202 COV |

The following table shows the redirected message format when incoming cross border payments are received from SWIFT in MT or MX format and to be redirected through TARGET2. The TARGET2 clearing configurations are referred for this purpose.

| Clearing Configuration | Message Direction | Incoming Message Type  (from correspondent bank) | Outgoing Message Type  (To TARGET2) |
| --- | --- | --- | --- |
| Clearing configured to send messages in MX format | Redirect | MT 103 | pacs.008 (TARGET2 format) |
| Redirect | CBPR+ pacs.008 | pacs.008 (TARGET2 format) |
| Clearing configured to send messages in MT format | Redirect | MT 103 | MT 103 |
| Redirect | CBPR+ pacs.008 | MT 103 |
| Clearing configured to send MX messages in future | Redirect | MT 103 | MT 103 until future date  pacs.008 (TARGET2 format) after future date |
| Redirect | CBPR+ pacs.008 | MT 103 until future date  pacs.008 (TARGET2 format) after future date |

The following table shows the redirected message format when incoming TARGET2 payments are received and to be redirected to correspondent bank as SWIFT cross border message in MT or MX format. The company properties configurations are referred for this purpose.

| Company Configuration | Message Direction | Incoming Message Type  (from TARGET2) | Outgoing Message Type  (to correspondent bank) |
| --- | --- | --- | --- |
| Company configured to send cross border payments in MX format | Redirect | MT 103/202 | CBPR+ pacs.008/pacs.009 |
| Redirect | pacs.008/pacs.009 | CBPR+ pacs.008/pacs.009 |
| Company configured to send cross border payments in MX format at a future date | Redirect | MT 103/202 | MT 103/202 until future date  CBPR+ pacs.008/pacs.009 after future date |
| Redirect | pacs.008/pacs.009 | MT 103/202 until future date  CBPR+ pacs.008/pacs.009 after future date |
| Company configured to send cross border payments in MT format | Redirect | MT 103/202 | MT 103/202 |
| Redirect | pacs.008/pacs.009 | MT 103/202 |

## TARGET2 Payment Capture

The system provides the following options to capture and initiate outgoing TARGET2 payments.

[Payment Order](#)

The front office users can capture outgoing TARGET2 payment using the PAYMENT.ORDER (`PO`) application. The system provides dedicated menu to capture TARGET2 payments. These screens have the relevant ISO20022 fields.

- TARGET2 Customer Transfer (MX) – On successful processing outgoing pacs.008 message is generated and sent to TARGET2 through SWIFT
- TARGET2 Bank Transfer (MX) – On successful processing outgoing pacs.009 message is generated and sent to TARGET2 through SWIFT
- TARGET2 Liquidity Transfer Request (MX) – On successful processing, outgoing LTR payment message (camt.050 or pacs.009) is generated and sent to TARGET2 through SWIFT.

Dedicated payment order products are provided for TARGET2 customer transfer (TARGET2) and bank transfer (TARGET2BT), and liquidity transfer (TARGET2LTR).

Read the [Working with TARGET2 RTGS (ISO20022)](Working_with.htm) topic for details on the fields available in the respective payment order screens.

[Order Entry](#)

The back office users can capture TARGET2 payments using the Order Entry (OE) screen. The system provides generic menus to capture ISO20022 format payments, such as TARGET2. The following screens have the relevant ISO20022 fields.

| Process | Screens |
| --- | --- |
| Outgoing Payment Capture | - Outgoing ISO Customer Transfer – On successful processing, TARGET2 pacs.008 message is generated ad sent through SWIFT - Outgoing ISO Bank Transfer – On successful processing, TARGET2 pacs.009 message is generated and sent through SWIFT - Outgoing ISO Liquidity Transfer Request – On successful processing, TARGET2 camt.050 / pacs.009 is generated and sent through SWIFT - Outgoing Financial Institutions direct debit transfer – On successful processing, TARGET2 pacs.010 message is generated and sent through SWIFT   For TARGET2 payments, the channel must be determined or imposed as TGT. |
| Incoming Payment Capture | The system provides the following menus to manually capture incoming ISO format payments (for exceptional scenarios, where STP capture is not possible). These screens have the relevant ISO20022 fields.   - Incoming ISO Customer Transfer – The user can capture an incoming TARGET2 customer payment details manually and post accounting entries - Incoming ISO Bank Transfer – The user can capture an incoming TARGET2 bank payment details manually and post accounting entries   Routing agent details are not captured in the screen while manually creating incoming payments.  For TARGET2 payments, the channel must be selected as TGT. |

Read the [Working with TARGET2 RTGS (ISO20022)](Working_with.htm) topic for details on the fields available in the respective order entry screens.

[Delivery Preview of Outgoing Payment](#)

When an outgoing payment is captured in system using Order Entry screens as mentioned above, system provides an option to view the expected XML message to be generated by system based on the data captured and determined channel (TGT for TARGET2). This feature is called delivery preview.

The user needs to first capture and validate the payment details to ensure there are no errors. Then click on the delivery preview option, which opens a new screen and shows the expected XML message. The preview shows the payload without any business application header or technical header. In case of any payload XSD validation error, the error is displayed at the end of the message.

- This option is applicable for single messages only, not applicable for bulk payments.
- This option is applicable for CBPR+ payments as well as SWIFT MX based RTGS payments (such as TARGET2) captured from the OE screen.

[Initiation using pain.001](#)

The system supports initiation of TARGET2 customer payment (pacs.009) using pain.001 (v9) and response using pain.002 (v10).

## TARGET2 Payment Repair

The system provides generic ISO view and ISO repair screens with relevant fields for viewing and repairing payments sent or received using ISO20022 format. TARGET2 MX payments are repaired using the ISO repair screen.

Incoming, outgoing, or redirected TARGET2 payments having active functional or technical error are moved to repair status (235). The users can open such payments using the Pending Repair enquiry for viewing or modification (repair). In view mode, all the fields are displayed as read-only whereas in repair mode, selected fields are editable (for which repair is allowed).

Modification is not allowed for debtor, ultimate debtor, ultimate creditor, creditor, debtor agent and previous instructing agent details in repair mode.

The user can modify the details and validate the payment with modified details. If all validations are successful, then the user can commit the payment for further processing with the repaired details.

For a TARGET2 payment in repair mode, the following are some of the fields, which are editable and can be modified.

- Instruction Priority
- Output Channel
- Instructed Agent Details (BIC, Clearing System ID and Clearing Member ID)
- Credit Account
- Debit/Credit side FX rates (Customer Spread, Treasury Rate, Exchange Rate)
- Requested Execution Date
- Debit and Credit Value Date
- Charge Information
- Routing Information (BIC, Clearing System ID and Clearing Member ID, Name, LEI, Account Number, Unstructured Address) for following agents
  - Creditor Agent
  - Intermediary Agent 1,2,3
  - Instructing Reimbursement Agent
  - Instructed Reimbursement Agent
  - Third Reimbursement Agent
- Additional Information fields
  - Local Instrument
  - Category Purpose
  - Transaction Purpose
  - Instruction for Creditor Agent
  - Instruction for Next Agent
  - Time Indication
- Regulatory Reporting Information
- Unstructured Remittance Information
- Return/Reject option

## TARGET2 ISO20022 Message Structure

The following diagram shows the structure of a TARGET2 MX (ISO20022) message sent across SWIFT network.

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS.png)

The RequestPayload section contains the business information consisting of following blocks:

| Block | Description |
| --- | --- |
| Application Header | It contains the business application header (BAH) |
| Document | It contains the actual business message (such as pacs.008, pacs.009, pacs.004, pacs.010 and so on) |

The RequestHeader section contains the details required to transport the request payload over a network provider. This is also referred as technical header.

TPH support generation of the message containing the Technical header, Business Application Header and the underlying document for sending the message over SWIFT.

[Document](#)

The Document block contains information about the actual business message. It consists of two sections:

- The first section is Group Header, which contains common details applicable for the underlying business message. Some of the important fields in the Group Header section are:

| Field | Description |
| --- | --- |
| *Message Identification* | This is a unique identification for the business message and populated by system as per TARGET2 specification of individual message. |
| *Creation Date Time* | The system populates the date and time when the XML document is created |
| *Number Of Transaction* | Indicates the number of transaction details in the business message. TARGET2 allows only single transaction details to be sent/received in each message. Hence, this fields must always have value 1 (single transaction details) |
| *Settlement Information* | Applicable for customer and bank transfer. This section is used to provide information on the following:   - Settlement Method – system populates value CLRG for TARGET2 payments. - Clearing System Code – system populates value TGT for TARGET2 payments |

- The second section contains information about the business message such as:

| Block | Description |
| --- | --- |
| Credit Transfer Transaction Information | Contains details of the transaction for customer transfer (pacs.008) and bank transfer (pacs.009) |
| Credit Transfer Transaction Information | Contains details of return transaction (pacs.004) |

[Business Application Header](#)

The Business Application Header (BAH) is a mandatory element in the TARGET2 ISO20022 format message. The system provides a configurable option to generate the business application header for TARGET2 messages. The configurations to generate business application header are maintained in Delivery module.

The system supports the following elements of BAH:

| Field | Description |
| --- | --- |
| *From* | Specifies the party or agent who has created the message. The system supports population of BIC tag under From / Financial Institution Identification. Other fields are not populated. |
| *To* | Specifies the receiving agent who processes the business document. The system supports population of BIC tag under To / Financial Institution Identification. Other fields are not populated. |
| *Business Message Identifier* | Specifies an identification for the message. This is useful to match with outgoing payment when acknowledgements are received. The system populates this field for all generated messages. |
| *Message Definition Identifier* | The system provides a configurable option to populate the full ISO message name (such as pacs.009.001.08 for Customer Transfer) ` |
| *Creation Date* | The system populates the date and time at which the message is generated. |

The following BAH tags are not supported:

- Character Set
- Market Practice
- Copy Duplicate
- Related

[Technical Header](#)

A technical header is required to transport the underlying request payload consisting of business application header and document.  The Swift Alliance Access provides a proprietary format, XMLv2 (also called DataPDU), which is used to exchange ISO20022 messages (MX) over Interact services. This format envelopes the request payload, adding a technical header and a technical trailer.

The system provides a configurable option to generate the technical header for sending messages through SWIFT to TARGET2. The configurations to generate technical header are maintained in Delivery module.

Read the Support for SWIFTNet Interact MX services user guide (Temenos Transact > Delivery > Support for SWIFTNet Interact MX services) for more information on features and configurations related to BAH and Technical header, sending/receiving MX messages.

## Supported Message Elements in TARGET2 ISO20022 Payments

The following sections explains about the various elements in the ISO20022 (MX) format TARGET2 payment messages (Customer Transfer - pacs.008, Bank Transfer - pacs.009, pacs.010) which can be captured and processed in TPH.

[Party and Agent Roles](#)

ISO20022 (MX) format TARGET2 payment messages uses several roles to indicate the various parties and agents involved in the payment chain.

Some of these roles are static in nature and therefore transmitted through the payment chain. Some agents are not static, they are changed/swapped as and when payment is processed and redirected through agents.

The system supports the following party and agent roles for ISO20022 format TARGET2 payments.

[Debtor](#)

This element identifies the party which owes an amount of money to the (ultimate) creditor. This is a static role and remains unchanged in the entire payment chain. The debtor could be a customer account for customer transfer or financial institution account for bank transfer.

While capturing an outgoing payment using `OE` screen or `PO` screen, the system provides an option to enter the following details for debtor:

| Field | Description |
| --- | --- |
| *Name* | Debtor name |
| *Structured Address* | Consists of the following elements:   - Department - Sub Department - Street Name - Building Number - Building Name - Floor - Post Box - Room - Post Code - Town Name - Town Location Name - District Name - Country Sub Division - Country   For an outgoing payment, the debtor name and address is fetched from the customer record (based on the debit account number) and populated in the outgoing message.  However, if the user uses the impose option for the debtor, then the manually entered name and address is populated in outgoing message (instead of the customer record details). |
| *Organisation / Financial Institution Identification* | For customer transfer, Organisation Identification field is applicable. For bank transfer, Financial Institution Identification field is applicable.   - BIC – To capture the debtor BIC - LEI – Legal Entity Identifier of the debtor - Other Identification – Applicable for customer transfer only   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| *Private Identification* | Applicable for customer transfer only   - Date and Place of Birth   - Birth Date   - Province Of Birth   - City Of Birth   - Country Of Birth - Other Identification   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| *Country of Residence* | Debtor’s country of residence |

Based on the entered debit account, the debtor account tag is mapped in the outgoing message. If IBAN is entered, then it is mapped under IBAN tag. If IBAN is not entered, it is not entered under Other Identification tag. For outgoing payments, the system maps only the account number, other optional fields are not mapped.

When an incoming CBPR+ payment is received, the debtor and debtor account details are stored in the system. If the payment is redirected, the received debtor and debtor account details are mapped in the redirected message. The ORDPTY role is used to store and map debtor details. When a CBPR+ payment is opened for repair, the debtor details are displayed in the read-only mode. The fields which are displayed for debtor in view and repair screens are same as in the capture screen mentioned above. Additionally the unstructured address fields are also displayed in view/repair screens as those might be present in incoming payments. Modification of debtor details is not allowed in repair mode.

- Debtor role is similar to ordering customer (tag 50) in MT103 message.
- Because of co-existence of MT and MX format, unstructured address elements are also supported in CBPR+ format (for scenarios when the payment is initiated in SWIFT FIN and redirected as MX message).
- SWIFT recommends to use structured information when payments are initiated in MX.

Transact customer application is used to capture structured address details as required in ISO20022 format. Banks should ensure proper structured address details are maintained in the customer records, so that it is populated for debtor role in outgoing CBPR+ payments.

Outgoing transfer captured in the `OE` or `PO` application fetches the name and address details from the customer record, and populates the details against the debtor element in the generated message ( for example, pacs.008 and pacs.009). The address details in customer record may be structured and unstructured.

Here, the preference is given to the structured address details in the outgoing message, if *Town Name* and Country details are available. In other situations, unstructured address is populated in the outgoing messages (if available). However, if impose option is used, then name or address details from customer record is not used.

Rules for capturing the debtor details are as follows:

- If debtor BIC is provided, then all other fields are optional.
- If debtor LEI is provided, then it must adhere to the LEI format.
- If address is provided, the user must provide structured address, unstructured address, or Hybrid Address. Read [Support for Hybrid Address](#Hybrid) for more details on Hybrid Addresses.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- If address is provided, then name of the debtor must be provided.
- Value should be provided in either Organization Identification or Private Identification field. When a value is provided in the Other Identification field (within Organization or Private Identification), maximum two occurrences are allowed.

[Ultimate Debtor](#)

This element identifies the ultimate party, which owes an amount of money to the (ultimate) creditor. This is a static role and remains unchanged in the entire payment chain. Ultimate debtor is applicable only for customer transfer.

While capturing an outgoing payment using the `OE` screen or `PO` screen, the system provides option to enter the following details for ultimate debtor:

| Field | Description |
| --- | --- |
| *Name* | Ultimate debtor name. |
| *Structured address* | Structured address consists of the following elements   - Department - Sub Department - Street Name - Building Number - Building Name - Floor - Post Box - Room - Post Code - Town Name - Town Location Name - District Name - Country Sub Division - Country |
| *Organisation Identification* | - BIC – to capture the ultimate debtor BIC - LEI – legal entity identifier of ultimate debtor - Other Identification   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| *Private Identification* | - Date and Place of Birth   - Birth Date   - Province Of Birth   - City Of Birth   - Country Of Birth - Other Identification   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| *Country of Residence* | Ultimate debtor’s country of residence |

When an incoming CBPR+ payment is received, the ultimate debtor details are stored in the system. If the payment is redirected, the received ultimate debtor details are mapped in the redirected message. The ULTDBT role is used to store and map ultimate debtor details.

When the user opens a CBPR+ payment for repair, the ultimate debtor details are displayed in the read-only mode. The fields which are displayed for ultimate debtor in view and repair screens are same as in the capture screen. Modification of ultimate debtor details is not allowed.

There is no tag in SWIFT MT message for ultimate debtor information.

Rules for capturing the ultimate debtor details are as follows:

- If the ultimate debtor BIC value is provided, then all other fields are optional.
- If the ultimate debtor LEI value is provided, then it must adhere to the LEI format.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- If the address is provided, then name of the ultimate debtor must be provided.
- Either Organization Identification or Private Identification should be provided. When Other Identification value is provided (within Organization or Private identification), maximum two occurrences are allowed.

[Creditor](#)

This element identifies the party to which an amount of money is due. This element is also referred as beneficiary. This is a static role and remains unchanged in the entire payment chain. The creditor could be a customer account for customer transfer or financial institution account for bank transfer.

While capturing an outgoing payment using the `OE` screen or `PO` screen, the system provides an option to enter the following details for creditor:

| Field | Description |
| --- | --- |
| *Name* | Indicates the name of the creditor (beneficiary). |
| *Structured address* | The structured address consists of the following elements:   - Department - Sub Department - Street Name - Building Number - Building Name - Floor - Post Box - Room - Post Code - Town Name - Town Location Name - District Name - Country Sub Division - Country |
| *Unstructured address lines* | Unstructured address lines (max 3 lines) for scenarios when the message was initiated in MT format. |
| *Organisation / Financial Institution Identification* | For customer transfer, Organisation Identification details are applicable. For bank transfer, Financial Institution Identification details are applicable.   - BIC – To capture the creditor BIC - LEI – Legal Entity Identifier of creditor - Other Identification – Applicable for customer transfer only   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| *Private Identification* | Applicable for customer transfer only   - Date and Place of Birth   - Birth Date   - Province Of Birth   - City Of Birth   - Country Of Birth - Other Identification   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| *Country of Residence* | Creditor’s country of residence |

The system provides an option to maintain creditor or beneficiary details using the BENEFICIARY application. While capturing outgoing CBPR+ payment using the PO application or OE screen, the user can select a valid beneficiary record id and click on Validate. The system fetches beneficiary details and populates the details on the screen.

Based on the entered credit account, the creditor account tag is mapped in the outgoing message. If IBAN is entered, then it is mapped under IBAN tag, else mapped under Other Identification tag. For outgoing payments, the system maps only the account number, other optional fields are not mapped.

When an incoming CBPR+ payment is received, the creditor and creditor account details are stored in the system. If the payment is redirected, the received creditor and creditor account details are mapped in the redirected message. The BENFCY (for customer transfer) or BENINS (for bank transfer) role is used to store and map creditor details.

When an incoming CBPR+ payment is received and the system is unable to credit the beneficiary account, the payment is moved to repair. Possible scenarios where the system is unable to credit the beneficiary account are:

- creditor account is not existing
- creditor account is closed
- posting restrictions on creditor account
- creditor account is not provided

When the user opens a CBPR+ payment for repair, the creditor details are displayed in the read-only mode, except the *Creditor Account* field. The fields which are displayed for creditor in view and repair screen are same as in the capture screen. The user can modify the creditor account details and submit the payment for processing.

- Creditor role is similar to beneficiary customer (tag 59) in MT103 message and beneficiary institution (tag 58) in MT202 message.
- Because of co-existence of MT and MX format, unstructured address elements are also supported in CBPR+ format (for scenarios when the payment is initiated in SWIFT FIN and redirected as MX message).
- SWIFT recommends to use structured information when payments are initiated in MX.

Rules for capturing the creditor details are as follows:

- If the Creditor BIC value is provided, then all other fields are optional.
- If the Creditor LEI value is provided, then it must adhere to the LEI format.
- If address is provided, the user must provide structured address, unstructured address, or Hybrid Address. Read [Support for Hybrid Address](#Hybrid) for more details on Hybrid Addresses.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- If address is provided, then the name of creditor must be provided.
- Either Organization Identification or Private Identification details should be provided. When Other Identification details are provided (within Organization or Private identification), maximum two occurrences are allowed.

Depending on the situation, structured and unstructured address details can be captured for creditor on any outgoing transfer captured in the `OE` or `PO` application there is a possibility that both structured and unstructured address details are captured for creditor. Here, preference is given to the structured address details in the outgoing message if both *Town Name* and Country details are available. In other situations, unstructured address is populated in the outgoing messages (if available).

[Ultimate Creditor](#)

This element identifies the ultimate party to which an amount of money is due. This is a static role and remains unchanged in the entire payment chain. Ultimate creditor is applicable only for customer transfer.

While capturing an outgoing payment using the OE screen or PO screen, the system provides an option to enter the following details for ultimate creditor:

| Field | Description |
| --- | --- |
| *Name* | Indicates the name of the ultimate creditor. |
| *Structured address* | Structured address consists of the following elements   - Department - Sub Department - Street Name - Building Number - Building Name - Floor - Post Box - Room - Post Code - Town Name - Town Location Name - District Name - Country Sub Division - Country |
| *Organisation Identification* | - BIC – to capture the creditor BIC - LEI – legal entity identifier of creditor - Other Identification   - Identification   - Scheme Name (Code or Proprietary)  - Issuer |
| *Private Identification* | - Date and Place of Birth   - Birth Date   - Province Of Birth   - City Of Birth   - Country Of Birth - Other Identification   - Identification   - Scheme Name (Code or Proprietary) - Issuer |
| *Country of Residence* | Ultimate Creditor’s country of residence |

The system provides an option to maintain ultimate creditor details against a creditor or beneficiary using the BENEFICIARY application. While capturing outgoing CBPR+ payment using `PO` or `OE` screen, the user can select a valid beneficiary record id and click Validate. The system fetches the beneficiary details and populates on the screen. If the user maintains the ultimate creditor details, then those details are also defaulted based on the beneficiary record.

When an incoming CBPR+ payment is received, the ultimate creditor details are stored in system. If the payment is redirected, the received ultimate creditor details are mapped in the redirected message. The ULTCDT role is used to store and map ultimate creditor details.

When the user opens a CBPR+ payment for repair, the ultimate creditor details are displayed in the read-only mode. The fields which are displayed for ultimate creditor in view and repair screen are same as in the capture screen. Modification of ultimate creditor details is not allowed.

There is no tag is SWIFT MT message for ultimate creditor information.

Rules for capturing the ultimate creditor details are as follows:

- If the Ultimate Creditor BIC value is provided, then all other fields are optional.
- If the Ultimate Creditor LEI value is provided, then it must adhere to the LEI format.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- If address is provided, then name must be provided.
- Either Organization Identification or Private Identification details should be provided. When Other Identification is provided (within Organization or Private identification), maximum two occurrences are allowed.

[Initiating Party](#)

This element identifies the party which initiates the credit transfer on behalf of the debtor. This is a static role and remains unchanged in the entire payment chain. This role is applicable for customer transfer when initiated using pain.001 message containing Initiating Party details. If the payment is initiated using the OE screen or `PO` application, this role is not captured on screen.

When the user receives an incoming payment, the initiating party details are stored in the system if received. If the payment is redirected, the received initiating party details are mapped in the redirected message. The INIPTY role is used to store and map ultimate creditor details.

The Initiating Party details are not displayed in the view or repair screens.

Rules for capturing the initiating party details are as follows:

- If initiating party BIC is provided, then all other fields are optional.
- If initiating party LEI is provided, then it must adhere to the LEI format.
- If address is provided, the user must provide structured address, unstructured address, or Hybrid Address. Read [Support for Hybrid Address](#Hybrid) for more details on Hybrid Addresses.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- If address is provided, then name must be provided.
- Either Organization Identification or Private Identification details should be provided. When Other Identification details are provided (within Organization or Private identification), maximum two occurrences are allowed.

[Instructing Agent](#)

This role identifies the agent that instructs the next agent in the payment chain to process the payment. It can be considered as the sender of the payment message. This is not a static role, it keeps on changing as and when the payment is redirected.

For outgoing and redirected payments, the system populates own company BIC (configured in company properties) as the instructing agent. No other fields are populated for this role in the generated message.

When the user opens a TARGET2 payment for repair, the following instructing agent related fields are displayed in the read-only mode and not allowed to be modified.

| Field | Description |
| --- | --- |
| *BIC* | Indicates the Sender/Instructing agent BIC. |
| *Clearing System ID* | Indicates the ISO clearing system identification. |
| *Clearing Member ID* | Indicates the national clearing code/member identification. |

Rules for capturing instructing agent details are as follows:

- When the transaction is exchanged on the SWIFT network (that is, if the instructing agent or sender and instructed agent or receiver of the message are on SWIFT), then BIC is mandatory and other elements are optional.
- If instructing agent BIC is provided, then all other fields are optional.

[Instructed Agent](#)

This role identifies the agent that has been instructed in the payment chain to process the payment. The agent can be considered as the receiver of the payment message. This is not a static role, it changes as and when the payment is redirected.

While capturing an outgoing payment, the system provides option to enter the following details for the instructed agent:

| Field | Description |
| --- | --- |
| *BIC* | Indicates the Receiver/Instructed agent BIC |
| *Clearing System ID* | Indicates the ISO clearing system identification |
| *Clearing Member ID* | Indicates the National clearing code/member identification |

For TARGET2 payments, only BIC is sufficient to route the payment. Hence, if BIC is provided, then other fields are not required. When BIC is not provided, then both Clearing System ID and Clearing Member ID fields must be provided together so that the system can fetch and populate the corresponding BIC.

The system populates the determined receiver BIC in the generated message as instructed agent (from RECVER role). Other optional fields are not mapped. When the user opens CBPR+ payments for repair, the instructed agent details are displayed. The fields which are displayed for instructed agent in view and repair screen are same as in the capture screen mentioned above. Modification of instructed agent is allowed.

Rules for capturing the instructed agent details are as follows:

- When the transaction is exchanged on the SWIFT network (that is, if the instructing agent/sender and instructed agent/receiver of the message are on SWIFT), then BIC is mandatory and other elements are optional. If instructing agent BIC is provided, then all other fields are optional.

[Debtor Agent](#)

This role indicates the agent that service the account of the debtor. This is a static role and remains unchanged in the entire payment chain.

For outgoing payment, the processing company is considered as the debtor agent.

For TARGET2 payments, only BIC is sufficient. Hence, if BIC is provided, then other fields are not required.

When an incoming TARGET2 payment is received, the debtor agent details are stored in the system. If the payment is redirected, the received debtor agent details are mapped in the redirected message. The ORDINS role is used to store and map debtor agent details.

When the user opens a TARGET2 payment for view or repair, the debtor agent details are displayed if present. Modification of debtor agent is not allowed. The system displays following details for debtor agent.

| Details | Description |
| --- | --- |
| BIC | Indicates the debtor agent BIC |
| Clearing System ID | Indicates the ISO clearing system identification |
| Clearing Member ID | Indicates the national clearing code/member identification |
| LEI | Indicates the Legal Entity Identifier (LEI) of the debtor agent |
| Structured Address | The following three fields of structured address of the debtor agent can be captured:   - *Town Name* - *Country Code* - *Post Code* |
| Unstructured address line | The user can enter a maximum of three lines of unstructured address, each line can hold a maximum of 35 characters. |
| Account | Indicates the debtor agent account. |

- Due to the co-existence of MT and MX format, unstructured address elements are also supported in CBPR+ format (for scenarios when the payment is initiated in SWIFT FIN and redirected as MX message).
- SWIFT recommends to use structured information when payments are initiated in MX.

Rules for capturing the debtor agent details are as follows:

- If debtor agent BIC is provided, then all other fields are optional.
- If debtor agent LEI is provided, then it must adhere to the LEI format.
- If address is provided, the user must provide structured address, unstructured address, or Hybrid Address. Read [Support for Hybrid Address](#Hybrid) for more details on Hybrid Addresses.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- Name and address must be provided together.

[Creditor Agent](#)

This role indicates the agent that services the account of the creditor (beneficiary). The creditor could be a customer account for customer transfer or financial instruction account for bank transfer. This is a static role and remains unchanged in the entire payment chain.

While capturing an outgoing payment using the OE screen, the system provides option to enter the following details for creditor agent:

| Details | Description |
| --- | --- |
| BIC | Indicates the creditor agent BIC. |
| Clearing System ID | Indicates the ISO clearing system identification. |
| Clearing Member ID | Indicates the national clearing code/member identification. |
| LEI | Indicates the Legal Entity Identifier of the creditor agent. |
| Structured Address | The following three fields of the structured address of the creditor agent can be captured:   - *Town Name* - *Country Code* - *Post Code* |
| Unstructured address line | The user can enter a maximum of three lines of unstructured address, and each line can hold a maximum of 35 characters. |
| Account | Indicates the creditor agent account. |

For TARGET2 payments, only BIC is sufficient. Hence, if BIC is provided, then other fields are not required.

For outgoing and redirected payments, the system populates creditor agent BIC determined by Routing & Settlement (from ACWINS role). R&S does not support payment routing based on LEI.

When an incoming TARGET2 payment is received, the creditor agent details are stored in the system. If the payment is redirected, the received creditor agent details are mapped in the redirected message. Role ACWINS is used to store and map creditor agent details.

When the user opens a TARGET2 payment for repair, the creditor agent details are displayed. The fields which are displayed for creditor agent in view and repair screen are same as in the capture screen mentioned above. Modification of creditor agent is allowed.

- This is similar to the account with institution (tag 57) in SWIFT MT message.
- Because of co-existence of MT and MX format, unstructured address elements are also supported in CBPR+ format (for scenarios when the payment is initiated in SWIFT FIN and redirected as MX message).
- SWIFT recommends to use structured information when payments are initiated in MX.

Rules for capturing the creditor agent details are as follows:

- If creditor agent BIC is provided, then all other fields are optional.
- If creditor agent LEI is provided, then it must adhere to the LEI format.
- If address is provided, the user must provide structured address, unstructured address, or Hybrid Address. Read [Support for Hybrid Address](#Hybrid) for more details on Hybrid Addresses.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- Name and address must be provided together.

When structured and unstructured address details are available, then preference is given to structured address details in the outgoing message. If both *Town Name* and Country details are available, then populate structured address else unstructured address is populated in outgoing message (if available).

[Previous Instructing Agent 1, 2 and 3](#)

This role identifies the previous agents, which have processed the payment, prior to the current agent. This role ensures when a payment is processed serially through multiple intermediary agents, all the previous agents are retained in the payment chain. This is useful when payment is returned (using pacs.004).

When a redirected payment is processed, R&S component determines and populates the previous instructing agent roles. TARGET2 allows maximum three previous instructing agent roles in the payment chain. For a redirected payment, the system supports population of upto three previous instructing agents (PRVINS, PRVIN2 and PRVIN3 roles).

For an outgoing payment, previous instructing agent is not populated in the generated message.

When an incoming TARGET2 payment is received, the previous instructing agent details are stored in system. If the payment is redirected, Routing & Settlement determines the swapped roles and generates previous instructing agent roles which are mapped in the redirected message.

When the user opens a TARGET2 payment for repair, the previous instructing agent 1, 2 and 3 details are displayed in the read-only mode. Modification of previous instructing agent details is not allowed. The system displays the following details for each previous instructing agent:

| Details | Description |
| --- | --- |
| BIC | Indicates the BIC of previous instructing agent |
| Clearing System ID | Indicates the ISO clearing system identification |
| Clearing Member ID | Indicates the national clearing code/member identification |
| LEI | Indicates the Legal Entity Identifier (LEI) of the previous instructing agent. |
| Structured Address | The following three fields of structured address of the previous instructing agent are displayed   - *Town Name* - *Country Code* - *Post Code* |
| Unstructured address line | The user can enter maximum three lines of unstructured address |
| Account | Indicates the previous instructing agent account. |

SWIFT MT format does not have any explicit tag to hold this information. However, optional provision is there in MT message to pass this information as part of tag 72 (Sender to Receiver Information) with code word ‘INS’ followed by the previous instructing agent BIC.

If incoming MT message is received with code word ’INS’ and BIC in Tag 72, and the payment is to be redirected in MX format, then the system performs an enrichment to populate the Previous Instructing Agent role.

Rules for capturing the previous instructing agent 1, 2 and 3 details are as follows:

- If BIC is provided, then all other fields are optional.
- If LEI is provided, then it must adhere to the LEI format.
- If address is provided, the user must provide structured address, unstructured address, or Hybrid Address. Read [Support for Hybrid Address](#Hybrid) for more details on Hybrid Addresses.
- If structured address is provided, then *Town Name* and *Country Code* fields are mandatory.
- Name and address must be provided together.
- If previous instructing agent 2 details are provided, then previous instructing agent 1 must be provided.
- If previous instructing agent 3 details are provided, then previous instructing agent 2 must be provided.

[Population of Previous Instructing Agent](#)

The following diagram illustrates the change of agent roles at different stages when the payment is processed by different agents.

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_1.png)

When acting as a redirecting agent, the system generates the previous instructing agent roles. The system ensures that maximum three previous instructing agents are populated while redirecting payments when the payment is sent through a MX based channel.

For a redirected MX payment, the system generates the previous instructing agents based on the following conditions:

- If previous instructing agent 1 is present, it remains as previous instructing agent 1

- If previous instructing agent 2 is present, it remains as generated previous instructing agent 2
- If previous instructing agent 1 is present, then the current instructing agent (sender of the payment instruction) becomes previous instructing agent 2. Previous instructing agent 1 remains unchanged.
- If previous instructing agent 1 and 2 are present, then the current instructing agent (sender of the payment instruction) becomes previous instructing agent 3. Previous instructing agent 1  and 2 remains unchanged.
- If previous instructing agent 1 is not present and the debtor agent is different from the instructing agent, then the instructing agent becomes previous instructing agent 1.

| Incoming Message | | | Redirected Message |
| --- | --- | --- | --- |
| Sender | Is Previous Instructing Agent Present | Is Debtor Agent present |  |
| Bank A | No | No | Sender Bank A becomes debtor agent in redirected message |
| Bank A | No | Yes | Sender Bank A becomes Previous Instructing Agent 1 in redirected message |
| Bank A | Previous Instructing Agent 1 Present | NA | Previous Instructing Agent 1 remains as it is Sender becomes Previous Instructing Agent 2 |
| Bank A | Previous Instructing Agent 1 and Previous Instructing Agent 2 Present | NA | Previous Instructing Agent 1 and 2 remains as it is Sender becomes Previous Instructing Agent 3 |
| Bank A | Previous Instructing Agent 1  And  Previous Instructing Agent 2  and  Previous Instructing Agent 3  Present | NA | Not Possible as maximum three previous instructing agents are allowed |

[Intermediary Agent 1, 2 and 3](#)

An intermediary is an agent which is between the debtor’s agent and creditor’s agent. When debtor agent and creditor agent does not have direct relationship, the payment may be sent serially through one or more intermediary agents to reach the creditor agent. The intermediary agents in the payment chain acts as redirecting agents. These are not static roles, they change as and when a payment is redirected.

When payment is processed, Routing & Settlement component determines the intermediary agents required to send the payment. TARGET2 allows maximum three intermediary agent roles in the payment chain. For outgoing and redirected payments, the system supports population of upto three intermediary agents (role INTINS, INTIN2 and INTIN3).

While capturing an outgoing payment using the `OE` screen, the system provides an option to enter the following details for intermediary agent 1, 2, and 3:

| Details | Description |
| --- | --- |
| BIC | Indicates the intermediary agent BIC |
| Clearing System ID | Indicates the ISO clearing system identification |
| Clearing Member ID | Indicates the national clearing code/member identification |
| LEI | Indicates the Legal Entity Identifier of the intermediary agent |
| Structured Address | The following three fields of structured address of the intermediary agent can be captured   - *Town Name* - *Country Code* - *Post Code* |
| Unstructured address line | The user can enter a maximum of three lines of unstructured address and each line can hold a maximum of 35 characters |
| Account | Indicates the intermediary agent account |

Normally for international payments, BIC is sufficient to route the payment. Hence, if BIC is provided, then other fields are not required.

If clearing system details are provided, then both Clearing System ID and Clearing Member ID fields must be provided together.

For an outgoing and redirected payment, Routing & Settlement determines the intermediary agents and then mapped in the generated message. R&S does not support payment routing based on LEI.

When an incoming TARGET2 payment is received, the intermediary agent details are stored in system. If the payment is redirected, R&S components determines the swapped roles and the regenerated intermediary details are mapped in the redirected message.

When the user opens a TARGET2 payment for repair, the intermediary agent 1, 2 and 3 details are displayed. The fields which are displayed for each intermediary agent in view and repair are same as in the capture screen. The system allows the user to modify the intermediary agent details.

- SWIFT MT format supports only one intermediary role using Tag 56. However optional provision is there in MT message to pass additional intermediary agent details as part of Tag 72 (Sender to Receiver Information) with code word ’INT’ followed by the previous instructing agent BIC.
- If incoming MT message is received with code word ’INT’ and BIC in Tag 72, it is not treated as an intermediary agent in system. It is saved like a code word like any other details of Tag 72.

Rules for capturing the intermediary agent 1, 2 and 3 details are as follows:

- If BIC is provided, then all other fields are optional.
- If LEI is provided, then it must adhere to the LEI format.
- If address is provided, the user must provide structured address, unstructured address, or Hybrid Address. Read [Support for Hybrid Address](#Hybrid) for more details on Hybrid Addresses.
- If structured address is provided, then *Town Name* and *Country Code* fields are mandatory.
- Name and address must be provided together.
- If Intermediary agent 1 account is entered, other details (like BIC, clearing identification and so on) should also be provided
- If Intermediary agent 2 account is entered, other details (like BIC, clearing identification and so on) should also be provided
- If Intermediary agent 2 details are provided, then Intermediary agent 1 must be provided
- If Intermediary agent 3 account is entered, other details (like BIC, clearing identification and so on) should also be provided
- If Intermediary agent 3 details are provided, then Intermediary agent 2 must be provided

[Message Identification](#)

This is a point-to-point reference, as assigned by the instructing party and sent to the next party in the chain to unambiguously identify the message. When the message is received and redirected, every agent generates a unique new Message Identification. This is a mandatory information.

The system supports population of message id in outgoing and redirected payments. For payments, bulk reference id is assigned as the message identification.

As per TARGET2 specification, message identification is populated as ‘NONREF’ in payment messages.

[Settlement Method](#)

It indicates the method used to settle the payment instruction. This is a mandatory information.

For TARGET2 payment messages, settlement method is always populated as ‘CLRG’.

[Clearing System Code](#)

It indicates the channel through which the payment instruction is processed. This is a mandatory information.

For TARGET2 payment messages, clearing system code is always populated as ‘TGT’.

[Instruction Identification](#)

The instruction identification is a point-to-point reference that can be used between the instructing agent and the instructed agent to refer to the individual instruction. This is a mandatory information.

Since this is a point-to-point reference in a redirected payment, the received instruction identification is not passed, and a new value is assigned.

For payments, the system assigns the generated FTNumber as the instruction identification for outgoing and redirected payments.

Instruction identification must not start or end with a slash '/' and must not contain two consecutive slashes '//'.

[End To End Identification](#)

Identification as assigned by the initiating party, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire payment chain. This is a mandatory information.

While capturing a payment, if end-to-end identification is provided, the same value is populated in the outgoing message. Otherwise the fixed value, NOTPROVIDED is populated.

For a redirected payment, the system populates the same value as received.

[Transaction Identification](#)

Identification as assigned by the first instructing agent, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire interbank chain. This is not supported by TARGET2.

[Unique End to End Reference (UETR)](#)

Unique End to End Reference (UETR) is a universal unique identifier to provide an end-to-end reference of a payment transaction. This is a mandatory information.

The system supports generation of UETR for outgoing payments captured in the system.

For a redirected payment, the system populates the UETR as received.

[Instruction Priority](#)

Instruction Priority is an indicator of the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the instruction. This is an optional information.

This field allows the following values for instruction priority:

| Value | Description |
| --- | --- |
| NORM | Indicates that the priority level is normal |
| HIGH | Indicates that the priority level is high |

The system supports the capture and population of instruction priority as mentioned below –

- When a payment is captured using payment order, the user can specify the message priority as NORM or HIGH
- When a payment is captured or repaired using order entry, the user can specify the message priority as a numerical value (from 1 to 9)
  - value greater than 5 is mapped as HIGH
  - value blank or less than or equal to 5 is mapped as NORM

The priority is passed as received (or the modified priority if changed) for a redirected payment.

[Settlement Priority](#)

The Settlement Priority indicates the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the settlement instruction. This is an optional information.

The following are the values allowed for settlement priority:

| Value | Description |
| --- | --- |
| NORM | Indicates that the priority level is normal |
| HIGH | Indicates that the priority level is high |
| URGT | Indicates that the priority level is urgent (highest priority possible)  Allowed for Bank Transfer only. |

The system supports capturing of settlement priority when outgoing payment is initiated using the PO screen or OE screen. There is no specific processing done in the system for this information.

For a redirected payment, the settlement priority is passed as received.

[Service Level](#)

This indicates agreement under which or rules under which the transaction should be processed. Service level can be provided in coded or proprietary form. SWIFT recommends to use the coded form.

This is an optional information and if provided maximum three occurrences of service level is mapped (which could be combination of codes and proprietary form).

Service Level / Code is also used to transport the GPI (Global Payments Innovation) Service Identifier. Hence when an outgoing or redirected message is generated, the system checks if the bank is GPI enabled (configured in company properties). If the bank is GPI enabled, then the system automatically adds ‘G001’ as the service level:

- Customer Transfer (pcs.008)
- Bank Transfer Cover (pacs.009 COV)

Therefore users should not select G001 service level code while capturing payments, whereas it is automatically added in the generated message. GPI identifier is not added for any other outgoing or redirected messages except the two mentioned above.

When coded form is used, the code should be a valid one as per ExternalServiceLevel1Code list. This information is available at [External code sets | ISO20022](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets).

When the user captures the payment using PO screen or OE screen, dropdown fields lists the service level codes. The user can select the appropriate service level code from the dropdown. No separate validation is done on the applicable codes.

When this field is received in an incoming message, the service level details are stored in the system like code word, as follows:

- Information code = INSBNK
- Code word = SVCLVL (code) or SVCLVLPY (proprietary)
- Code word text = <the code or proprietary value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if configured for outbound code word generation.

When an incoming customer transfer (pacs.008) is processed, all received service level codes except ‘G001’ is stored as mentioned above. If the system receives ‘G001’ as service level code, it is updated as ‘001’ in the *ServiceTypeIdentifier* field (of POR.SUPPLEMENTARY.INFO).

[Local Instrument](#)

This indicates a user community specific instrument. Local instrument can be provided in coded or proprietary form. SWIFT recommends to use the coded form. This is an optional information.

When using a coded form, the code should be a valid one as per the ExternalLocalInstrument1Code list. This information is available at [External code sets | ISO20022](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets).

When the user captures a payment using the PO or OE screen, dropdown fields, which lists the local instrument codes, are provided. The user can select the appropriate local instrument code from the dropdown. No separate validation is done on the applicable codes.

When this field is received in an incoming message, the local instrument details are stored in the system as code words:

- Information code = INSBNK
- Code word = LCLINSCD (code) or LCLINSPY (proprietary)
- Code word text = <the code or proprietary value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

The received information is passed as it is in a redirected payment.

[Category Purpose](#)

The Category Purpose specifies the high-level purpose of the payment instruction based on a set of pre-defined categories. Category purpose can be provided in coded or proprietary form. SWIFT recommends to use the coded form. This is an optional information.

When the coded form is used, the code should be a valid one as per the ExternalCategoryPurpose1Code list. This information is available at [External code sets | ISO20022](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets)

When the user captures the payment using the PO screen or OE screen, dropdown fields, which lists the category purpose codes, are provided. The user can select the appropriate category purpose code from the dropdown. Separate validation is not done on the applicable codes.

When this field is received in an incoming message, the category purpose details are stored in the system as code words:

- Information code = INSBNK
- Code word = CYPURPCD (code) or CYPURPPY (proprietary)
- Code word text = <the code or proprietary value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if configured for outbound code word generation.

[Settlement Time Indication](#)

This provides the information on the occurred settlement time of the payment transaction. This is an optional information. This is not relevant for outgoing payment capture and received in incoming message from TARGET2.

When this field is received in an incoming message, settlement time indication fields are stored in the system as code words:

- Information code = TIMIND

- Code word = DBTTIME or CDTTIME
- Code word text = <time value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if applicable.

The system supports the following Settlement Time Indication fields.

| Field | Description |
| --- | --- |
| *Debit Date Time* | Specifies date and time at which the payment is debited at the transaction administrator. The date and time is defined with UTC offset (YYYY-MM-DDThh:mm:ss.sss+/-hh:mm).  For TARGET2, it indicates the date and time at which the payment is processed and debited at the central bank |
| *Credit Date Time* | Specifies date and time at which the payment is credited at the transaction administrator. The date and time is defined with UTC offset (YYYY-MM-DDThh:mm:ss.sss+/-hh:mm).  For TARGET2, it indicates the date and time at which the payment is processed and credited at the central bank |

[Settlement Time Request](#)

The user can provide information on the requested settlement time(s) of the payment instruction. The system supports to capture the following settlement time indication fields and sends in the generated message.

The user should enter the data in the settlement time request fields using format HH:MM:SS+/-hh:mm

(HH – hour, MM – minute, SS – second, +/- hh:mm indicates offset in hour and minute).

The user should enter the offset while capturing the details, otherwise the system considers offset as +00:00.

- If time is entered as HH:MM+/-hh:mm, the system considers the time as HH:MM:00+/-hh:mm and processes further
- If time is entered as HH:MM, then systems consider the time as hh:mm:00+00:00 and processes further.
- If time is entered as HH:MM+/-, then systems consider the time as hh:mm:00+/-00:00 and processes further.

When this field is received in an incoming message, the time settlement and time indication fields are stored in system as code words:

- Information code = TIMIND

- Code word = TILLTIME or FROMTIME or RJCTTIME
- Code word text = <time value received>

There is no specific validation or processing done in system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed as received if configured for outbound code word generation.

The system supports the following fields in the Settlement Time Request field.

| Field | Description |
| --- | --- |
| *Till Time* | Indicates the time until when the payment may be settled |
| *From Time* | Indicates the time from when the payment may be settled |
| *Reject Time* | Indicates the time by when the payment must be settled to avoid rejection. |

[Instruction for Creditor Agent](#)

This specifies further information related to processing of the payment instruction, provided by the initiating party and intended for the creditor agent. This is an optional information consisting of instruction code and information.

Following are the allowed values for instruction code:

| Value | Description |
| --- | --- |
| CHQB | Pay Creditor By Cheque ((Ultimate) creditor must be paid by cheque.) |
| HOLD | Hold Cash For Creditor (Amount of money must be held for the (ultimate) creditor, who will call. Pay on identification.) |
| PHOB | Phone Beneficiary (Please advise/contact (ultimate) creditor/claimant by phone.) |
| TELB | Telecom (Please advise/contact (ultimate) creditor/claimant by the most efficient means of telecommunication) |

If the user selects a code, additional information can be provided using the information field, such as the phone number of beneficiary and so on.

The user can enter additional information without a code or receive only additional information in the incoming message without a code.

When only additional information text is captured or received, the system defaults the instruction code as IFCA, for storing it internally in TPH. The default code IFCA is not displayed when the payment is viewed in TPH ISO capture, View or Repair screens and also IFCA is not mapped in the outgoing message.

If the payment is opened using the non-ISO Order Entry screens to view or repair, then default code IFCA is visible along with the information text. However, this is not mapped in outgoing message.

For customer payment, all the above mentioned codes are allowed. For bank transfer, CHQB and HOLD are not allowed.

Maximum two occurrences of instruction for creditor agent are mapped.

- If the user enters the CHQB Instruction Code, then HOLD is not allowed
- If the user enters the PHQB Instruction Code, then TELB is not allowed

When a payment is captured using the PO screen or OE screen, dropdown fields, which lists the instruction codes, are provided. The user can select the appropriate instruction code from the dropdown and enter additional information.

When this field is received in an incoming message, the instruction for creditor agent details are stored in system as code words:

- Information code = INSBNK
- Code word = <received instruction code>
- Code word text = <received instruction information>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if configured for outbound code word generation.

[Instruction for Next Agent](#)

Specifies further information related to processing of the payment instruction, which may need to be acted upon by the next agent. This is an optional information consisting of only textual information (no code).

A maximum four occurrences of Instruction for Next agent is mapped.

When the user captures a payment using the PO screen or OE screen, user can capture this information.

Instruction of Next Agent will no longer be sent out to TARGET2 in an outgoing message as the support is withdrawn since NOV.2025. Likewise, TARGET2 will no longer include this information in incoming messages post this deadline.

In a redirected payment the received information is passed if configured for outbound code word generation.

[Purpose](#)

Specifies the underlying reason for the transaction. It is used by the end-customers such as initiating party, (ultimate) debtor, (ultimate) creditor to provide information on reason of the transaction. It is not used for processing by any of the agents involved in the payment chain. This is an optional information.

The user can provide the purpose in coded or proprietary form. SWIFT recommends to use the coded form.

When the user uses the coded form, the code should be a valid one as per the ExternalPurpose1Code list. This information is available at [External code sets | ISO20022](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets)

When payment is captured using the `PO` application or OE screen, dropdown fields, which lists the purpose codes, are provided. The user can select the appropriate purpose code from the dropdown. No separate validation is done on the applicable codes.

When this field is received in an incoming message, the purpose details are stored in the system as code words:

- Information code = INSBNK
- Code word = TXPURPCD (code) or TXPURPPY (proprietary)
- Code word text = <the code or proprietary value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed as it is.

[Regulatory Reporting](#)

Specifies the information required for regulatory and statutory requirements. This is an optional information.

While the user initiates a payment using the `PO` application or OE screen, the system supports capturing regulatory information which comprises of the following:

- Debit Credit Reporting Indicator – This is a coded information which identifies whether the regulatory information applies to debit side, credit side, or both side of the transaction. Allowed values are:
  - BOTH - Regulatory information applies to both credit and debit sides
  - CRED - Regulatory information applies to the credit side
  - DEBT - Regulatory information applies to the debit side
- Authority – Indicates the entity that requires the regulatory reporting information
  - Name
  - Country
- Details – Provides details on the regulatory reporting information. Multiple occurrence sare allowed. It consists of the following fields
  - Type
  - Date
  - Country
  - Code
  - Amount
  - Information (multiple occurrence)

When an incoming payment is received with regulatory reporting information, the details are stored in the system. If the payment is redirected, the received regulatory reporting information is passed unchanged.

There is no specific validation or processing done in the system for this information.

In ISO20022 format message processing, regulatory reporting details is not considered as code word.

This is similar to regulatory reporting Tag 77B of MT message. In MT message, the details are very limited whereas in ISO20022 format the details are more with multiple repeating values.

[Related Remittance Information](#)

This provides information related to the handling of the remittance information by any of the agents in the transaction processing chain. This is an optional information.

The system does not provide option to capture related remittance information while capturing payments using the PO screen or OE screen. This information is not displayed in view or repair screens.

However, if this information is received in incoming message, the same is stored in the system. For a redirected payment the received information is passed unchanged.

There is no equivalent field in MT message.

Rule for capturing the related remittance information are as follows:

- Either Related remittance Information element or Remittance Information element should be used. Do not use both the elements.

[Remittance Information](#)

Information supplied to enable the matching of an entry with the items that the transfer is intended to settle, such as commercial invoices in an accounts' receivable system. This is an optional information.

Remittance Information can be provided in one of the following two forms:

- Unstructured – This is similar to remittance information Tag 70 in MT message. The data is limited to 140 characters and not structured. Only one occurrence of unstructured information is allowed.
- Structured – The structured remittance information contains several fields to provide remittance details which can be used for automated matching (outside payment system). Multiple occurrence of unstructured information is possible. The structured remittance information is divided into following high level groups:
  - Referred Document Information – Provides identification and content of the referred document. It consists of multiple child elements.
  - Referred Document Amount – Provides details on the amount of the referred document. It consists of multiple child elements.
  - Creditor Reference Information – Reference information provided by the creditor to allow the identification of the underlying document. It consists of multiple child elements.
  - Invoicer – Identification of the organization issuing the invoice, when it is different from the creditor or ultimate creditor. It consists of multiple child elements.
  - Invoicee – Identification of the party to which an invoice is issued, when it is different from debtor or ultimate debtor. It consists of multiple child elements.
  - Tax Remittance – Provides remittance information about a payment made for tax related purpose. It consists of multiple child elements.
  - Garnishment Remittance – Provides remittance information about a payment made for garnishment related purpose
  - Additional Remittance Information – Additional information, in free text form, to complement the structured remittance information

As structured remittance information is vast, all fields are not used for manual capture while initiating payments. Proper structured remittance information is mostly generated in other external system and provided in the form of pain.001 message. Hence, the system provides the following options:

- Limited number of fields are exposed in the `PO` application and OE screen for manual capture of structured remittance information.
- When structured remittance information is received in a pain.001 (v9) message or in an incoming SWIFT ISO20022 format payment, the system stores the entire details in the XML format. While redirecting the payment, the received XML is passed as it is without any modification.
- The system does not allow modification of structured remittance information in repair mode
- In view or repair mode, received remittance information is displayed in the XML format
- Since the entire structured remittance information is stored as XML, the system does not perform any validation on individual elements of the data

While initiating a payment using the `PO` application or OE screen, the system provides the following fields of structured remittance information for manual capture:

- Referred Document Info Type Code
- Referred Document Info Number
- Referred Document Amount Remitted Amount Currency
- Referred Document Amount Remitted Amount Currency
- Referred Document Amount Credit Note Amount Currency
- Referred Document Amount Credit Note Amount
- Creditor Reference Information Type Code
- Creditor Reference Information Type Prop
- Creditor Reference Information Type Issuer
- Creditor Reference Number
- Additional Remittance Information

Rules for capturing the remittance information are as follows:

- Either related remittance information element or remittance information element should be used. Do not use both the elements.
- When remittance information is used, either unstructured or structured information should be used. Do not use both the information.
- When structured remittance information is provided, total business data for all occurrences must not exceed 9000 characters.

[Charge Details](#)

The charge details are in ISO20022 format. The charges details is divided into charge bearer and charges information.

[Charge Bearer](#)

Specifies which party or agent bears the charges associated with processing of the payment. This is a mandatory information.

The system supports the following charge code processing:

| Charge Code | Description |
| --- | --- |
| CRED | The creditor borne all transaction charges (similar to charge code BEN) |
| DEBT | All transaction charges are to be borne by the debtor (similar to charge code OUR) |
| SHAR | Charges are shared. In a credit transfer context, the transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor. (similar to charge code SHA) |

SLEV (following service level) charge code is not supported in system. Hence this option is not provided in the PO screen and OE screen. If SLEV is received in an incoming message, the system saves it and treats as SHAR.

[Charges Information](#)

Provides information about the agents in the payment chain who have paid the charges or to whom charges are due. This is a mandatory information if charge is deducted and optional for initiator if charges are not deducted.

It consists of following two elements. If the user provides the charges information, then both these elements must be provided.

| Element | Description |
| --- | --- |
| Amount | Indicates the charge amount along with the currency. |
| Agent | Identifies the agent who has paid the charges or to which it is due. In ISO20022 format, charge agent can be represented using the following elements:   - BIC - LEI - Clearing System id and Clearing Member id - Name - Postal Address - structured or unstructured |

When outgoing payment is processed in the system and charges are deducted, the system populates the BIC of the charge agent only along with the charge amount and currency in the generated message.

When an incoming message is received, the system stored all the charge information. If the payment is redirected, the system populates the received charges information and then adds its own charges (BIC, amount and currency) for SHAR and CRED scenarios.

Charge bearer is similar to Tag 71A (details of charges) in MT message, which can have SHA/BEN/OUR as charge code.
Charges information is similar to 71F (sender’s charges) and 71G (receiver’s charges) in MT message.
In MT message, only charge amount and currency is specified and charge agent details are not specified. However in MX, charge agent is also required. Therefore, if an incoming MT message with charge is received and redirected as MX message, the charge agent Name and Address lines are populated as NOTPROVIDED.

## Supported Characters for ISO Message

RTGS ISO Clearings have not published their own requirements regarding the character set support. So, Temenos Payments Hub supports the characters set based on SWIFT CBPR+ guidelines for ISO messages. Read the [International\_Payments (CBPR+ ISO20022)](../../../../International_Payments/PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm) guide for more details on character conversion.

## Data Enrichment for MT and MX Format Conversion

TARGET2 is migrating from MT to MX format using big bank approach. Similarly SWIFT is also migrating from MT to MX format for cross border payments. SWIFT’s migration to MX (ISO20022) format is not following a big bang approach, there is co-existence of MT and MX format.

Banks should be able to receive and process incoming cross border payments in both MT as well as MX format. The system provides configurable option for a bank to decide whether they want to send cross border payments in either in MT format (that is, staying in MT format) or MX format (that is, migrating to MX format). When a bank sends outward messages (outgoing or redirected) following scenarios are possible:

- Receive an incoming cross border payment in MX format and redirect to TARGET2 in MX format
- Receive an incoming cross border payment in MT format and redirect to TARGET2 in MX format
- Receive an incoming payment in MX format from TARGET2 and redirect as a cross border payment through SWIFT using MX format
- Receive an incoming payment in MX format from TARGET2 and redirect as a cross border payment through SWIFT using MT format

The system provides the functionality to perform automatic enrichment of data for such scenarios.

Similarly, banks can receive TARGET2 or CBPR+ payment initiation request through pain.001 (v9) which is xml based. If the processed customer payment is to be routed as MT103 message through a SWIFT based channel, then the system performs enrichments so that proper MT message is generated.

These enrichments are performed as part of Routing and Settlement (R&S) when outgoing channel is being determined. Based on the incoming and outgoing channel formats system performed the data enrichments.

[Incoming MT Format and Outgoing MX Format](#)

The following section explains about the various data enrichments performed by the system when an incoming message is received in MT format (a SWIFT cross border payment or from a SWIFT MT Based PMI) and to be redirected in MX format.

The system supports the following MT to MX conversions

- MT 103 to pacs.008
- MT 101 to pacs.008
- MT 202 to pacs.009
- MT 202 COV to pacs.009 COV

In case of a cover message (MT 202 COV to pacs.009 COV), the sequence B data is transformed into pacs.009 COV underlying customer credit transfer block through mapping routine while the message is generated. No automatic enrichment is performed for this sequence B data.

Read the [Payment Direction](#Payment_Direction) section, where the conditions for these redirection format condition is mentioned.

[Name and Address Enrichment](#)

The system performs name and address enrichment for debtor (Tag 50) and creditor (Tag 59) as per PMPG guidelines. The same logic is applied even for agent roles (tag 52, 53, 54, 55, 56, 57) also.

[Structured SWIFT FIN (MT) to Unstructured MX](#)

When the system receives the incoming MT message with structured address in the party roles (Tag 50F and 59F), then it should be enriched to map to the unstructured address lines in MX message. Below snippet shows the sample enrichment.

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_2.png)

If LEI (Legal Entity identifier) is received for ordering customer and beneficiary customer, they are enrichment in the following way.

- Ordering Party - Field 50F: if LEI is received as 6/XY/LEIC/<LEI>, then it is mapped to LEI tag for Debtor role
- Beneficiary - Field 59F: if LEI is received as 3/XY/LEIC/<LEI>, then it is mapped to LEI tag for the creditor role

Here, XY indicates country code and /LEIC/ indicates that the following data is legal identifier code. All the data before the actual LEI is ignored while enriching.

If name and address data is truncated as part of conversion, a ‘+’ sign is added at the end of the data field to indicate truncation.

[Unstructured SWIFT FIN to Unstructured MX](#)

When incoming MT message is received with unstructured address in the party roles (Tag 50 and 59 without using F format), then it should be enriched to map to the unstructured address lines in MX message. Below snippet shows the sample enrichment.

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_3.png)

Apart from Debtor and Creditor, the above mentioned address format conversion is also applied for all the agent roles also.

[National Clearing Code (NCC) Enrichment](#)

If NCC is received in MT message for any agent, then system performs enrichment so that it can be mapped as clearing system identification and clearing member identification in MX format.

Incoming MT103 has NCC details as //SC123456. Then in the outgoing MX message, it should be populated with clearing system id as GBDSC and member id as 123456. Here SC is the two character code used for MT messages, GBDSC is the five characters ISO clearing system identification used in MX messages and // indicates NCC in MT format.

When the Reference Data (RD) module is installed, the system refers to the RD.CTRY.NAT.SYS.IDENTIFIER application to perform this NCC conversion.

If RD module is not installed, then the system refers to the ISO.CLEARING.SYSTEM.ID application where the details are maintained.

[Instruction Code (Tag 23E)](#)

If the following code words are received in Tag 23E of MT103, then the system performs the following enrichment by inserting new records so that these code words are mapped in the respective MX fields:

- INTC and CORT are enriched as Category Purpose Code
- OTHR is enriched as Category Purpose Proprietary
- CHQB,HOLD,PHOB,TELB enriched as Instruction for Creditor Agent
- SDVA is enriched as Service Level Code

Apart from the code words mentioned above, if any other code word is received in 23E, those are not enriched.

When these code word records are enriched, new records are inserted and received data is not deleted.

[Time Indication (Tag 13C)](#)

If the following code words are received in tag 13C, then system performs the following enrichment by inserting new records so that these code words can be mapped in the respective MX fields:

- CLSTIME (CLS Time) is enriched to be mapped to Settlement Time Request/CLS Time
- SNDTIME (Receive Time) is enriched to be mapped to Settlement Time Indication/Debit Date Time
- RNCTIME (Send Time) is enriched to be mapped to Settlement Time Indication/Credit Date Time

The MT time format is also converted into MX format in the enriched record.

When these code word records are enriched, new records are inserted and received data is not deleted.

[Transaction Type Code (26T)](#)

If transaction type code is received in Tag 26T, then the system inserts a new record so that it can be mapped to the *Transaction Purpose Proprietary* field of the respective MX message.

When these code word records are enriched, new records are inserted and received data is not deleted.

[Remittance Information (Tag 70)](#)

If remittance information is received in Tag 70, then it is mapped to *Unstructured Remittance Information* field of respective MX message.

If Tag 70 contains /ROC/, then the subsequent content is populated as Customer Specified Reference (so that it can be mapped as End to End identification).

If Tag 70 contains /ROC/INFORMATION1234, then enrichment is done to populate a new record as shown below.

POR.Transaction > CustomerSpecifiedReference = INFORMATION1234

[Sender to Receiver Information (Tag 72)](#)

Information received in Tag 72 is enriched as mentioned below.

- For each occurrence of /INS/<BIC>, system creates a new record for previous instructing agent role and maps the BIC (maximum 3 roles are populated)
- Remaining details of Tag 72 are mapped to Instruction for Next Agent field in MX message

[Charge Details (Tag 71A, 71F/G)](#)

The system enriches/maps the charge details received in the incoming MT message as mentioned below:

- Charge code (Tag 71A) mapping

SHA is mapped as SHAR

BEN is mapped as CRED

OUR is mapped as DEBT

- Charge Agent mapping

If one or more charge details are received (Tag 71G or 71F), then a new corresponding record is inserted for each charge details to populate the charge agent role:

If charge code = SHA or BEN, then a charge agent record is added with received amount and currency. Name and Unstructured address lines are saved as ‘NOTPROVIDED’ (Since charge agent details are not available in tag 71).

[Regulatory Reporting (Tag 77B)](#)

If the regulatory reporting details is received in Tag 77B, then the system inserts a new record to create a regulatory reporting record as per MX format as mentioned below:

- ORDERRES is mapped as DEBT
- BENEFRES is mapped as CRED
- Country code is mapped as Country code
- Information after code word is mapped as Information Line (removing //).

[Incoming MX Format and Outgoing MT Format](#)

The following section explains about the various data enrichments performed by system when an incoming message is received in MX format (a SWIFT cross border payment or from a SWIFT Based Payment Market Infrastructure (PMI)) and to be redirected in MT format.

The system supports the following MX to MT conversions

- pacs.008 to MT 103
- pacs.009 to MT 202
- pacs.009 COV to MT 202 COV
- pain.001 to MT 103

In case of a cover message (pacs.009 COV to MT 202 COV), the underlying customer credit transfer information is transformed into sequence B through mapping routine while the message is generated. No automatic enrichment is performed for this sequence B data.

Read the [Payment Direction](#Payment_Direction) section, where the conditions for these redirection format condition is mentioned.

[Name and Address Enrichment](#)

The system performs name and address enrichment for debtor (Tag 50) and creditor (Tag 59) as per PMPG guidelines. The same logic is applied even for agent roles (tag 52, 53, 54, 55, 56, 57) also.

[Structured MX to Structured MT](#)

When the incoming MX message is received with name and structured address, then the system performs the following enrichments so that name and structured address are properly mapped in MT message.

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_4.png)

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_5.png)

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_6.png)

- If BIC is not present, then enrich the XML name and address elements into corresponding F option (if supported by the MT tag). Use comma (‘,’ without space) as a delimiter to separate various available data elements in the sub-fields 2/… (address) and 3/XY/… (town).
- If LEI is present, do not use the second line for name, truncate if needed using the ‘+’ sign as the last character. Truncate any other line the same way. Enrichment rules for LEI element are as follows:
  - Place LEI on last line of 50F or 59F, if space allows.
  - For 50F, insert a 6/XY/LEIC/ followed by the actual LEI. XY is the country code of the debtor.
  - For 59F, insert a 3/XY/LEIC/ followed by the accrual LEI. XY is the country code of the creditor.
- If LEI not present, use two lines for the name and truncate any other line, indicating truncation with the + character.
- If there is no LEI and single line name, then use two lines for the *Country*, and *Town* fields and so on.
- If there is no second line for any other field, use two lines for the *Street* and *Building* fields.

[Unstructured MX to Structured MT](#)

If name and unstructured address is received, the system performs the following enrichments to map the data as structured name and address in the MT message.

If all occurrences of the unstructured address line starts with a SWIFT FIN qualifier, such as 2/ (up to two occurrences allowed) or 3/, then F format should be created for Tag 50 and 59. The mapping of the fields should be as follows:

- Name: Enrich the Nm element (Name) so that it gets mapped as line 1 in MT field 50 / 59 with option F with the prefix ‘1/’ at the beginning of the line
- Address: Enrich all occurrences of the unstructured AdrLine element to the residual lines of MT field 50 / 59 using option F preserving the prefix (2/, 3/)

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_7.png)

This same enrichment as mentioned above is applicable for the address line starting with 4/, 5/, 6/, 7/, 8/.

[Unstructured MX to Unstructured MT](#)

If the system receives name and unstructured address in the incoming MX message, then the system performs the following enrichments so that these can be mapped as unstructured address in the MT message.

For this scenario all the unstructured address lines in the MX message does not start with 1/ or 2/ or 3/.

- Name: Map the Nm element (Name) to line 1 of the MT field 50 (with K letter option)  / field 59 (No letter option)
- Address: Map all occurrences of AdrLine elements to the residual lines of the MT FIN field 50 / 59

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_8.png)

[National Clearing Code (NCC) Enrichment](#)

If the system receives the clearing system identification and clearing member identification in the MX message for any agent, then the system enriches the data in the equivalent MT format and populates in the account line.

Incoming pacs.008 has clearing system id as ‘GBDSC’ and member id as ‘123456’ for an agent. Then in the MT outgoing message, if NCC details is sent out, it should be populated as ‘//SC123456’. Here ‘SC’ is the two character code used for MT messages, ‘GBDSC is the five characters ISO clearing system identification used in MX messages and ’//’ indicates NCC in MT format.

When the Reference Data module (RD) is installed, the system refers the Country National System Identifiers (RD.CTRY.NAT.SYS.IDENTIFIER) application to perform the NCC conversion.

If the RD module is not installed, then the system refers to the ISO.CLEARING.SYSTEM.ID application where the details should be maintained.

[Instruction Code (Tag 23E)](#)

If the following code words are received in various XML tags of the incoming MX message, then the system performs the following enrichment by inserting new records so that these code words are mapped in the respective MT fields:

- Category Purpose Code - INTC and CORT are enriched so that it gets mapped to 23E
- Category Purpose Proprietary - OTHR are enriched so that it gets mapped to 23E
- Instruction for Creditor Agent - CHQB,HOLD,PHOB,TELB are enriched so that it gets mapped to 23E
- Service Level Code - SDVA is enriched as 23E

Apart from the code words mentioned above, if the system receives any other code word in various MX tags, those codes are not enriched for mapping in 23E.

When these code word records are enriched, new records are inserted and received data is not deleted.

[Time Indication (13C)](#)

If settlement time indication related XML tags are received in MX message, then the system performs following enrichments by inserting new records so that these code words can be mapped in the respective MT fields:

- Debit Time (DBTTIME) is enriched as SNDTIME
- Credit Time (CDTTIME) is enriched as RNCTIME

The MX time format is also converted into MT format in the enriched record.

When these code word records are enriched, new records are inserted and received data is not deleted.

[Remittance Information (Tag 70)](#)

The system performs the following enrichments by inserting new record with information code RMTINF so that Tag 70 is populated as mentioned below:

- If the system receives the Ultimate Debtor information, then it is mapped as /ULTD/<ConditionalData>

For /ULTD/, < ConditionalData> is derived as mentioned below:

```
If NAME is present
{
If both TOWN.NAME and COUNTRY are present then
            ConditionalData = /ULTD/NAME/COUNTRY/ TOWN.NAME
        Else if ORGANISATION IDENTIFICATION à OTHER IDENTIFICATION is present then
            ConditionalData = /ULTD/NAME/ORG.ID.OTHER.ID
        Else
            ConditionalData = /ULTD/NAME
}
Else (means NAME is absent)
{
if ORGANISATION IDENTIFICATION à OTHER IDENTIFICATION is present then
ConditionalData = /ULTD/ ORG.ID.OTHER.ID
Else
ConditionalData = Empty (Do not populate any record with RMTIF and /ULTD/
combination if DerivedData is empty.
}
```

Copy

- If the system receives the Ultimate Creditor information, then it is mapped as /ULTB/<ConditionalData>.

The conditional data logic mentioned above holds for /ULTB/ as well.

- If the system receives the Purpose code or proprietary, then the received purpose code is mapped as PURP/<received value>.
- If the system receives the end-to-end identification, then the received end to end id is mapped as /ROC/<received value> (if it is not equal to NOTPROVIDED).
- If the system receives the related remittance information, then it is mapped as /RELID/<first related remittance identification>.
- If the system receives the structured remittance information, then it is mapped as /SRI/+ (that is, the structured remittance information is present in the original message but it is not translated).

[Sender to Receiver Information (Tag 72)](#)

The system performs the following enrichments by inserting new record with information code INSSDR, so that Tag 72 is populated as mentioned below:

- If 2nd Intermediary Agent is available, then it is mapped as /INTA/<BIC of Intermediary 2>
- If second intermediary agent is available, then it is mapped as /INTA/<BIC of Intermediary 2>.
- If third intermediary agent is available, then it is mapped as /INTA/<BIC of Intermediary 3>.
- If the Service Level code or proprietary is received, then the received purpose code is mapped as /SVCLVL/<received value> (except for service level code = SDVA or starting with G00).
- If the local instrument code or proprietary is received, then the received purpose code is mapped as /LOCINS/<received value>.
- If the category purpose code or proprietary is received, then the received purpose code is mapped as /CATPURP/<received value> (except for Category Purpose Code = CORT or INTC).
- If the instruction for next agent information is received, then the received information text is mapped as /REC/<received value>.
- If the Previous Instructing Agent 1 is available, then it is mapped as /INS/<Previous Instructing Agent 1BIC>.
- If the Previous Instructing Agent 2 is available, then it is mapped as /INS/<Previous Instructing Agent 2BIC>.
- If the Previous Instructing Agent 3 is available, then it is mapped as /INS/<Previous Instructing Agent 3BIC>.

If all the received information may not fit into Tag 72 of MT message (due to length and number of line limitation), some information may not get transmitted in the generated MT message.

[Regulatory Reporting (Tag 77B)](#)

- If the system receives the regulatory reporting details in the MX message, then the data is enriched so that it can be properly populated in Tag 77B of MT message.DEBT is mapped as ORDERRES
- CRED is mapped as BENEFRES
- Country code is mapped as Country code

Regulator Reporting Information is mapped as Information Line after code.

## Acknowledgements

Direct participant bank generates outward payment messages (in ISO20022 format), which is sent to TARGET2 using an appropriate SWIFT gateway (MX compliant). SWIFT InterAct is the messaging service used to send/receive ISO20022 XML format TARGET2 messages. When the system process a payment, generated TARGET2 messages are sent through the T24 delivery module.

SWIFT delivers the TARGET2 message to ESMIG layer, which performs technical validations. After completing the validation successfully, it delivers the message to RTGS. RTGS on processing the payment sends acknowledgement indicating whether the payment is success or failure.

The following diagram shows various possible acknowledgements corresponding to a TARGET2 customer payment sent as pacs.008 through SWIFT.

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_9.png)

1. Outward customer payment message (pacs.008) is generated in system and sent to TARGET2 through SWIFT. It could be other messages also such as Bank Transfer (pacs.009 Core and Cover), return Payment (pacs.004) and so on.
2. This is an acknowledgement sent by SWIFT (Network ACK) indicating if the message has been accepted or rejected (similar to the F21 technical acknowledgement response for SWIFT FIN against MT messages).
3. If the pacs.008 is accepted by SWIFT, then it delivers the message to ESMIG layer.
4. On successful delivery, SWIFT may receive a delivery notification (if requested and ESMIG can send). This is optional.
5. SWIFT forwards the positive delivery notification to the sender of the underlying message. Based on positive DLN, sender understands the outgoing message has been received by the receiver (which is ESMIG in this scenario).

If SWIFT is unable to deliver the message to receiver, it sends a negative delivery notification indicating delivery failure.

6. On receipt of the message from SWIFT, ESMIG performs technical validations. If the validation fails, then it rejects the message and sends admi.007 (receipt acknowledgement) negative acknowledgement.
7. SWIFT forwards the admi.007 negative acknowledgement to the sender of the underlying message.
8. If ESMIG layer validations are successful, then the received message is sent to RTGS. In such scenario ESMIG does not send any positive acknowledgement.
9. RTGS validates the message and tries to settle the payment. Based on settlement RTGS sends pacs.002 (payment status report) to indicate rejection or successful settlement.
10. SWIFT forwards the pacs.002 message to the sender of the underlying payment.

Payment Status Report (pacs.002) is considered as business acknowledgement in the system.

[](#)[Technical Acknowledgement](#)

When a TARGET2 payment is sent, the system can receive following technical acknowledgements

- Network ACK and Delivery Notifications (DLN) from SWIFT
- admi.007 (receipt acknowledgement) from ESMIG

If a separate client interface is used (for example, ESBs, other SWIFT gateways and so on) to send these messages to SWIFT (instead of the Delivery module sending through SWIFT Alliance), in that case the system may receive technical acknowledgements from the interface (Interface Ack) as well.

[SWIFT Acknowledgment Processing](#)

TARGET2 messages processed in the system are sent using the Delivery module. The Delivery layer updates the Business Application Header, Technical Header and sends the message through SWIFT Interact Service. A specific carrier is defined in Delivery to send/receive TARGET2 MX messages.

The delivery module supports sending MX messages through SWIFT Alliance standard interface using XMLv2 DataPDU format. The following technical acknowledgements from SWIFT can be received:

- Transmission Report for Network Ack/Nack
- SWIFT Alliance standard Delivery Report format for Delivery Notifications (this is optional if configured and supported by ESMIG)
  - xsys.010 for overdue warning
  - xsys.011 for positive delivery notification (when message is delivered)
  - xsys.012 for failed delivery notification (when message is not delivered)

The Delivery module provides the configurations at TARGET2 carrier level to define the technical acknowledgements applicable. Therefore, the bank users can configure

- if Network Acknowledgement is applicable
- if delivery notification is applicable

Failed delivery notification (xsys.012) is not configurable as SWIFT always sends this notification if the network could not deliver the message (max timeline is 14 days). If delivery notification (xsys.011) is configured, then the system may also receive overdue warning (xsys.010).

The Delivery module receives the technical acknowledgements against outward messages. The Delivery module uses a proprietary technical acknowledgement XML response format to send the details of these acknowledgements to TPH for further processing through a configured queue (the acknowledgement messages are not forwarded). TPH receives the following information sent in the proprietary acknowledgement response message:

| Information | Description |
| --- | --- |
| Response Class | Indicates the type of response – Interface, Network, DLN |
| Response Source | Indicates the originator of the response |
| Response Type | Indicates whether it is a Positive ack (0), Negative ack (1), or Warning (2) |
| Error Codes | Indicates the list of error codes and the related description from the acknowledgement |
| Original Transaction Reference | Indicates the transaction reference from the Delivery Outward Header |
| Original Bulk Reference | Indicates the original Bulk Reference (for example, Temenos Payments Hub Bulk Reference which is populated in message identification at group header in the outgoing message) from the delivery outward header |
| Original Message Type | Indicates the Message Type from the Delivery Outward Header |
| Original Request Ref | Indicates the Carrier sequence from the Deliver Outward Header |

On receipt of the technical acknowledgement details in the proprietary XML format, the system identifies the underlying outward message (from the PSM.BLOB table), for which this technical acknowledgement is received, using the Original Bulk Reference. The received acknowledgement response is saved in PSM.BLOB.

- The *AckNackMsgType* field is updated with Response Class
- The *AcknowledgementCode* field is updated with Response Type
- The *AckNackReason* field is updated with Error Codes
- The *AcknowledgementMessage* field is updated with the received proprietary XML response
- The *AcknowledgementAction* field is updated as PNDG (for negative ack) for non-payment messages

Based on the message type, the system identifies if the acknowledgement is for a payment message (such as pacs.008, pacs.009, pacs.004) or a non-payment message (such as camt.056, camt.029 and so on).

When negative SWIFT technical acknowledgement is received, the system does not perform any automatic action. The user can view all such outgoing messages using the 'SWIFT ISO Technical Exception' enquiry for manual action.

[ESMIG Acknowledgement Processing](#)

After receiving the payment message through SWIFT, the ESMIG layer performs technical validation. If the validation is not successful, the message is rejected and not forwarded to RTGS. A mandatory negative acknowledgement (admi.007) is sent to the sending participant bank. If the message is rejected by ESMIG, negative acknowledgement message is received against the outward payments (such as pacs.008, pacs.009, pacs.004) and non-payment messages (such as camt.056, camt.029) in case of any rejection by ESMIG admi.007 does not have a Business Application Header (BAH). TPH supports receiving and processing of admi.007 messages.

The system provides a configuration in Source Settings (Action on NACK field in PP.SOURCE) for automatic action on underlying payment, if admi.007 rejection is received against an outward TARGET2 payment. If this is configured, then the system automatically cancels the outgoing payment and accounting entries are reversed. When the outgoing message is a child of a batch transaction (*Batch Indicator* –‘true’), and the reversal of the account is successful, TPH creates a new RJ transaction for the outgoing transaction amount to debit the Batch Suspense account and to credit the Debtor of the original bulk transaction (reversal accounting entries of the batch parent transaction). If not configured, then all such outgoing TARGET2 messages rejected through admi.007 can be viewed using the RTGS Technical Exception enquiry for manual action.

For non-payment messages (such as camt.056, camt.029) processing of admi.007 is automatic irrespective of the above configuration. The corresponding case management status in EB Queries and Answers (EBQA is updated as clearing rejected.

[Manual Processing of Negative Technical Acknowledgement](#)

As mentioned above, the system receives technical acknowledgements from SWIFT and ESMIG against messages sent to TARGET2. The user can view all such messages that have received negative technical acknowledgement and pending for manual action using the ‘RTGS Technical Exception’ enquiry. It is mandatory to enter the channel as TGT to filter the TARGET2 specific record. The enquiry displays the following TARGET2 messages:

- Payment messages (such as pacs.008, pacs.009, pacs.009 cover, pacs.004)
  - which are waiting for acknowledgement
  - NACK has been received
  - message waiting for DLN
  - negative DLN has been received
- Non-payment messages (such as camt.056, camt.029) for which NACK has been received

The enquiry provides following options against each record displayed in the output screen:

| Option | Description |
| --- | --- |
|  | Allows to display the underlying message in read-only mode. |
|  | Allows to display the audit trail of the underlying message. |
|  | Allows to display the attributes of the received technical acknowledgements. |
|  | Allows to perform manual action on the underlying message. It opens a new screen with available actions. The actions are displayed based on whether it is a payment or non-payment message and based on the status. |

The user can perform one of the following actions against a record in the enquiry:

- **Cancel**: When the user performs this action, accounting entries are reversed and the status of outward payment is updated as Reversed (993). Audit trail is updated.

  If the outgoing pacs.008 sent to clearing is a part of pain.001 bulk payment file with the *Batch Booking Indicator* field as TRUE, and after successful reversal of the accounting entries, a new RJ transaction is created for the outgoing transaction amount to debit the Batch Suspense account and to credit the Debtor of the bulk payment as the money should be returned to the debtor who initiated the bulk payment. The user can also view the remittance information of the original transaction in the reversal message to identify which payment has been reversed. If the debtor of the bulk payment was debited for any processing charges by the TPH, the charged amount will not be credited back to the debtor as the TPH bank has processed the payment.

  If the outgoing payment is a part of the pain.001 bulk file with the *Batch Booking Indicator* field as TRUE, and settled through the cover method, where the cover is sent through Clearing, TPH releases the cover message to the clearing once positive ACK is received for the announcement message (pacs.008) from the SWIFT network.

  - On receiving the ACK for the announcement and releasing the cover, it is possible to receive a negative DLN for the announcement message. In that case, the user cannot initiate a cancellation request for an already released cover message since the status of the transaction is updated as NACKED.

  In such cases, the instructing bank has to wait for the return payment for the cover from the correspondent bank. The received return message gets routed to the repair queue with the ’Original transaction is not fully processed’ warning message. The user should accept this warning and enter the credit account number as the Original Debtor account of the batch parent transaction and submit it from the repair queue. On successful submission and authorization of the return transaction, the status of the return is updated as Completed and the status of the original transaction is updated as 'Completed with Return'.

  - On receiving the ACK for the announcement message and once the cover is released to the Clearing, it is possible for the system or the bank to receive admi.007 for the cover message from the Clearing. This can be processed either manually or through STP based on the configuration.
    - In case of a manual process, the user can wait for pacs.002 RJCT for the announcement message from the creditor agent through SWIFT. On receiving pacs.002 RJCT for the announcement message, it gets routed to the SWIFT ISO Business Exception enquiry. The user cannot take any action for the pacs.002 message since the original transaction is not in the Completed status. The user can take reverse action from the RTGS ISO Technical Exception enquiry for the cover message, which has received admi.007 from the Clearing. Once the reversal is successful, a new RJ transaction is created to debit the Batch Suspense account and to credit the Debtor of the original transaction.
    - In case of STP process, the transaction gets reversed automatically. Once the reversal is successful, a new RJ transaction is created for the outgoing transaction amount to debit the Batch Suspense account and to credit the Debtor of the original transaction. Once the transaction is reversed, if the TPH bank receives pacs.002 RJCT for the announcement message, then the message gets routed to SWIFT ISO Business Exception enquiry. The user cannot take any action for the pacs.002 message, since the original transaction is not in the Completed status. Once the original payment is marked as reversed, the payment is not displayed in the RTGS ISO Exception queue.

For redirected payments (pacs.008, pacs.009, and pacs.004), when the system receives a NACK and the user selects the ‘Cancel’ action from the RTGS Technical Exception queue, the system triggers the following overrides:

1. ‘The payment will be cancelled, and all posting entries, including charges, will be reversed. Do you wish to continue?’
2. ‘The return message should be manually sent to the original sender’.

Upon accepting these overrides, the user must manually initiate the return transaction to the sending bank using ‘Outgoing ISO Bank Transfer Return’ or ‘Outgoing ISO Customer Transfer Return’ screen.

The posting entries are directly reversed (separate reversal transaction is not created). Hence credit notification from TPH is not generated for the customer.

In case the underlying is a return payment (pacs.004), once the return transaction is reversed, the related original transaction (can be traced using *OriginalOrReturnId*field in POR.SUPPLEMENTARY.INFO table) is moved back to its original status (Completed).

- **Complete**: When user performs this action, payment status is updated as Complete (999). Accounting entries are not reversed (actions taken outside Temenos Payments Hub/Temenos Transact –directly on SWIFT alliance). Audit trail is updated.

Complete action can be performed for following scenarios:

- When the payment is sent out again from external interface
- Bank user creates a new payment using the OE screen by entering same details from the original transaction, imposing the ordering customer details, imposing same debit and credit accounts (to nullify accounting entries).

- **ProcessAsAckReceived**: This action is applicable when the underlying payment is in one of the following status:
  - Payment Sent and waiting for ACK/NACK (Status Code 677)
  - Cover sent and waiting for ACK/NACK (688)
  - NACK received for cover (691)
  - NACK received for payment (680)

    This action moves the payment to the next status assuming that the system has received ACK and continues processing. Audit trail is updated.
- **ProcessAsDLNReceived**: This action is applicable when the underlying payment is in one of the following status:
  - Payment sent and waiting for DLN
  - Cover sent and waiting for DLN
  - Negative DLN received for payment/underlying message
  - In case of cover, Negative DLN received for cover

    This action moves the payment to the next status assuming that the system has received positive DLN and continues processing. Audit trail is updated.
- **Ignore**: This option updates the AcknowledgmentAction as ‘Ignore’ (in PSM.BLOB) so that this record is not showed in this exception enquiry again. Audit trail is updated.
- **Accept**: This option is applicable for camt.056 and camt.029 messages. This action updates the AcknowledgmentAction as ‘Accept’ (in PSM.BLOB) so that this record is not showed in this exception enquiry again. Also the related EBQA record is updated to ‘Network Rejected’. The error.reason field in EBQA is updated as, ‘Rejected by the clearing with reason code <PSM.BLOB->AckNackReason>’

- For non-payment messages, only action ‘Igonre’ and ‘Accept’ are applicable. Other actions are applicable for payment messages.
- When a technical NACK is received for an outgoing pacs.004, this can be manually cancelled from Technical Exception queue which marks the return transaction as ‘Reversed’ (993) and the original transaction back to ‘Completed’ (999) status. If the outgoing pacs.004 was initiated in response to an incoming camt.056 then the corresponding EBQA record is updated with status as INWORK and process indicator as MANUAL. The error reason in EBQA table is updated as ‘Return rejected by the network’.
- When NACk is received against outward cancellation request (camt.056) or Resolution of Investigation (camt.029) and accepted from the technical exception enquiry, the status of EBQA record is updated as ‘Network Rejected’.

[Payment Status Changes based on SWIFT Technical Acknowledgements](#)

When an outward payment is processed and sent out, the system checks the SWIFT technical acknowledgement configured in the Delivery module and accordingly changes the status of the outward payment. Similarly, when an incoming technical acknowledgement from SWIFT is received, the status of the underlying outward payment is updated based on the technical acknowledgement configured in the Delivery module.

[Outward](#)

When an outward payment is processed and to be sent through the Delivery module, TPH checks against the delivery configuration to identify which technical acknowledgements are configured against the outward message and accordingly the status of the outward message is updated.

The following table explains the outward payment’s status change based on technical acknowledgement configured in the Delivery module for the carrier.

| Status of payment when message is emitted | Network Ack Req | DLN Req | Status |
| --- | --- | --- | --- |
| Payment Message ready to be sent through serial method (Status Code = 676) | Yes | Yes | Payment sent and status = Waiting for ACK (677) |
| No | Yes | Payment sent and status = Waiting for DLN |
| Yes | No | Payment sent and status = Waiting for ACK (677) |
| No | No | Payment sent and status = Complete (999) |
| Payment Message ready to be sent through Cover method (Status Code = 676) | Yes | Yes | Payment sent and status = Waiting for ACK (677) |
| Yes | No | Payment sent and status = Waiting for ACK (677) |
| Cover Message ready to be sent  (Status Code = 687) | Yes | Yes | Cover sent and status = Waiting for ACK (688) |
| No | Yes | Cover sent and status = Waiting for DLN |
| Yes | No | Cover sent and status = Waiting for ACK (688) |
| No | No | Cover sent and status = Complete (999) |

[Inward](#)

The received technical acknowledgements could be positive (ACK) or negative (NACK). When NACK is received, the user performs manual action using the ‘RTGS Technical Exception’ enquiry. The following table explains the processing when ACK (positive acknowledgement) is received.

| Positive Acknowledgement | Processing |
| --- | --- |
| Positive Interface Ack received | On receipt of ACK from client interface, the status of the underlying payment is not changed, since the message has not been delivered to SWIFT yet. |
| Positive Network Ack received | The network ack could be for a payment sent serially or for a payment sent using cover or for a cover.  Network Ack received for payment:  On receipt of ACK from SWIFT, the status of the underlying payment is changed, since the message has been accepted by SWIFT.   - Underlying payment status is moved to ‘Complete’ if DLN is not expected - Underlying payment status is moved to ‘Payment sent and waiting for DLN’ if DLN is expected - In case of cover scenario, the cover message is sent out once network ACK is received for the underlying direct message sent earlier   If the status of the payment is not in ‘Payment sent and waiting for Ack’, then audit tail is updated to indicate positive acknowledgment is received but status is not changed. It can happen in exceptional scenario when the DLN is received before the network acknowledgment. In case of a payment settled through cover, TPH releases the cover when network ack is received and does not wait for DLN as DLN can be received mush later. Also for GPI, it is expected to send cover before the end of day of the value date/settlement date mentioned in the underlying message.  Network Ack received for cover:  If status of the Cover is ‘Cover Sent and waiting for Ack’, then the status of for the cover is changed.   - Status is moved to ‘Complete’   - when DLN is not expected for underlying direct message or cover   - when DLN is expected for the underlying direct message and already positive DLN is received   - underlying payment is sent as MT103 (for which DLN is not applicable) - Status is moved to ‘Cover sent and waiting for DLN’, if DLN is expected for the cover - Status is moved to ‘Payment sent and waiting for DLN’, if DLN is required for the underlying payment and not yet received. This is done as TPH releases the cover after getting the positive acknowledgment for the cover and does not wait for the DLN (if configured to receive).   If the status of the payment is not in ‘Cover sent and waiting for Ack’, then just audit tail is updated to indicate positive acknowledgment is received but status must not be changed. |
| Delivery Notification Ack received | The positive Delivery Notification (positive DLN) is an information to the sender that the message has been delivered by swift to the correspondent bank / Clearing gateway (such as ESMIG).  DLN received for payment:  On receipt of DLN from SWIFT, the status of the underlying payment is changed, since the message has been delivered by SWIFT.  If the status of the payment is ‘Payment Sent and waiting for Ack’ or ‘Payment Sent and waiting for DLN’, then it is moved to the next status.   - In case of serial method, payment status is moved to complete. - In case of cover scenario, cover message is sent out if status is ‘Payment Sent and waiting for Ack’ and cover is not sent before   If the status of the payment is not in ‘Payment Sent and waiting for Ack’ or ‘Payment sent and waiting for DLN’, then just audit tail must be updated to indicate positive DLN is received but status is not changed.  DLN received for cover:  If the status of the payment is ‘Cover Sent and waiting for Ack’ or ‘Cover Sent and waiting for DLN’, then   - Status is moved to ‘Complete’, if DLN is not required for the underlying direct message OR if DLN is required for the underlying direct message and positive DLN is already received OR underlying message is sent as MT103 (DLN not applicable) - Status is moved to ‘Payment sent and waiting for DLN’, if DLN is required for the underlying direct message and has not yet been received   If the status of the payment is not ‘Cover Sent and waiting for Ack’ or ‘Cover Sent and waiting for DLN’, then just audit trail is updated to indicate positive DLN is received but status is not changed.  Overdue Delivery Warning is received:  Overdue delivery notification is sent by SWIFT if it is not able to deliver the message to the receiver within DLN overdue days (default is 14 days). The Delivery module provides the ability to configure the days within which DLN positive delivery notification must be received. If the configured days is passed then the network sends overdue delivery notification. The overdue days is passed as part of the SWIFT technical header.  Only the audit trail is updated to indicate DLN overdue is received but status must is not changed. |

[](#)[Resubmission of Payment Messages based on Acknowledgements](#)

When an outward Target2 message is sent, it may receive negative technical acknowledgements from SWIFT network based on delivery configurations. Payments may also receive acknowledgement from ESMIG Layer (admi.007). Payments that are awaiting technical acknowledgements and that have received negative technical acknowledgement including negative admi.007 are displayed using the RTGS Technical Exception enquiry. Under certain circumstances (for example, when DLN is not received), the users can decide to resend the payment again.

From the RTGS Technical Exception Enquiry, the user can select a payment and use the resubmit option to resend it. Resubmission of payment (Customer Transfer - pacs.008, Bank Transfer - pacs.009 and pacs.009COV, Return - pacs.004) is allowed when it is in one of the following statuses.

- Payment Sent and waiting for Ack (677)
- Payment Sent and waiting for DLN (673)
- Cover Sent and waiting for Ack (688)
- Cover Sent and waiting for DLN (683)
- Nack or Negative DLN received for payment (680)
- Nack or Negative DLN received for Cover (691)

On invoking the resubmit option, the system opens the DE version from where the user can actually resubmit the message. DE module resends the message with same Technical Header, Business Application Header (BAH), and underlying payment payload. In case the underlying payment(which is being resent) is in Awaiting Ack or Awaiting DLN status, a possible duplicate indicator is added in the BAH.

When the message is resent successfully, the following updates are also performed on the underlying payment:

- The payment status is updated (refer table below).
- If some acknowledgements were received already (Ack/DLN responses) for the direct payment or cover, those are deleted
- Audit trail is updated as: <MessageType> is resubmitted by <CurrentUserName> at <CurrentDateTime>

| Payment status before resubmit | Payment status after resubmit | Other updates |
| --- | --- | --- |
| Payment sent and waiting for ACK (677) | Payment sent and waiting for ACK (677) | Any responses received for the payment (direct message) is deleted from Response status list |
| Cover sent and waiting for ACK (688) | Cover sent and waiting for ACK (688) | Any responses received for the cover is deleted from Response status list |
| Payment sent and waiting for DLN | Payment sent and waiting for ACK (677) | Any responses received for the payment (direct message) is deleted from Response status list |
| Cover sent and waiting for DLN | Cover sent and waiting for ACK (688) | Any responses received for the cover is deleted from Response status list |
| NACK received for Payment (680) | Payment sent and waiting for ACK (677) | Any responses received for the payment (direct message) is deleted from Response status list |
| NACK received for Cover (691) | Cover sent and waiting for ACK (688) | Any responses received for the cover is deleted from Response status list |

When the response is received for the underlying payment, the system checks if a cover is sent already. If yes, the system proceeds to send a cover again.

A cover is sent again, only when the cover sent earlier received any negative responses.

The above check is done to ensure that the cover is not sent twice because of underlying payment resubmission in scenarios like:

- Cover already has positive responses received (both ACK/DLN) or
- Cover has received no responses yet

[Resubmission of Non-payment Messages based on Technical Acknowledgements](#)

When an outward Target2 payment status report (pacs.002) or Notice to Receive (camt.057) message is sent through SWIFT, it is possible to receive negative technical acknowledgements against these non-payment messages. In case of negative technical acknowledgements, these non-payment messages are displayed in the RTGS Technical Exception enquiry for the user to understand that these have been negatively acknowledged. From the exception enquiry, the system provides an option to only ignore and take any further action separately outside the system.

If a negative acknowledgement is received against the outward payment status report (pacs.002) the system does not perform any accounting entry but the operational users need to handle required postings manually.

In case, the bank decides to resend pacs.002 or camt.057 which are waiting for Ack/DLN or received Nack/Negative DLN, this resubmission must be done from the delivery (DE) module directly. TPH does not provide the resubmit option for such non-payment messages.

[](#)[Action on Payments Failing XSD Validation in TPH Transformation Layer](#)

When an outward Target2 payment is captured and processed, the XML format message is generated finally and sent through the Delivery module. The message generation happens after all processing is done (such as channel determination, validations, posting and so on). When the message is generated it is also validated against the respective schema (XSD). Under exceptional scenarios like when the xsd validation fails, this message cannot be sent out.

Therefore, if the payment message (pacs.008, pacs.009, pacs.009cov, pacs.004) fails the payload validation in the Camel Transformation Layer, the system updates payment status as Payment Failed XSD Validation and displays such payments in RTGS Technical Exception enquiry. The users can take one of the following actions on these payments:

| Action | Description |
| --- | --- |
| Complete | Updates payment status to Completed (999). Any further action need to be done manually outside the system |
| Cancel | Reverses the accounting entries and the payment status is moved to Cancel |

The system updates the file status as failed along with the error description and the user can view the status from the Sent File Details enquiry.

**User Menu > Payments > Payment Hub > Payment Inquiries > Received and SentFile Details > Sent File Details**.

The message with XSD error is still passed to Delivery Camel but the disposition (status) of the outward messages in DE module is marked as Repair.

[Action on Non - payment Failing XSD Validation in TPH Transformation Layer](#)

Similar to payment messages, when non-payment messages are generated (such as camt.056 – cancellation request, camt.029 – resolution of investigation and so on), the system validates them against the XSD.

If such non - payment messages fails the payload XSD validation (in the Camel Transformation Layer), the system displays them in RTGS Technical Exception enquiry. The system updates the audit trail as Payment Failed XSD Validation in the related payment transaction. The system updates the file status of the non-payment message as failed along with the error description in sent file details table.

**User Menu > Payments > Payment Hub > Payment Inquiries > Received and SentFile Details > Sent File Details**.

The users can take one of the following actions on these messages in RTGS Technical Exception enquiry:

| Action | Description |
| --- | --- |
| Ignore | No action is taken by TPH. Any further action needs to be done manually outside the system |
| Accept | The status of the outward cancellation message gets updated as NETWORKREJECTED. The user can again initiate outward cancellation request. Refer to the [Outward Recall (Revocation) Request (camt.056) to TARGET2](#Out_Recall) section for more details about further processing of outward cancellation request. |

- Resubmit option is not applicable for non-payment messages.
- The message with XSD error is still passed to Delivery Camel but the disposition (status) of the outward messages in the Delivery (DE) module is marked as ‘Repair’.

[](#)[Business Acknowledgement](#)

After the payment message reaches central RTGS system (after successful validation at ESMIG layer), it is sent for settlement processing. RTGS system performs various business validations as part of the settlement process and then tries to settle the payment. Based on the status of validation and settlement, RTGS system sends a business acknowledgement in the form of payment status report (pacs.002 message).

- If the settlement fails or rejected, a negative acknowledgement is sent (mandatorily) to the sending participant bank using pacs.002 message.
- If the settlement is successful, a positive acknowledgement can be sent to the sending participant bank using pacs.002 message. This is optional and based on subscription by the bank.

Payment Status Report is applicable for the following payment messages:

- Customer transfer (pacs.008)
- Bank transfer (pacs.009)
- Return payment (pacs.004)

If positive payment status report is received, the audit trail of the underlying payment is updated, and the status remains completed. If negative payment status report is received, the system can be configured to process it either in STP mode or manually. If manual processing is configured, then the user can view all such outward TARGET2 payments, which has received negative pacs.002, using the ‘RTGS Business Exception’ enquiry for manual action. The enquiry provides following actions:

| Action | Description |
| --- | --- |
| Reverse | TPH posts reversal accounting entries and moves the payment status to 993 (reversed). |
| Ignore | The transaction remains in completed status and does not post any reversal accounting entries. |

## Returns

If the payee bank is unable to credit funds to the beneficiary for a received inward CT request, it returns the payment using pacs.004 message. This can be due to closed or invalid beneficiary account. In an RTGS systems, payments can be returned on the same day. The system generates the returns as a positive response to an incoming recall request (camt.056). TPH supports TARGET2 return processing using pacs.004 message.

## Recall

Payer bank can send a recall request for a credit transfer request (CT) within the configured number of days from the payment date. Payments can be cancelled due to duplicate sending, technical problems causing erroneous transfers, and fraudulent originated credit transfer. TARGET2 receives the recall request first and if the:

- Payment (pacs.008, pacs.009, pacs.004) is not settled in RTGS, it revokes the transaction and sends a positive cancellation response to the sender of the recall request.
- Payment is already settled, it forwards the request to the payee bank.

However, if the recall request is against a return payment (pacs.004), then TARGET2 can accept or reject based on whether the return is settled or not in RTGS. TARGET2 does not forward recall request against return payments.

Payee bank receives the inward recall request and responds manually with one of the following responses:

- Positive - Accepts the recall request (to debit the customer after receiving authorisation from customer) and generates a positive recall response (by generating a pacs.004 return) to TARGET2
- Negative - Rejects the recall request by sending negative recall response (camt.029) to TARGET2

TARGET2 receives, validates and forwards the recall response to the bank (that initiated the recall). If the camt.029 message fails validation in TARGET2, it sends back a camt.025 message to the sender of camt.029.

[Enquiries for Manual Case Management Functions](#)

Enquires under the RTGS Cancellations main menu performs case management functions such as initiate recall request, authorise, respond to an incoming recall request, and so on.

**User Menu** > **Payments** > **Payment Hub** > **Investigations & Cancellations** > **Cancellations** > **RTGS Cancellations**

The following are the individual enquiries under the main menu applicable for TARGET2:

| Enquiry | Description |
| --- | --- |
| Bank Initiated Cancellation Request | Initiates a recall or revocation request against outward TARGET2 payment sent earlier as per the requirement of the bank (cancellation is not requested by the ordering customer) |
| Customer Initiated Cancellation Request | To initiate a recall (revocation) request against outward TARGET2 payment sent earlier based on request from debtor (on behalf of ordering customer) |
| Authorise Outward Cancellation Request | Authorises the outgoing recall (revocation) request |
| Delete Unapproved Outward Cancellation Request | Deletes unapproved outward cancellation requests |
| Outward Cancellation Request - View Status | Allows to view the status of outgoing recall requests sent |
| Outward Cancellation Req - Network Clearing Rejected | Allows to view the clearing rejected recall requests |
| Outward Cancellation Request-Pending Response | Allows to view the recall request awaiting response from clearing/bank |
| Inward Cancellation Req-Require Manual Action | Respond to an inward recall request to accept or reject |
| Inward Cancellation Request-View Status | Allows to view status of inward cancellation requests received |
| ROI Clearing Rejected - View status | Allows to view outward camt.029 messages rejected by clearing |
| Authorise Inward Cancellation Requests | Authorises manual action on inward cancellation request |

These enquiries are applicable for MX based RTGS systems, for example, TARGET2. Hence, it is mandatory to enter the clearing name for which records are to be displayed (TGT for TARGET2). The system supports the following case management scenarios for TARGET2.

Refer to the [Enquiries Related to RTGS ISO Outward Cancellation Processing](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Investigations/Introduction.htm#202207a) section in the [Investigations and Enquiries](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Investigations/Introduction.htm) guide for more details on the outward cancellation request enquiries.

[](#)[Outward Recall (Revocation) Request (camt.056) to TARGET2](#)

Any TARGET2 payment sent out can be recalled by initiating a recallor revocation request.

- User can initiate a recall or revocation request (camt.056) for a previously sent outward payment to TARGET2 that are in completed status (999)
  - Customer transfer (pacs.008)
  - Bank transfer (pacs.009 Core and Cover)
  - Return payment (pacs.004)

Refer to the [Enquiries Related to RTGS ISO Outward Cancellation Processing](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Investigations/Introduction.htm#202207a) section in the [Investigations and Enquiries](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Investigations/Introduction.htm) guide for more details on the outward cancellation request enquiries.

[Receiving Inward Resolution of Investigation (camt.029) from TARGET2 Against Outward Recall or Revocations Requests (camt.056)](#)

Following are the scenarios in receiving an Inward Resolution of Investigation (camt.029) from TARGET2:

| Scenario | Action |
| --- | --- |
| Identification logic of original camt.056 | When an incoming camt.029 message is received from TARGET2, the system identifies the original camt.056 (EBQA record) based on the *Original Instruction Id* field (optional) received in camt.029 matched against camt.056. If the *Original Instruction Id* field is not available in camt.029, TPH performs the following.   - During message acceptance, the system enriches the *Original Instruction ID* field by deriving it based on the Orgnlmsgid (*Original Message Id*) and OrgnlUETR (*Original UETR*) tags of incoming camt.029. - After enriching the value of the *Original Instruction Id* field, mapping routine finds its respective EBQA record to identify the original camt.056. - If original instruction id derivation fails, the system does not the enrich *Original Instruction Id* field and the received file details remains in ACCEPTED status. |
| Receiving camt.029 acceptance from TARGET2 against camt.056 when an underlying payment (pacs.008 or pacs.009) is already settled and camt.056 is forwarded to the beneficiary bank | TPH performs the following:   - When a camt.029 acceptance message (status in camt.029 is FTNA) is received from TARGET2, the underlying payment (pacs.008 or pacs.009) is retrieved. - If a record is not found in EBQA, the received file details are updated as UNMATCHED. - If the underlying payment record is retrieved, status of the record (EBQA) is retained as CANCELLATIONSENT. |
| Receiving camt.029 acceptance from TARGET2 against camt.056 when an underlying payment (pacs.008 or pacs.009) is not settled and revocation is successful | TPH performs the following:   - When a camt.029 acceptance message (status in camt.029 is PTNA) is received from TARGET2, the underlying payment (pacs.008 or pacs.009) is retrieved. - If a record is not found in EBQA, the received file details are updated as UNMATCHED. - If the underlying payment record is retrieved, status of the record (EBQA) is retained as CANCELLATIONSENT. |
| Receiving camt.029 acceptance from TARGET2 against camt.056 when underlying payment (pacs.008 or pacs.009) is not settled and revocation is successful | TPH performs the following:   - When a camt.029 acceptance message (status in camt.029 CNCL and reason code proprietary is COMP) is received, the underlying payment (pacs.008 or pacs.009) is retrieved. - If a record is not found in EBQA, the received file details are updated as UNMATCHED. If the underlying payment record is found, status of the record (EBQA) is updated as CANCELACCEPTED. - Reversal accounting entries are posted for the underlying payment (for example, pacs.008)   - Debit TARGET2 Nostro   - Credit Customer Account - Status of the underlying payment updated to 993. |
| Receiving camt.029 Acceptance Message from TARGET2 When Return Payment (pacs.004) is not Settled and Revocation is Successful | TPH performs the following:   - When a camt.029 acceptance message (status in camt.029 is CNCL and reason code proprietary is COMP) is received, the underlying return payment (pacs.004) is retrieved. - If a record is not found in EBQA, the received file details is updated as UNMATCHED. - If the underlying pacs.004 record is found, status of the record (EBQA) is updated to CANCELACCEPTED. - Reversal accounting entries are posted for the underlying pacs.004 payment   - Debit TARGET2 Nostro   - Credit Customer Account - Status of the return payment (pacs.004) is updated to 993, status of the related inward payment (for example, pacs.008) is updated to 999. |
| Receiving camt.029 reject message from TARGET2 when return payment (pacs.004) is already settled and revocation is unsuccessful | TPH performs the following:   - When a camt.029 rejection message (status in camt.029 is RJCR) is received, the underlying return payment (pacs.004) is retrieved. - If a record is not found in EBQA, the received file is updated as UNMATCHED. - If the underlying payment (pacs.004) record is found, status of the EBQA record is updated to CANCELREJECTED. |
| Receiving a camt.029 reject message from beneficiary bank in response to the camt.056 sent earlier and forwarded by TARGET2 to beneficiary bank | TPH performs the following:   - When a camt.029 reject message (status in camt.029 RJCR) is received, the underlying payment (pacs.008 or pacs.009) is retrieved. - If the underlying payment cannot be retrieved, then a EBQA record is created with status INWORK and process indicator is set as UNMATCHED. The record is updated with the reason of error as Original Txn not found. - If the underlying payment record is found, status of the EBQA record is updated as .REJECTED. |

[Responding to Inward Recall Request (camt.056) Received from TARGET2](#)

The system provides automatic and manual options to respond to an incoming cancellation request.

- Positive response - pacs.004 return payment is generated and sent through TARGET2.
- Negative response - camt.029 is generated and sent via TARGET2.

[Automated Positive or Negative Response to Inward camt.056 Received from TARGET2](#)

- If the clearing transaction type is CT, then create a record in EBQA with status INWORK.
- Retrieves the original transaction for which the recall request is received (original transaction look up criteria API is attached in PP.CLEARING.SETTING of incoming camt.056).
- If the payment record is not found (in POR.TRANSACTION), then system checks for AutoNegativeCancelReqResponse parameter in PP.CLEARING.SETTING.
  - If AutoNegativeCancelReqResponse is Y, then the system automatically generates camt.029 with reason code as NOOR and status as RJCR. EBQA record status is updated as REJECTED.
  - If AutoNegativeCancelReqResponse is N, then the system updates the reason of error as Transaction Record Not found in EBQA and ProcessIndicator as UNMATCHED. EBQA record status is updated as INWORK.
- If payment record is found (in POR.TRANSACTION) and the status of original payment is 999, system checks if the camt.056 is received within the acceptance days defined in PP.CLEARING.SETTING of inward camt.056.
- If the camt.056 is received outside the time frame of the acceptance days (CurrentBusinessDay – Requested execution date is greater than the configured acceptance days), system checks the AutoNegativeCancelReqResponse parameter.
  - If AutoNegativeCancelReqResponse is Y, then the system automatically generates camt.029 with reason code as LEGL and status as RJCR. EBQA record status is updated as REJECTED.
  - If AutoNegativeCancelReqResponse is N, then the system updates error Cancellation cannot be accepted as it is beyond acceptance days in EBQA and ProcessIndicator as MANUAL. EBQA record status is updated as INWORK.
- If the payment record is found (in POR.TRANSACTION) and the status of original payment is 999, then the system checks for Automatedreturnindicator parameter in PP.CLEARING.SETTING.
  - If Automatedreturnindicator is N, then park the record for manual intervention by setting the *Process indicator* field in EBQA to Manual and status to INWORK.
  - If the Automatedreturnindicator is Y, then the system automatically generates pacs.004 as a positive response.

[Manual Positive or Negative Response to Inward camt.056 Received from TARGET2](#)

- User can respond to the incoming recall requests parked for manual action using enquiry Inward Cancellation Req-Require Manual Action. Enter the clearing name as TGT to fetch records related to TARGET2
- Select a record and click on *Amend* option to view the EBQA record. The screen displays options to accept or reject the recall request
- To reject a recall request, the user must:
  - Select the Reject option
  - Provide the ISO reject reason code and optionally additional information
  - Commit the transaction and authorise
  - EBQA record status is updated as CANCELREJECTED and ROI ID with date and time is updated in EBQA
  - camt.029 message is generated and sent to TARGET2
- To accept a recall request:
  - User needs to select the accept option, submit and authorise
  - A new return payment is triggered and processed (RT flow).
  - Following accounting entries are raised:
    - Debit Customer account
    - Credit Clearing suspense account
    - Debit Clearing suspense account
    - Credit Clearing Nostro
  - EBQA record status is updated as CANCELACCEPTED
  - The status of underlying payment being recalled is moved to 996

[Receiving camt.025](#)

When pacs.004 message is generated and sent to TARGET2, TPH receives an inward camt.025 message from TARGET2. camt.025 is received from TARGET2 in response to an outgoing camt.029 message sent to TARGET2. The camt.025 can be received from TARGET2 in case of any business validation failures while processing received camt.029 message or on acceptance of the received camt.029 message.

If the <ReqTp> <Prtry> <id> tag in the camt.025 is updated with the value XSTS or SSTS, then the status is considered as ACCP (accepted). If the <ReqTp> <Prtry> <id> tag in the camt.025 is updated with the VSTS, then the status is considered as RJCT (rejected). The status of the EBQA record is updated as clearing rejected.

## Cover Processing

[Outgoing](#)

TPH has the ability to send outgoing CBPR+ customer payments through SERIAL and COVER method based on routing configuration. With cover method, the customer payment message (pacs.008) is sent directly to the creditor agent bank through SWIFT if the RMA is available. A separate cover payment message (pacs.009 COV) is sent to clear and settle the payment at an inter-bank level through one or more reimbursement agents.

The cover can be sent either through correspondent banks over SWIFT or can be routed through a PMI such as TARGET2. This depends on the routing configuration maintained in system.

TPH supports –

- Sending outgoing cover payment through TARGET2 (pacs.009 COV)
- Receive an incoming MT202 COV and redirect through TARGET2 as pacs.009 COV

[Incoming](#)

The system provides hold for cover option to park incoming customer payments (MT103 or pacs.008 containing reimbursement agent details through which cover is received) until funds are received through cover. Once funds arrive through cover, system does automatic matching of the cover against the previously received customer payment and complete the processing.

The creditor agent bank can also receive credit notification (MT910 / camt.054) indicating funds has been received. Customer payments parked for cover payment can be released on receipt of credit notification as well.

Customer payments, for which funds are expected to arrive through cover:

- can be configured to be processed STP without waiting for cover
- can be configured to be processed STP without waiting for cover if the transaction amount is less than a configurable threshold
- can be manually released from hold for cover queue and processed

## Business Day

The business day of TARGET2 RTGS is split into five periods:

- Start of Day (SOD)
- RTGS Real-Time Settlement I (RTGS RTS I)
- Maintenance window for TARGET services (if activated)
- RTGS Real-Time Settlement II (RTGS RTS II)
- End of Day (EOD)

Participant banks use the ‘RTGS Real-Time Settlement II’ window for payment processing by sending or receiving messages.

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_14.png)

TPH supports cut-off time maintenance only for the payment window for Customer and Bank Transfer.

## Bank Identifier Code (BIC)

BIC is given to all participant banks, as TARGET2 uses it as bank or branch identification. TARGET2 uses BIC11 to identify each party/agent.

IBAN is the preferred account identifier in TARGET2.

## Message Priority

TARGET2 ISO message format allows two types of priorities for a customer or bank transfer:

| Type of Priority | Value |
| --- | --- |
| Instruction Priority | HIGH or NORM |
| Settlement Priority | URGT or HIGH or NORM  - If settlement priority is not provided, the payment order is processed with normal priority (NORM) in RTGS. - Priority URGT (Urgent) is applicable for bank transfer only. |

## Clearing Directory and Reachability

TARGET2 provides reachability directory (containing BIC codes) for every participant. Sending banks need to validate reachability of the beneficiary bank against this directory before initiating payments to TARGET2. This validation is based on BIC. TARGET2 Directory upload feature is available in the system.

TARGET2 does not provide separate directory files for CTs and DDs. Hence Temenos Payments Hub was enhanced to use standard TARGET2 directory file to perform reachability check of both customer transfers and FI direct debits.

## Payment Product for Processing TARGET2 Payments

TARGET2 payments are processed using heavy weight product. The system is pre-configured with heavy weight products to process TARGET2 payments initiated from Payment Order, Order Entry and STP payments.

The users can modify or define their own heavy weight products using the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Bank Operations Configuration** > **Product Determination** > **Product Condition – Heavy.**

Read the Product Determination user guide (for more details on heavy weight product related features and configurations.

## Charge Processing

The system supports the following charge code processing:

- CRED: All transaction charges are to be borne by the creditor (similar to charge code BEN)
- DEBT: All transaction charges are to be borne by the debtor (similar to charge code OUR)
- SHAR: charges are shared. In a credit transfer context, the transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor. (similar to charge code SHA)

The system does not support the SLEV charge code (following service level). Hence, this option is not provided in the screens of the PO or OE applications. If SLEV is received in an incoming message, it is saved and treated as shared (SHAR).

Read the Fees and Billing user guide for more details on charge related features and configurations.

## Forex (FX)

The system supports processing payments in currencies other than the local currency. FX comes into consideration if the debtor’s or creditor’s account currency is different from the payment currency. The system does not support all three to be different currencies. Either debit account currency or credit account currency need to be the same as payment currency. Therefore FX happen either on the debit side or on the credit side but not on both side.

The system uses the exchange rates maintained by the Temenos Transact FX module. The FX module stores the currency-wise rates date wise.

The system provides configurable options to:

- process FX transactions using STP or manually
- configure discount on exchange rate for customers through client agreements
- Rate Fixing – to process transactions using previous day’s rate or manually provided rate, when rates are not available for current date.

Read the Forex user guide for more information on forex related features and configurations.

## Code Word

Code words are added as part of a payment messages to convey payment processing information. TARGET2 MX payments uses defined set of code words (as per SIO External Code list) for consistent processing across financial institutions. Additionally banks can also make special agreements and define code words for payment processing as per their agreement among themselves. These are known as Bilaterally agreed code words.

The system supports processing of payments with code words. A payment can contain multiple code words. Based on code word ranking, a final code word is arrived at and used for further processing. The code words can be used to influence:

- Payment routing
- Fees
- Posting

When the system processes TARGET2 MX messages, the following information are stored in the system as code word:

- Service Level
- Local Instrument
- Category Purpose
- Purpose
- Instruction for Creditor Agent
- Settlement Time Indication
- Settlement Time Request

In SWIFT MT format payment messages code words were allowed in Tag 23E (Instruction Code), Tag 70 (Remittance Information), Tag 72 (Sender to Receiver Information) and Tag 13C (Time Indication).

In ISO20022 format MX message there are several fields (as mentioned above) which may contain a code word (as per ISO external code list) or proprietary value. There is no one to one correspondence between the MT fields and MX fields which may contain code words.

Read the Code Words user guide for more details on booking related features and configurations.

Read the ‘Data enrichment for MT and MX format conversion’ section for details on code words supported for MT and MX conversions.

## Duplicate Check

The system can be configured to perform duplicate check on payment instructions received from SWIFT. Duplicate criteria can be configured using the EB.DUPLICATE.TYPE application. The ID of record should be configured against the heavy weight products defined to process SWIFT payments (in *Duplicate Type* field). The Business Application Header (BAH) of CBPR+ payments contains a possible duplicate field. This field is not used to determine duplicate payment. The users must define their own duplicate criteria using the EB.DUPLICATE application.

## Financial Action Task Force (FATF) Regulation

The FATF regulations are the internationally endorsed global standards against money laundering and terrorist financing. They increase transparency and enable countries to successfully take action against illicit use of their financial system. FATF governs the ordering party details that are sent as part of SWIFT customer transfers. There are separate regulations for Europe and non-European regions.

The system supports this regulatory requirement by way of a configuration.

Read the FATF user guide for more details on FATF related features and configurations.

## Filtering (Sanction Screening)

The system can be optionally interfaced with Filtering module to scan the payments before they are booked. Filtering helps to monitor various risks which are required for cross border payments such as:

- Disallowed counterparties, country and currency
- Allowed exposure for a counterparty, country and currency

Based on filtering response system can be configured to:

- Park payment in repair
- Seize funds
- Return / reject based on payment type

Read the Sanction Screening user guide (for more details on filtering related features and configurations.

## Booking

The system provides comprehensive configuration to define rules for booking entries based on payment characteristics. The system invokes the Temenos Payment DDA by providing all necessary information to book the entries. Payment characteristics are the characteristics included in Payment Product Definition.

Different booking entries include

- Principal, Charge, VAT bookings
- Rules to determine the Debit /Credit Accounts/Amount/Value Date for Principal, Charges and VAT
- Rules to Suppress entries with zero amount

The user can also configure the posting of charges accounting entry. For instance, the following are possible

- Posting charge separately from principal or along with principal
- Post charges separately and also in detail.

The user can configure statement lines to produce statements as per customer requirement.

Read the Posting user guide for more details on booking related features and configurations.

## Message Flow

The following diagram shows the high level message processing in TARGET2.

_UG2.0_v3.0_forUpload/image2.png)

| Message Type | Description |
| --- | --- |
| pacs.008 | Payer bank sends customer transfer payments to TARGET2, which settles and forwards the payment request to the payee bank. |
| pacs.009 | Payer bank sends the bank transfer payments (core and cover) to TARGET2, which settles and forwards the payment request to the payee bank. |
| pacs.004 | Payee bank returns the payment due to an issue (with the credit account) or as a positive answer to a recall request. |
| pacs.010 | Financial Institutions sends the direct debit payment to TARGET2, which settles and forwards the payment to the other Financial Institutions. |
| SWIFT Ack/Nack, DLN | Outward messages to TARGET2 are sent through SWIFT. SWIFT validates the message and sends network acknowledgement to indicate acceptance of rejection. Additionally delivery notification can be received if requested. |
| admi.007 | TARGET2 messages sent through SWIFT are received by ESMIG layer and validates. ESMIG sends negative acknowledgement as a response to received CT request (pacs.008 or pacs.009) or return payment request (pacs.004) in case of rejection. Reason for rejection could be a schema error. |
| pacs.002 | TARGET2 sends payment status report as a response to CT request (pacs.008 or pacs.009) or return payment request (pacs.004).   - If the settlement is rejected or failed, TARGET2 mandatorily sends pacs.002. - If the settlement is successful, TARGET2 optionally sends pacs.002 (if subscribed). |
| camt.056 | Payee bank initiates a cancellation request to cancel an outward credit transfer. |
| camt.029 | Negative answer to an inward or outward cancellation request. |
| camt.025 | TARGET2 sends a negative response against a camt.029 (if rejected). |

[Credit Transfer](#)

The below diagram shows the CT flow in TARGET2.

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_16.png)

TARGET2 RTGS system supports two types of CT:

- Customer transfer using pacs.008 message
- Bank transfer using pacs.009 message (core and cover)

The RTGS system processes CT requests within the allowed business day cycle for settlement, which is explained below.

1. TPH allows the following:
   - Front office user can capture outward TARGET2 CT requests from payee bank in the Payment Order (PO) application as a single payment
   - Back office user can capture outward TARGET2 CT requests from payee bank in the Order Entry (OE) application as a single payment
   - Receive cross border CT requests as MT101, MT103, MT202, MT202 COV message through SWIFT from correspondent banks and redirect them to TARGET2
   - Receive cross border CT requests as CBPR+ pacs.008, pacs.009 or pacs.009 COV message through SWIFT from correspondent banks and redirect them to TARGET2
   - Receive a pain.001 (v9) payment initiation request, process and generate customer transfer (pacs.008) to TARGET2
2. TPH processes the payment (at payee bank) and determines the payment that needs to be sent to TARGET2 based on product configuration. It posts the following accounting entries:

- Debit - Debtor Account (for originating payments) or Correspondent Bank Nostro Account (for redirected payments)
- Credit - TARGET2 Nostro account
- Credit - P&L account (if any charges are configured for customer transfer)

  After successful posting, TPH generates the following messages and sends them to TARGET2 through SWIFT:

  - pacs.008 for customer transfer
  - pacs.009 for bank transfer (core or cover)

3. SWIFT validates the payment and sends the following acknowledgements:
   - Network Acknowledgement – to indicate if the message has been accepted or rejected.
   - Delivery Notification – to indicate if the message is successfully delivered. This is optional.

     If any of these SWIFT acknowledgements are negative, then the underlying outgoing payment is parked in system for Manual action using ‘RTGS Technical Exception’ enquiry.

     Read the [Technical Acknowledgement](#Technical_Acknowledgement) section for more information.
4. ESMIG layer receives the request message from payee bank sent through SWIFT and performs technical validation. If the validation fails, it rejects the payment request and TPH receives admi.007 negative technical acknowledgement message indicating rejection.

   If any of these SWIFT acknowledgements are negative, then the underlying outgoing payment is parked in system for Manual action using ‘RTGS Technical Exception’ enquiry.

   Read the[Technical Acknowledgement](#Technical_Acknowledgement) section for more information.
5. If ESMIG validation is successful, TARGET2 RTGS system takes it up for further business validations and settlement. Based on the result of settlement, TPH receives pacs.002 message from TARGET2.
   - If the validation or settlement by RTGS is not successful, a pacs.002 message is mandatorily sent to indicate rejection.

     On receipt of pacs.002 rejection TPH can process it in STP mode or manually using ‘RTGS Business Exception’ enquiry.
   - If the settlement is successful, the bank receives a pacs.002 (if subscribed).

     Read the [Business Acknowledgement](#Business_Acknowledgement) section for more information.
6. After successful settlement at TARGET2, it forwards the CT request to the beneficiary bank. TPH receives the inward CT request (at payer bank) from TARGET2 and performs the following:

- Validates and accepts the request for processing.
- On successful processing, the system credits the beneficiary account and performs the following accounting entries:
  - Debit - TARGET2 Nostro Account
  - Credit - Creditor Account
  - Credit - P&L account (if any charges are configured for customer transfer)

    Payer bank does not send any separate payment confirmation message to TARGET2 or payee bank for an inward CT request.

    If the payer bank is not able to credit the beneficiary account, the return is sent to TARGET2 through pacs.004 message. Read the Return Payment section for more information.

TPH supports redirection of inward payments from TARGET2 using SWIFT.

[SWIFT Technical Acknowledgement](#)

TPH sends payments to TARGET2 using SWIFT in MX format. SWIFT sends the following technical acknowledgements, which are received and processed.

The process flow is described below:

1. Bank sends a CT (pacs.008 or pacs.009) or return payment (pacs.004) request to TARGET2 through SWIFT gateway.
2. SWIFT receives the message and performs technical validation. If the validation is not successful, it sends a negative network acknowledgement message (mandatorily) to the sending bank to indicate rejection.

   If the validations are successful, then SWIFT sends a positive network acknowledgement indicating message has been accepted by network.
3. Once network validation is successful, SWIFT delivers the message to ESMIG which is the interface for TARGET2.
   1. If message delivery is not successful but SWIFT continues to retry, then TPH may receive delivery overdue warning (xsys.010) from SWIFT
   2. If message delivery is successful, TPH may receive a positive delivery notification (xsys.011) from SWIFT
   3. If message delivery is successful even after retry for a configured durations, TPH may receive a negative delivery notification (xsys.012) from SWIFT

Receiving delivery notification is optional.

4. Outward TARGET2 payments, that receive a negative technical acknowledgement from SWIFT is viewed using the ‘RTGS Technical Exceptions’ enquiry for manual action.

Read the [Technical Acknowledgement](#Technical_Acknowledgement) section for more information.

[ESMIG Technical Acknowledgement](#)

ESMIG layer receives the outward payment messages (in ISO20022 format) generated by a bank for TARGET2. After receiving the payment or non-payment message through SWIFT, it performs technical validation. If the validation is not successful, ESMIG rejects and the message is not forwarded to RTGS. When there are rejections by ESMIG, a negative acknowledgement (admi.007) message is sent to the sending participant bank. These messages are received against the outward payments (such as pacs.008, pacs.009, pacs.004) or non-payment messages (such as camt.056, camt.029). If the validations are successful, ESMIG does not send any positive acknowledgement.

The process flow is described below:

1. Bank sends a CT (pacs.008 or pacs.009) or return payment (pacs.004) or a case management message (camt.056 or camt.029) request to TARGET2.
2. ESMIG layer receives the message and performs technical validation. If the validation is not successful, it sends an admi.007 message (mandatorily) to the sending participant bank to indicate rejection.
3. The bank receives the admi.007 message and identifies the outward transaction based on the related reference. The reference needs to have the BAH message ID of the outward payment request or non-payment request which is rejected.
4. Once the outward transaction is identified, subsequent processing of admi.007 can be configured for Automatic or Manual through configuration.
   - Automatic − TPH automatically cancels the outward payment and accounting entries are reversed without any manual intervention.
   - Manual − TPH does not perform any automatic action.

     For non-payment messages on receipt of admi.007, the corresponding case management record is updated with the CLEARING REJECTED status automatically irrespective of the above configuration.

     Outward TARGET2 payments, that receive a negative technical acknowledgement (admi.007) and manual processing is configured, is viewed using the ‘RTGS Technical Exceptions’ enquiry. The users can perform one of the following actions:
   - Cancel – Reveres the outward payment and moves the status to reversed (993).
   - Complete – Does not reverse the accounting entries, hence, the user needs to manually perform any further actions. The status changes to complete (999), ignoring the negative-acknowledgement.

Read the [Business Acknowledgement](#Business_Acknowledgement) section for more information.

[Business Acknowledgement Processing](#)

TARGET2 sends payment status report as a response to CT and return payment request. This indicates the status of payment settlement by RTGS system.

The process flow is described below:

- Bank sends CT (pacs.008 or pacs.009) or Return Payment (pacs.004) request to TARGET2.
- ESMIG layer receives the message and performs technical validations. On successful validation, it forwards the payment request to TARGET2.
- TARGET2 validates the request and accepts for settlement. Based on result of validation and settlement, TPH receives the pacs.002 message from TARGET2.

- If validation or settlement is not successful, a pacs.002 message is sent (mandatorily) to the bank to indicate rejection (RJCT).
- If settlement is successful (ACSC), the bank receives a pacs.002 (if subscribed).

- Receives pacs.002 against the outward payment and identifies the outward transaction based on the original instruction identification or original message identification. Based on the status received in the payment status report (ACSC or RJCT), it updates the audit trail of the outward transaction.
- If the status is reject (RJCT), subsequent processing of pacs.002 can be configured for Automatic or Manual through reason code configuration.
  - If the reason code received in pacs.002 is configured for Automatic processing (Routetoexception = N), TPH performs the following:
    - Posts reversal accounting entries
    - Moves original payment status to 993 (reversed)
  - If the reason code received in pacs.002 is not configured for Automatic processing (Routetoexception = Y), TPH does not perform any automatic reversal.

    The user can view the outward TARGET2 payments that have failed settlement (received negative pacs.002) using the ‘RTGS Business Exceptions’ enquiry. Additionally, the user performs one of the following actions:
  - Reverse – TPH posts reversal accounting entries and moves the payment status to 993 (reversed).
  - Ignore – The transaction remains in completed status and does not post any reversal accounting entries.

[Return Payment](#)

The system (as a payee bank) generates return payment as a result of failed inward CT (pacs.008 or pacs.009).

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_17.png)

The process flow is described below:

1. If an inward CT request fails to credit the beneficiary at payee bank, the payee bank sends returns as pacs.004 message to TARGET2. The user can manually generate the return from the Repair queue or automatically (if configured in the system).

   The system performs the following when returning the inward payment:

- Replaces the beneficiary account in the incoming CT payment with a configured suspense account to par the funds in a suspense account:
  - Debit - TARGET2 Nostro
  - Credit - Suspense Account
- Creates a new return transaction by exchanging the party/agent roles and processing with the following accounting entries:
  - Debit - Suspense Account
  - Credit - TARGET2 Nostro
- On successful processing of the return transaction, the inward payment status is updated as returned.

2. A pacs.004 message is generated and sent to TARGET2 through SWIFT. The return chain component in the pacs.004 message has the party and agent details in reversed order.
3. SWIFT validates the payment and sends the following acknowledgements:
   1. Network Acknowledgement – to indicate if the message has been accepted or rejected.
   2. Delivery Notification – to indicate if the message is successfully delivered. This is optional.

      If any of these SWIFT acknowledgements are negative, then the underlying return payment is parked in the system for Manual action using ‘RTGS Technical Exception’ enquiry.

      Read the [Technical Acknowledgement](#Technical_Acknowledgement) section for more information.
4. ESMIG layer receives the pacs.004 message from SWIFT and performs technical validation. If validation fails, the return payment request is rejected and the system receives admi.007 negative technical acknowledgement message indicating rejection.

   Read the [Technical Acknowledgement](#Technical_Acknowledgement) section for more information.
5. If ESMIG layer accepts the message, RTGS system performs further business validations and settlement. Based on the settlement status, TARGET2 sends a pacs.002 message to TPH.

- If validation or settlement is not successful, a pacs.002 message is sent to indicate rejection.
- If settlement is successful, the bank receives a pacs.002 (if subscribed).

Read the [Business Acknowledgement](#Business_Acknowledgement) section for more information.

On receiving pacs.002 RJCT for the return transaction, if the processing is configured as STP or manual (on clicking Reverse button from the enquiry), the system creates a reversal transaction by reversing the accounting entries. and updates the following:

- Status of pacs.004 from Completed to 998 (Rejected)
- Status of original transaction for which the return is generated from Completed with Return (996) to Completed (999).

6. After successful settlement of the return payment at TARGET2, it forwards the return payment to the original payer bank.

Original payer bank receives the inward pacs.004 return payment from TARGET2 and performs the following steps:

1. Validates and accepts the request for processing
2. Identifies the original transaction and original debit account
3. On successful processing, credits the returned funds to the original debit account. It performs the following accounting entries:

- Debit - TARGET2 Nostro
- Credit - Identified debit account (main debit account of original payment being returned). Updates the original outward credit transfer payment as ‘Returned’.

[Recall Processing](#)

The following diagram shows the process of recalling a payment.

_UG2.0_v3.0_forUpload/Introduction to TARGET2 RTGS_18.png)

The process flow is described below:

1. The bank user can initiate manual recall (requested by customer or operations user) for the following outward payments that were sent to TARGET2:
   - Customer transfer (pacs.008)
   - Bank transfer (pacs.009 CORE)
   - Return payment (pacs.004)The system provides an enquiry to list the above payments.
2. The user selects the payments from the enquiry (for which recall request is to be initiated) and provides the reason code for cancellation. The system process the request and forwards it to TARGET2 as a camt.056 message through SWIFT.
3. TARGET2 receives the cancellation request (camt.056), and performs the following validations:

- If the CT request (pacs.008 or pacs.009) is already settled at TARGET2, it forwards camt.056 to the payee bank and sends a camt.029 message to the originator of the camt.056 with status code as FTNA.
- If the CT (pacs.008 or pacs.009) or return payment (pacs.004) is not settled at TARGET2, it does not forward camt.056 to the payee bank and sends a camt.029 message to the originator of the camt.056 with status code as CNCL.
- If the return payment (pacs.004) is already processed and settled at TARGET2, it does not forward camt.056 to the payee bank and sends a camt.029 message to the originator of the camt.056 with status code as RJCR.

4. Payee bank receives the inward cancellation request (camt.056). The system validates if the cancellation request is valid and within the permitted acceptance days (if configured).

- If the request is valid and within permitted acceptance days, bank user accepts the recall request in the system (post consent from the customer, if required)
  - If the original payment is fully processed, it reverses the accounting and marks the payment as ‘Returned’.
  - If the original payment is not complete (that is, failed and parked in Repair queue), it parks the incoming camt.056 in a Manual queue as unmatched items.
- If the request is not valid or within configured permitted due days, the system rejects the recall request by sending a camt.029.

5. Based on the processing (of the inward camt.056), TPH sends one of the following responses at the payee bank:

| Response | Description |
| --- | --- |
| Positive | If recall request is accepted at the payee bank, the system sends pacs.004 return payment to TARGET2. TARGET2 validates, settles, and forwards the return payment to the payer bank   - ESMIG validates the pacs.004 request and sends admi.007 (if an error occurs). - If ESMIG validation is successful, RTGS validates and settles the return. A pacs.002 is sent based on settlement status.   Read the [Technical Acknowledgement](#Technical_Acknowledgement) and [Business Acknowledgement](#Business_Acknowledgement) sections for more information. |
| Negative | If recall request is rejected at the payee bank, system sends camt.029 to TARGET2 and then forwards it to the originator bank.  If RTGS rejects the camt.029, it sends a camt.025. |

6. Payer bank receives pacs.004 or camt.029 from TARGET2 against the recall request.

- If the payer bank receives a pacs.004 return, it reverses the original pacs.008 payment (customer is credited back) and marks the status of original payment as returned.
- If the payer bank receives a camt.029 response, it rejects the cancellation request and marks the status of the cancellation request as CANCELREJECTED.

TPH supports only bank initiated recalls.

[Support of Inward camt.025 Message from Clearing](#)

The system supports processing of camt.025 message received from TARGET2 in response to an outgoing camt.029 message. The camt.025 is received from TARGET2, when the camt.029 message is rejected (for example, validation failure of camt.029 message).

- If the <ReqTp> <Prtry> <id> tag in the camt.025 has the value XSTS/SSTS, the status is considered as accepted (ACCP).
- If the <ReqTp> <Prtry> <id> tag in the camt.025 has the value VSTS, the status is considered as rejected (RJCT) and the status of the cancellation record is updated to clearing rejected.

## Liquidity Transfer Advice

TARGET2 can send Liquidity Transfer Advice (LTA) to the direct participant banks to notify a balance or position update on their accounts held with TARGET2. LTA is sent as camt.054 message from TARGET2. LTA may represent a credit advice or a debit advice depending upon whether participant banks account is credited or debited in TARGET2 due to liquidity transfer operations between the accounts.

On receipt of incoming camt.054 from TARGET2, TPH stores the LTA, qualifies the LTA as a payment, resolves the accounts and performs posting. LTA payments that failed processing are moved to repair queue. LTAs that failed format validation or duplicate check are available in TPH for repair. ‘LQ’ license is required to receive and process LTA from TARGET2.

[Co-Management](#)

The Co-management is a functionality where TARGET2 allows indirect participant banks to maintain Main Cash Account (MCA) within TARGET2, while delegating the management of such account to another bank, typically its agency bank (who is a direct participant in TARGET2). The bank that manages MCA for the indirect participant bank is called the Co-manager, while the bank that has delegated the management of its MCA is called the Co-managee.

The Co-manager has the authority to act upon the Co-managed entity’s MCA for effective liquidity management. The actions include,

- Funding and de-funding the Co-managee account.
- Executing overnight deposits and lending operations on the Co-managee account.

TARGET2 sends a Liquidity Transfer Advice (LTA) to the Co-manager when the balance of the Co-managee MCA changes due to any of the actions mentioned above. The Co-manager may use this LTA to update Co-managee’s Nostro account to manage liquidity operations.

[Qualifying the LTA as Payment:](#)

When TPH receives a camt.054 message, it checks whether the transaction can be determined as ‘LTA payment’ or not based on the configurable criteria mentioned below. The user can configure the LTA qualification criteria using the following menu.

**Admin Menu**>**Payments**>**Liquidity Management**>**LTA Qualification**

| Criteria | Description |
| --- | --- |
| Sending Institution Identification | ID of the sending institution (TARGET2) |
| Receiving Institution Identification | ID of the receiving institution (typically a BIC of our bank) |
| Participant Identification | Identification of the participant whose liquidity position or balance is adjusted.   This will be our bank BIC (BIC as registered with the TARGET2) where we are a direct participant or liquidity serviced participant. |
| Account Identification | Account of the participant whose liquidity position or balance has been adjusted. Can be a bank identifier or account.  This is the Account (held in TARGET2) where Temenos bank is a direct participant or liquidity serviced participant. |
| Advice Type | Indicates whether the LTA is for a debit or credit operation.   - Debit indicator (DBIT) indicates debit on our account (found in Debtor Account field) - Credit indicator (CRDT) indicates credit on our account (found in Credit Account field) |
| Transfer Type | Indicates the type of the underlying Transfer which is a regular payment, Ancillary System(AS) transfer or liquidity adjustment. |
| Local Instrument Proprietary | Identifies the Proprietary type of underlying transaction.  The values vary by TARGET2. For example,  LIIA - Immediate liquidity transfers = Intra-service (in case of  RTGS incl. AS-related + SettlementBankTransferInitiation)  LIIE - Immediate liquidity transfers = Inter-service |
| Local Instrument Code | Indicates the clearing specific codes as received. For example, LIQT,LIQE |
| TARGET2 Status Code | Indicates the status of the adjustments as recorded within the TARGET2 system. For example, BOOK |
| Debtor Agent | Identifier of the agent who is getting debited. This can be TARGET2 Identifier (BIC) or Our bank settlement BIC with the TARGET2 (or our Liquidity provider’s settlement BIC) depending upon LTA being debit or credit |
| Debtor Account | Account identifier of the debtor agent who is getting debited. This can be TARGET2 Account or Our Account with the TARGET2 (or any of our Liquidity serviced participant’s Account in case our bank provide such service)  depending upon LTA being debit or credit |
| Creditor Agent | Identifier of the agent who is getting credited. This can be TARGET2 Identifier (BIC) or Our bank settlement BIC with the TARGET2 (or our Liquidity provider’s settlement BIC depending upon LTA being credit or debit |
| Creditor Account | Account identifier of the creditor agent who is getting debited. This can be TARGET2 account or Our Account with the TARGET2 (or any of our liquidity serviced participant’s account in case our bank provide such service) depending upon LTA being credit or debit |

[Deriving the Accounts for LTA Payment](#)

If the LTA is qualified as a payment, the account for which LTA notification is received is debited or credited in receiving participant bank during processing of the LTA payment.

LTA payment comprises of a debit account and a credit account that represent accounts where the liquidity adjustments were affected by the Account Holding Institution (AHI). Both these accounts are external accounts to our bank, hence TPH resolves these accounts to an inhouse Nostro or suspense account within our bank to perform necessary bookings. The posting is mainly for liquidity management purposes, such that receiving participant bank Nostro balances are up-to-date with the balance or positions in the actual account in TARGET2, thus enabling the receiving participant bank to perform efficient liquidity management functions.

The user can configure the in-house Nostro or suspense account in LTA account mapping table from following menu:

**Admin Menu**>**Payments**>**Liquidity Management**>**LTA Account Mapping**

[Handling LTAs from Repair Queue](#)

Incoming LTAs that failed to qualify as a payment or failed while resolving the account or failed duplicate check or failed clearing specific validations are moved to repair queue for repairing by the bank user. Customers can also make LTA payments non-STP and can process from repair queue. The incoming LTAs that are awaiting repair can be viewed using dedicated enquiry – LTA Repair in TPH (Read [Repairing the LTAs that failed to Process Successfully](Working_with.htm#202105) in Working with TARGET2 RTGS (ISO20022) feature for more information).

From the repair screen, the user can either cancel the LTA or modify to submit in order to continue processing with repaired details. The following fields can be modified during repair:

- Value Date
- Debit Account
- Credit Account

After the user repairs the payment and commits, it is queued for supervisor authorisation (if configured). After authorisation, the repaired payments is processed again starting from LTA qualification step. If the user cancels the LTA, it is moved to cancelled (997) status on authorisation. The user must enter the reason for cancelling.

Read [Liquidity Transfer Advice](#202105) User Guide for more information on configurations.

## Liquidity Transfer Request

Participant banks that maintain cash accounts with TARGET2 can send Liquidity Transfer Request (LTR) messages to move funds between their Main Cash Account (MCA), Dedicated Cash Accounts (DCA), sub-accounts, central bank accounts, and accounts of other participant banks within the same liquidity group. Based on the Local Instrument Code (LIC), TPH sends a liquidity transfer message (pacs.009 or camt.050) TARGET2 to trigger the liquidity movement between the chosen accounts.

The system can receive Network ACK/NACK and Delivery Notifications (DLN) from SWIFT for the sent LTR message. It could also receive an admi.007 (receipt acknowledgement) from ESMIG. The system updates the audit trail of the LTR payment when a positive ack and DLN is received. The LTR remains in Completed status. However, when a nack, negative DLN or an admi.007 is received, depending on the configuration, the system either processes the reversal in Straight Through Processing (STP) mode or moves the payment to the ‘LTR Technical Exception’ enquiry. Read the [Liquidity Transfer Request](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Liquidity_Transfer_Request/Introduction.htm) user guide for more information.

After completing the technical validations, TARGET2 executes business validations and sends a pacs.002 or camt.025 message against the original pacs.009 or camt.050 message respectively to indicate whether the LTR is accepted or rejected.

On receipt of a positive pacs.002 or camt.025, TPH updates the audit trail of the original LTR keeping the LTR in Completed status. If a negative response is received, the system processes the response either in STP mode or manually based on the configuration. If manual processing is configured, then the user can view such LTRs from the ‘LTR Business Exception’ enquiry and take manual action.

LQ license is required to process and send LTRs to TARGET2.

[Capturing LTR](#)

The user can capture LTRs from the LTR screen of the PO application as well as the LTR screen of the OE application.

To capture LTR using the PO application, go to **User Menu** > **Payments** > **Liquidity Management** > **Front Office** > **LTR Initiation**.

To capture LTR using the OE screen, go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **LTR Initiation**.

The user can capture the following fields:

| Field | Description |
| --- | --- |
| *Payment Order Product* | User can select the product relevant to the channel using which the LTR message is to be delivered. Applicable only in the LTR PO application GUI |
| *Debit Account Number* | Indicates the account number (as maintained in the bank’s books) that is debited. The user can manually select the account. When this field is left blank, it is auto-populated when the External Debit Account field is captured based on the internal-external account mapping |
| *Debit Account Currency* | Indicates the currency of the debit account number |
| *Debit Account Name* | Indicates the name of the debit account number |
| *External Debit Account* | Indicates the account number (as maintained in the account holding institution) that is debited. The user can manually select the account. When this field is left blank, it is auto-populated when the Debit Account Number field is captured based on the internal-external account mapping. |
| *Payment Currency* | Indicates the transaction currency. TARGET2 supports only EUR payments. |
| *Payment Amount* | Indicates the transaction amount |
| *Credit Account Number* | Indicates the account number (as maintained in the bank’s books) that is credited. The user can manually select the account. When this field is left blank, it is auto-populated when the External Credit Account field is captured based on the internal-external account mapping |
| *Credit Account Currency* | Indicates the currency of the credit account number |
| *Credit Account Name* | Indicates the name of the credit account number |
| *External Credit Account* | Indicates the account number (as maintained in the account holding institution) that is credited. The user can manually select the account. When this field is left blank, it is auto-populated when the Credit Account Number field is captured based on the internal-external account mapping. |
| *Local Instrument Code* | Indicates the Clearing-specific codes. The LTR message type is selected based on the input of this attribute. When captured as "SBTI", a pacs.009 LTR message is generated. For all other local instrument codes, a camt.050 LTR message is generated |
| *Output Channel* | The user can select the output channel using which the LTR message is to be delivered. Applicable only in the LTR Order Entry GUI |

[Processing Liquidity Management Details](#)

In addition to normal payment processing, the captured LTRs are subject to liquidity management specific processing, as follows:

| Process | Description |
| --- | --- |
| Account Derivation | External account numbers are account numbers as maintained with the AHI. Internal account numbers are account numbers that are maintained in the participant bank’s books. These in-house accounts are typically mirror accounts to the external accounts and can either be a Nostro or suspense account. During LTR initiation, the user can capture either internal accounts or the external accounts. When the user captures internal accounts, the external accounts are auto-populated and vice-versa. The internal to external account mapping can be configured from the menu under **Admin Menu** > **Payments** > **Liquidity Management** > **LTA Account Mapping**. |
| Service Derivation | TARGET2 has two services – CLM (Central Liquidity Management) and RTGS (Real-Time Gross Settlement). CLM holds the Main Cash Accounts (MCA) and RTGS holds other accounts such as Dedicated Cash Account (DCA), sub-accounts, and so on. The system sends the LTR message to the service that holds the account being debited. TPH derives the service based on the 'Account Residing Service' configuration in the LTA Account Mapping table. |
| Message Derivation | TARGET2 supports both camt.050 and pacs.009 LTR message types. TPH derives the message type to be generated based on the Local Instrument Code (LIC) in the captured LTR payment. The system generates a pacs.009 LTR message and sends when the LIC is captured as “SBTI”. For all other cases, the system generates a camt.050 and sends it to TARGET2. |

Read the [Liquidity Transfer Request](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Liquidity_Transfer_Request/Introduction.htm) user guide for more information on capturing, processing, and viewing LTRs.

## Multi-addressee Participants

A multi-addressee is an entity that sends or receives payment messages directly through TARGET2 but cannot settle the payment as they do not own a cash account. All settlements are done through an authorised direct participant’s Dedicated Cash Account (DCA).

The following screenshot details the differences between Direct Participants, Indirect Participants and Multi-addressee access:



The following diagram illustrates the message flow and settlement process of an outbound payment from a multi-addressee. For example:

- Bank A is a multi-addressee
- Bank B is a direct participant that has authorised bank A to settle payments using its cash account
- Bank C is a direct participant of the TARGET2
- Bank D is a multi-addressee that uses bank C’s cash accounts to settle its payments.



- Bank A sends the payment or recall message directly to the TARGET2. The From tag in the BAH of the message holds Bank A’s BIC while the Instructing Agent or Assigner tag in the payload is populated with the BIC of Bank B.
  - When the message is intended for Bank C, a direct participant, the To tag in the BAH and the Instructed Agent or Assignee tag holds Bank C’s BIC.
  - When the message is intended for Bank D, a multi-addressee, the To tag in the BAH is populated with Bank D’s BIC while the Instructed Agent or Assignee tag holds Bank C’s BIC.
- Based on the To tag of the BAH, TARGET2 forwards the message to the intended recipient.
  - When the message is intended for bank C, a direct participant, TARGET2 settles the payment between the cash accounts of bank B (Bank A’s settlement bank) and bank C as per the information in the Instructing Agent and Instructed Agent tags (or Assigner and Assignee tags for recall message). The message is forwarded to Bank C.
  - When the message is intended for bank D, a multi-addressee, TARGET2 settles the payment between the cash accounts of bank B Bank A’s settlement bank) and bank C as per the information in the Instructing Agent and Instructed Agent tags (or Assigner and Assignee tags for recall messages). The message is forwarded to Bank D.

When TPH bank is a multi-addressee, its payments are settled using a direct participant of TARGET2. This direct participant becomes the settlement bank of the multi-addressee. This can be configured in the *Settlement Bic Or Ncc* field in the Clearing configuration screen. Read [Configuring Settlement BIC for a Multi-addressee](Configuration.htm#Configuring_Settlement_BIC_for_a_Multi-addressee) section for more information on how to configure the settlement BIC when Temenos Payments Hub bank is a multi-addressee. When configured, this will be picked up during R&S along with the settlement bank of the counterparty bank from the clearing directory.

If originating or the beneficiary banks are multi-addressee, the Instructed Agent and Instructing Agent or Assigner and Assignee tags are populated respectively with their settlement BICs. As part of outgoing payment processing, TPH stores Temenos Payment bank’s settlement BIC in the *Settlement\_BIC\_NCC\_Sender* local field while it stores the settlement BIC of the receiver in the *Settlement\_BIC\_NCC\_Receiver* local field. For an incoming message, TPH stores the BIC in From tag in SENDER role whereas the Instructing Agent or Assigner tags is stored in SNDINS role.

## Channel Validation

When the user captures and processes an outward payment in TPH, as part of Routing and Settlement, the system tries to determine the routing channel. While determining a channel, the system performs channel validations to validate whether the underlying payment object conforms to the messaging requirements of the destination channel. The system performs the same channel validations even for redirected payments, payments initiated from the `PO` application and pain.001. If the channel validation fails, then based on routing configuration, the system either checks the next channel or moves the payment to the repair queue.

The following are the two channel validations performed for ISO20022 based payments (for example, MX based clearing such as TARGET2):

- Common Validations : These are standard validations that are applicable for all ISO20022 based messages.

  If Nobicbkcdvalidation in `PP.CLEARING` or `PP.COMPANY.PROPERTIES` is set as Y, then validating the BIC against `RD.CENTRAL.BANK.DIR` is skipped as part of common validations.
- Specific Validations : These are additional validations (on top of common validations) that are specific to the determined channel (applicable only for TARGET2) and are not applicable for others.

The Channel validations are performed only for the following MX payment types:

- Customer Transfer (which results in pacs.008)
- Bank Transfer (which results in pacs.009)
- Return Payment (which results in pacs.004)

When a customer payment is captured which is settled through cover, the same payment object is first checked for customer transfer validations followed by the bank transfer validations. The system does not perform separate validations for the underlying credit transfer block of the pacs.008 announcement.

When a cover is received and redirected , the bank transfer part of the message is validated but no separate validation is performed for Underlying Credit Transfer section (as this information is saved as a BLOB and attached as it is in the redirected message).

The system does not perform any separate channel validation for the individual elements of structured remittance information. When structured remittance information is received in pain.001 or as an incoming message, it is saved as a XML (BLOB) and attached to the generated outgoing or redirected message.

[Customer Transfers (pacs.008)](#)

Given below are the Common and TARGET2-specific Validations for Customer Transfers (pacs.008).

[Common Validations](#)

The following table lists the common channel validations performed for all ISO20022 (MX) based on customer transfers (pacs.008) including TARGET2 customer transfer payments:

| Validation | Error Description |
| --- | --- |
| If the instructed currency is different from the payment currency, then exchange rate should be present | ExchangeRate must be present when InstructedAmount with different currency is present |
| If the instructed currency is equal to payment currency, then exchange rate may not be present | ExchangeRate may not be present when InstructedAmount has same currency as transaction currency |
| If instructed amount is not present, then exchange rate may not be present | If InstructedAmount is not present, then ExchangeRate may not be present. |
| If Intermediary agent 1 account details are present Intermediary Agent 1 details should be present | Intermediary agent institution information must be present when Intermediary agent account is present. |
| If Intermediary Agent 2 account details are present, Intermediary Agent 2 details should be present. | 2nd Intermediary agent institution information must be present when 2nd Intermediary agent account is present |
| If Intermediary Agent 3 account details are present, Intermediary Agent 3 details should be present. | 3rd Intermediary agent institution information must be present when 3rd Intermediary agent account is present |
| The details of the second intermediary agent are allowed only when the first intermediary agent is present | If 2nd IntermediaryAgent is present, then 1st IntermediaryAgent must be present |
| The details of the third intermediary agent are allowed only when the second intermediary agent is present | If 3rd IntermediaryAgent is present, then 2nd IntermediaryAgent must be present |
| The details of the first previous instructing agent account are allowed only when the first previous instructing agent is present | 1st Previous Instructing agent institution information must be present when 1st Previous Instructing agent account is present. |
| The details of the second previous instructing agent account are allowed only when the second previous instructing agent is present | 2nd Previous Instructing agent institution information must be present when 2nd Previous Instructing agent account is present |
| The details of the third previous instructing agent account are allowed only when the third previous instructing agent is present | 3rd Previous Instructing agent institution information must be present when 3rd Previous Instructing agent account is present |
| The details of the second previous instructing agent are allowed only if the first previous instructing agent details are present | If 2nd Previous Instructing Agent is present, then 1st Previous Instructing Agent must be present |
| The details of the third previous instructing agent are allowed only if the second previous instructing agent details are present | If 3rd Previous Instructing Agent is present, then 2nd Previous Instructing Agent must be present |
| If BIC is provided, it should be valid | Invalid Financial Institution BIC for <<party role>>  Given below are the list of Party Roles:  ORDINS, ACWINS, SENDER, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, CHGPTY, CHGPTY2, CHGPTY3, CHGPTY4, CHGPTY5, RECVER |
| If Postal Address Country is provided, it should be a valid country code | Invalid Postal Address Country for <<party role>>  Given below are the list of Party Roles:  ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, CHGPTY, CHGPTY2, CHGPTY3, CHGPTY4, CHGPTY5, ORDPTY, BENFCY, ULTDBT, ULTCDT, CHGPTY, INSPTY |
| If Country of Birth is provided, it should be a valid country code | Invalid Country of Birth for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| If Country of Residence is provided, it should be a valid country code | Invalid Country of residence for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| If the Regulatory Reporting Country is provided, it should have a valid country code | Invalid Regulatory Reporting Country Code |
| If the Account Currency is provided, it should have a valid currency code | Invalid Agent Account Currency for <<party role>>  Given below are the list of Party Roles:  ORDINS, ACWINS, SENDER, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, RECVER |
| If Structured Remittance Information details are provided, then Unstructured Remittance Information details are not allowed. If Unstructured Remittance Information details are provided, then Structured Remittance Information related details are not allowed | Unstructured and Structured Remittance Information are mutually exclusive |
| If Related Remittance Information details are provided, then Remittance Information details are not allowed. If Remittance Information details provided, related remittance information is not allowed. | Related Remittance Information and Remittance Information are mutually exclusive. Either one of them can be present |
| If Structured Postal Address details are provided, the Town Name and Country are mandatory | For structured Postal Address, Town Name and Country must be present for <<party role>>  Given below are the list of Party Roles:  SNDCBK, RCVCBK, TRMINS, ORDINS, ACWINS, RECVER, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, CHGPTY, CHGPT2, CHGPT3, CHGPT4, CHGPT5, ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| If Structured Postal Address details are provided (minimum Town name and country), Unstructured Postal Address (address lines) details are not allowed. If Unstructured Postal Address (address lines) details are provided, structured Address details are not allowed. This validation is relevant only when Hybrid address is not enabled. Read [Support for Hybrid Address](#Hybrid) for more details. | No Postal Address Lines can be present if any fields of Structured Postal Address information are present for <<party role>>  Given below are the list of Party Roles:  SNDCBK, RCVCBK, TRMINS, ORDINS, RECVER, INTINS, INTINS1, INTINS2, PRVINS, PRVIN2, PRVIN3, CHGPTY, CHGPT2, CHGPT3, CHGPT4, CHGPT5, ORDPTY, ULTDBT, INSPTY |
| If either of Structured or Unstructured Postal Address details are provided, name of the party role should be provided | Name and Structured Address (at least Town Name and Country) or Unstructured Address should be present for <<party role>>  Given below are the list of Party Roles:  SNDCBK, RCVCBK, TRMINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, CHGPTY, CHGPTY2, CHGPT3, CHGPT4, CHGPT5, RECVER,ULTDBT, INSPTY, ORDPTY |
| Maximum three occurrences of service level (code and/or proprietary) information can be provided.  (If the processing bank is enabled with GPI, then the system automatically maps G001 and therefore the user should provide maximum two service levels. If the processing bank is not GPI Enabled, then the user can enter upto three service levels) | Maximum 3 entry of service level is allowed |
| If Local Instrument information is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Local Instrument |
| If Category Purpose information is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Category Purpose |
| If Transaction Purpose information is provided, both code and proprietary should not be provided at the together | Either Coded or Proprietary form can be present for Transaction Purpose |
| If Account Identification scheme related information is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Account Identification Scheme for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENFCY, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Account Type for the party role is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Account Type for <<party role>> Given below are the list of Party Roles:  ORDPTY, BENFCY, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Account Proxy Type for the party role is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Account Proxy Type for <<party role>> Given below are the list of Party Roles:  ORDPTY, BENFCY, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Organisation Identification Scheme for the party role is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Organisation Other Identification Scheme for <<party role>> Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| If Private Identification Scheme for the party role is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Private Other Identification Scheme for <<party role>> Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| Both Organisation Identification related information and Private Identification related details should not be provided together | Either Organisation identification or Private identification can be present for <<party role>> Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| The PayCreditorByCheque (CHQB) and HoldCashForCreditor (HOLD) codes are not allowed together in the Instruction for Creditor Agent field | If Instruction for Creditor Agent is CHQB, HOLD is not allowed as another code |
| The Telecom (TELB) and PhoneBeneficiary (PHOB) codes are not allowed together in the Instruction for the Creditor Agent field | If Instruction for Creditor Agent is "PHOB", "TELB" is not allowed as another code. |
| If Clearing System Member Id is provided, either Clearing System Code or Clearing System Proprietary should be provided | If Clearing Member Identification is present, then clearing system id or proprietary must be present for <<party role>> Given below are the list of Party Roles: ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, CHGPTY, CHGPTY2, CHGPTY3, CHGPTY4, CHGPTY5 |
| The same code  should not be repeated when the Instruction for Creditor Agent is provided | Same code word should not be repeated for Instruction for Creditor Agent. |
| If the Organisation Identification details are provided, either the scheme code or scheme proprietary information should be provided | When Organisation Other Identification is provided, Identification is mandatory for <<Party Role>>. Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| Private Identification should be provided if any of private scheme code, scheme proprietary, or issuer details are provided | When Private Other Identification is provided, identification is mandatory for <<Party Role>>. Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| If any of the details of birth, such as Date, Province of birth, City of birth, Country of birth are provided, Birth date, City of Birth and Country of Birth should be provided | - BirthDate should be present   when CityOfBirth and CountryOfBirth are present for <<Party role>> - CityOfBirth should be present when BirthDate and CountryOfBirth   are present for <<Party role>> - CountryOfBirth should be present when BirthDate and CityOfBirth   are present for <<Party role>>   Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| End-to-End Identification of the payment should not start or end with “/” and should not contain “//” | End to End Identification should not have "/" as 1st and 16th character and no "//" up to 16th character |

[TARGET2 Specific Validations](#)

The following table lists the TARGET2 specific validations performed for customer transfers (pacs.008):

| Validation | Error Description |
| --- | --- |
| Transaction currency must be EUR | Transaction Amount Currency must be 'EUR' for Target2 |
| If structured remittance information is entered in the Order Entry screen, then the total length of the data should not exceed 9000 characters.  (This validation is performed only when the payment is created from OE. When structured remittance is received in pain.001 or in an incoming pacs.008 message, the complete data is stored as XML and hence 9000 character length validation is not performed). | Structured remittance Information should not exceed 9000 characters |
| Instruction for next agent should not exceed 35 characters. | Max 35 characters allowed in each line of instruction information |
| Settlement Priority URGT is not allowed for customer transfer. Only NORM and HIGH are allowed. | Settlement Priority URGT is not allowed for customer transfer |
| If BIC is present, then it may contain either 8 or 11 continuous characters | Organisation BIC must contain either 8 or 11 continuous characters for party <Party Role>  ORDPTY, BENFCY, ULTDBT, ULTCDT, INIPTY |
| For all agent roles, if BIC is not present, then name and address (structured and unstructured) should be present. | If BIC is absent, Name & Structured address (atleast Country&Town Name) or Unstructured Address must be present for <party role>  RECVER, INTINS, INTIN2, INTIN3, BENINS , PRVINS, PRVINS2, PRVINS3, ORDPTY, ORDINS, CHGPTY, CHGPTY2, CHGPT3, CHGPT4, CHGPT5, ACWINS, SNDCBK, RCVCBK, TRMINS |

[Bank Transfers (pacs.009)](#)

Given below are the Common Validations and TARGET2 Specific Validations for Bank Transfers (pacs.008).

[Common Validations](#)

The following table lists the common channel validations performed for all ISO20022 (MX) based bank transfer payments (pacs.009) including TARGET2 bank transfer payments:

| Validation | Error Description |
| --- | --- |
| The details of 1st Previous Instructing Agent Account are allowed only if the first Previous Instructing Agent is present | Intermediary agent institution information must be present when Intermediary agent account is present |
| The details of 2nd Previous Instructing Agent Account are allowed only if second Previous Instructing Agent is present | 2nd Intermediary agent institution information must be present when 2nd Intermediary agent account is present |
| The details of 3rd Previous Instructing Agent Account are allowed only if third Previous Instructing Agent is present | 3rd Intermediary agent institution information must be present when 3rd Intermediary agent account is present |
| The 2nd Intermediary Agent details are only allowed if first Intermediary Agent is present | If 2nd IntermediaryAgent is present, then 1st IntermediaryAgent must be present |
| The 3rd Intermediary Agent details are only allowed if second Intermediary Agent is present | If 3rd IntermediaryAgent is present, then 2nd IntermediaryAgent must be present |
| The 1st Previous Instructing Agent Account details are allowed only if 1st Previous Instructing Agent is present | 1st Previous Instructing agent institution information must be present when 1st Previous Instructing agent account is present. |
| The 2nd Previous Instructing Agent Account details are allowed only if second Previous Instructing Agent is present | 2nd Previous Instructing agent institution information must be present when 2nd Previous Instructing agent account is present |
| The 3rd Previous Instructing agent details are allowed only if the third Previous Instructing agent account is present | 3rd Previous Instructing agent institution information must be present when 3rd Previous Instructing agent account is present |
| The 2nd Previous Instructing Agent details is allowed only if the first Previous Instructing Agent details are present | If 2nd Previous Instructing Agent is present, then 1st Previous Instructing Agent must be present |
| The 3rd Previous Instructing Agent details is allowed only if the second Previous Instructing Agent details are present | If 3rd Previous Instructing Agent is present, then 2nd Previous Instructing Agent must be present |
| If BIC is provided, it should be valid | Invalid Financial Institution BIC for <<party role>>  Given below are the list of Party Roles:  ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, ORDPTY, BENINS, RECVER |
| If Postal Address Country is provided, it should be a valid country code | Invalid Postal Address Country for <<party role>>  Given below are the list of Party Roles:  ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, ORDPTY, BENINS |
| If Account Currency is provided, it should be a valid currency code | Invalid Agent Account Currency for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN1, PRVIN2 |
| Maximum of three occurrences of service level code or proprietary information can be provided  For pacs.009, this validation is similar to what is done for pacs.008. Based on whether bank is GPI Enabled or not, maximum 2 or 3 occurrences are allowed) | Maximum 3 entry of service level is allowed |
| If Local Instrument information is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Local Instrument |
| If Category Purpose information is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Category Purpose |
| If Transaction Purpose information is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Purpose |
| If Account Identification Scheme related information is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Account Identification Scheme for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Account Type for the party role is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Account Type for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Account Proxy Type for the party role is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Account Proxy Type for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If either of Structured or Unstructured Postal Address information is provided, name should be provided for the party role | Name and Structured Address (at least Town Name and Country) or Unstructured Address should be present for <<party role>>  Given below are the list of Party Roles:  PRVINS, PRVIN2, PRVIN3, RECVER, INTINS, INTIN2, INTIN3, ORDPTY, ORDINS, ACWINS, BENINS |
| If Structured Postal Address details are provided, Town Name and Country are mandatory | For structured Postal Address, Town Name and Country must be present for <<party role>>  Given below are the list of Party Roles:  PRVINS, PRVIN2, PRVIN3, RECVER, INTINS, INTIN2, INTIN3, ORDPTY, ORDINS, ACWINS, BENINS |
| If Structured Postal Address details are provided (minimum Town Name and Country) Unstructured Postal Address (address lines) information is not allowed.  This validation is relevant only when Hybrid address is not enabled. Read [Support for Hybrid Address](#Hybrid) for more details. | No Postal Address Lines can be present if any fields of structured Postal Address information are present for <<party role>>  Given below are the list of Party Roles:  PRVINS, PRVIN2, PRVIN3, RECVER, INTINS, INTIN2, INTIN3, ORDPTY, ORDINS, ACWINS |
| Both Name and either of Postal Address structured (minimum of town name and country) or Unstructured Address (address lines) should be provided for ordering customer | Name and Either Structured or Unstructured Address should be present for the Ordering Customer record |
| The same code should not be repeated for instruction for creditor agent | Same code word should not be repeated for Instruction for Creditor Agent. |
| End to End Identification of the payment should not start or end with “/” and should not contain “//” | End to End identification cannot start or end with "/" and should not contain "//" |
| Clearing Member Id should not exceed 28 characters for any agent roles | ‘Clearing Member Id should not exceed 28 characters for <Role>” Party Roles: ORDINS, ACWINS, SENDER, INTINS, INTIN2, INTIN3, PRVINS, PRVIN1, PRVIN2, CHGPTY, RECVER |

[TARGET2 Specific Validations](#)

The following table lists the TARGET2 specific validations performed for bank transfers (pacs.009):

| Validation | Error Description |
| --- | --- |
| Transaction currency must be EUR | Invalid Transaction Amount Currency (must be EUR) |
| Instruction Information should be allowed only when code is PHOB in Instruction for *Creditor Agent* field | Instruction Information is allowed when code is PHOB |
| Instruction for next agent should not exceed 35 characters. | Max 35 characters allowed in each line of instruction information |
| For non-liquidity bank transfers, SBTI code should not be allowed in the *Local Instrument Code* field. | Local Instrument Code SBTI is not allowed for non-liquidity transfers |
| For all agent roles, if BIC is not present, then name and address (structured and unstructured) should be present. | If BIC is absent, Name & Structured address (atleast Country and Town Name) or Unstructured Address must be present for <party role>  RECVER, INTINS, INTIN2, INTIN3, BENINS , PRVINS, PRVINS2, PRVINS3, ORDPTY, ORDINS, CHGPTY, CHGPTY2, CHGPT3, CHGPT4, CHGPT5, ACWINS, SNDCBK, RCVCBK, TRMINS |

[Financial Institutions Direct Debit (pacs.010)](#)

Given below are the Common Validations and TARGET2 Specific Validations for Financial Institutions Direct Debit (pacs.010).

[Common Validations](#)

The following table lists the common channel validations performed for all ISO20022 (MX) based direct debit payments (pacs.010) including TARGET2 bank transfer payments.

| Validation | Error Description |
| --- | --- |
| If atleaset one record exists with PO.InstructionCode = 'TILLTIME' AND where PO.InformationCode = 'TIMIND', PO.InstructionCode = 'RJCTTIME' then an error should be raised | Till time and reject time are mutually exclusive |
| If XX-PARTY.ACCOUNT.LINE is present where  XX<PARTY.TYPE = 'Credit' XX-PARTY.ROLE = 'ORDINS' XX-ROLE.INDICATOR = 'G' or 'R' Then XX-IDENTIFIER.CODE or XX-CLEARING.MEMBER.ID must be present within same record | Creditor agent institution information must be present when Creditor agent account is present |
| For the following roles ORDINS, ORDPTY, DEBTOR, DBTAGT  If Postal Address Country (XX-COUNTRY) is present then it must exist in the ISO country table | Invalid country code for <<XX.PARTY.ROLE>> |
| For the following party roles: ORDINS  If IDENTIFIER.CODE (BIC) is not present then Name (NAME) and Unstructured Address line (ADDRESSLINE) OR Name (NAME) and Structured address (atleast Town Name (ADDRR.TOWN.NAME) and Country (COUNTRY)) must be present | No structured Postal Address information can be present if any fields of Postal Address Lines are present for party <XX-PARTY.ROLE> |
| For the following party role: ORDINS  If aatleast one occurance of unstructured Postal Address Lines (XX.ADDRESS.LINE) is present, then no structured address (XX-ADDR.DEPT, XX-ADDR.SUBDEPT, XX-ADDR.STREET.NAME, XX-ADDR.BLDG.NO, XX-ADDR.BLDG.NAME, XX-ADDR.BLDG.FLOOR, XX-ADDR.POST.BOX, XX-ADDR.ROOM, XX-ADDR.POST.CODE, XX-ADDR.TOWN.NAME, XX-ADDR.TOWN.LOCATON, XX-ADDR.DISTRICT, XX-ADDR.COUNTRY.SUB.DIV, XX-COUNTRY) may be present. | If 3rd IntermediaryAgent is present, then 2nd IntermediaryAgent must be present |
| For the following party role: ORDINS  If atleast one value in XX-XX.ADDRESS.LINE) is not present the minimum of Town name and country s ((XX-ADDR.TOWN.NAME and XX-COUNTRY) should be present. | No structured Postal Address information can be present if any fields of Postal Address Lines are present for party <XX-PARTY.ROLE> |
| For the following party roles: ORDPTY  If IDENTIFIER.CODE (BIC) is not present then Name (NAME) and Unstructured Address line (ADDRESSLINE) OR Name (NAME) and Structured address (atleast Town Name (ADDRR.TOWN.NAME) and Country (COUNTRY)) must be present | If BIC is absent, Name & Structured address (atleast Country & Town Name) or Unstructured Address must be present for <XX-PARTY.ROLE> |
| For the following party role: ORDPTY  If aatleast one occurance of unstructured Postal Address Lines (XX.ADDRESS.LINE) is present, then no structured address (XX-ADDR.DEPT, XX-ADDR.SUBDEPT, XX-ADDR.STREET.NAME, XX-ADDR.BLDG.NO, XX-ADDR.BLDG.NAME, XX-ADDR.BLDG.FLOOR, XX-ADDR.POST.BOX, XX-ADDR.ROOM, XX-ADDR.POST.CODE, XX-ADDR.TOWN.NAME, XX-ADDR.TOWN.LOCATON, XX-ADDR.DISTRICT, XX-ADDR.COUNTRY.SUB.DIV, XX-COUNTRY) may be present. | No structured Postal Address information can be present if any fields of Postal Address Lines are present for party <XX-PARTY.ROLE> |
| For the following party role: ORDPTY  If atleast one value in XX-XX.ADDRESS.LINE) is not present the minimum of Town name and country s ((XX-ADDR.TOWN.NAME and XX-COUNTRY) should be present. | No structured Postal Address information can be present if any fields of Postal Address Lines are present for party <XX-PARTY.ROLE> |
| For the following party roles: DEBTOR  If IDENTIFIER.CODE (BIC) is not present then Name (NAME) and Unstructured Address line (ADDRESSLINE) OR Name (NAME) and Structured address (atleast Town Name (ADDRR.TOWN.NAME) and Country (COUNTRY)) must be present | If BIC is absent, Name & Structured address (atleast Country & Town Name) or Unstructured Address must be present for <XX-PARTY.ROLE> |
| For the following party role: DEBTOR  If aatleast one occurance of unstructured Postal Address Lines (XX.ADDRESS.LINE) is present, then no structured address (XX-ADDR.DEPT, XX-ADDR.SUBDEPT, XX-ADDR.STREET.NAME, XX-ADDR.BLDG.NO, XX-ADDR.BLDG.NAME, XX-ADDR.BLDG.FLOOR, XX-ADDR.POST.BOX, XX-ADDR.ROOM, XX-ADDR.POST.CODE, XX-ADDR.TOWN.NAME, XX-ADDR.TOWN.LOCATON, XX-ADDR.DISTRICT, XX-ADDR.COUNTRY.SUB.DIV, XX-COUNTRY) may be present. | No structured Postal Address information can be present if any fields of Postal Address Lines are present for party <XX-PARTY.ROLE> |
| For the following party role: DEBTOR  If atleast one value in XX-XX.ADDRESS.LINE) is not present the minimum of Town name and country s ((XX-ADDR.TOWN.NAME and XX-COUNTRY) should be present. | No structured Postal Address information can be present if any fields of Postal Address Lines are present for party <XX-PARTY.ROLE> |
| For the following party roles: DBTAGT If IDENTIFIER.CODE (BIC) is not present then Name (NAME) and Unstructured Address line (ADDRESSLINE) OR Name (NAME) and Structured address (atleast Town Name (ADDRR.TOWN.NAME) and Country (COUNTRY)) must be present | If BIC is absent, Name & Structured address (atleast Country & Town Name) or Unstructured Address must be present for <XX-PARTY.ROLE> |
| For the following party role: DBTAGT  If aatleast one occurance of unstructured Postal Address Lines (XX.ADDRESS.LINE) is present, then no structured address (XX-ADDR.DEPT, XX-ADDR.SUBDEPT, XX-ADDR.STREET.NAME, XX-ADDR.BLDG.NO, XX-ADDR.BLDG.NAME, XX-ADDR.BLDG.FLOOR, XX-ADDR.POST.BOX, XX-ADDR.ROOM, XX-ADDR.POST.CODE, XX-ADDR.TOWN.NAME, XX-ADDR.TOWN.LOCATON, XX-ADDR.DISTRICT, XX-ADDR.COUNTRY.SUB.DIV, XX-COUNTRY) may be present. | No structured Postal Address information can be present if any fields of Postal Address Lines are present for party <XX-PARTY.ROLE> |
| For the following party role: DBTAGT  If atleast one value in XX-XX.ADDRESS.LINE) is not present the minimum of Town name and country s ((XX-ADDR.TOWN.NAME and XX-COUNTRY) should be present. | No structured Postal Address information can be present if any fields of Postal Address Lines are present for party <XX-PARTY.ROLE> |
| If InformationLine not blank where InformationCode = INSBNK InstructionCode = SVCLVL AND If InformationLine not blank where InformationCode = INSBNK InstructionCode = SVCLVLPY then raise error that either Coded or Proprietary form can be present | Either Coded or Proprietary form can be present for Service Level |
| If Transaction Purpose information is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Purpose |
| If InformationLine not blank where  InformationCode = INSBNK InstructionCode = LCLINSCD AND  If InformationLine not blank where InformationCode = INSBNK InstructionCode = LCLINSPY then raise error that either Coded or Proprietary form can be present | Either Coded or Proprietary form can be present for Local Instrument |
| If InformationLine not blank where InformationCode = INSBNK InstructionCode = CYPURPCD AND If InformationLine not blank  where InformationCode = INSBNK InstructionCode = CYPURPPY then raise error that either Coded or Proprietary form can be present | Either Coded or Proprietary form can be present for Category Purpose |

[TARGET2 Specific Validations](#)

The following table lists the TARGET2 specific validations performed for Financial Institutions direct debit (pacs.010).

| Validation | Error Description |
| --- | --- |
| Transaction currency must be EUR | Invalid Transaction Amount Currency (must be EUR) |

## Support for Hybrid Address

As an interim step in transitioning from structured to unstructured addresses, TARGET2 supports for Hybrid address from NOV.2025 release onwards. Hybrid address is a combination of structured address fields and unstructured address fields, with only the town name and country being mandatory. The support of hybrid address applies to all party and agent roles including those within Remittance Information and Related Remittance Information.

The user can enable the support for hybrid address by setting the *Address Type* field in Clearing module to Hybrid, Str, Unstr. Read [Configuring Clearing](../../../../Payments/PP/Payments_Hub_(PP)/Clearing/Configuration.htm) for more details.

Once Hybrid address is enabled,

- User is allowed to have both structured and unstructured elements in the address fields.
- Mutual exclusivity validation between presence of structured and unstructured is disabled in this mode.

The bank (beneficiary account information capturing systems) or customer should ensure that the address details available in the structured address and unstructured address line fields are not duplicated while using hybrid address. Temenos does not validate these duplicated addresses.

In this topic

- [Introduction to TARGET2 RTGS (ISO20022)](#IntroductiontoTARGET2RTGSISO20022)

- [Types of Participants](#TypesofParticipants)
- [Payment Instruments](#PaymentInstruments)
- [Types of Messages](#TypesofMessages)
- [Payment Direction](#PaymentDirection)
- [TARGET2 Payment Capture](#TARGET2PaymentCapture)
- [TARGET2 Payment Repair](#TARGET2PaymentRepair)
- [TARGET2 ISO20022 Message Structure](#TARGET2ISO20022MessageStructure)
- [Supported Message Elements in TARGET2 ISO20022 Payments](#SupportedMessageElementsinTARGET2ISO20022Payments)
- [Supported Characters for ISO Message](#SupportedCharactersforISOMessage)
- [Data Enrichment for MT and MX Format Conversion](#DataEnrichmentforMTandMXFormatConversion)
- [Acknowledgements](#Acknowledgements)
- [Returns](#Returns)
- [Recall](#Recall)
- [Cover Processing](#CoverProcessing)
- [Business Day](#BusinessDay)
- [Bank Identifier Code (BIC)](#BankIdentifierCodeBIC)
- [Message Priority](#MessagePriority)
- [Clearing Directory and Reachability](#ClearingDirectoryandReachability)
- [Payment Product for Processing TARGET2 Payments](#PaymentProductforProcessingTARGET2Payments)
- [Charge Processing](#ChargeProcessing)
- [Forex (FX)](#ForexFX)
- [Code Word](#CodeWord)
- [Duplicate Check](#DuplicateCheck)
- [Financial Action Task Force (FATF) Regulation](#FinancialActionTaskForceFATFRegulation)
- [Filtering (Sanction Screening)](#FilteringSanctionScreening)
- [Booking](#Booking)
- [Message Flow](#MessageFlow)
- [Liquidity Transfer Advice](#LiquidityTransferAdvice)
- [Liquidity Transfer Request](#LiquidityTransferRequest)
- [Multi-addressee Participants](#MultiaddresseeParticipants)
- [Channel Validation](#ChannelValidation)
- [Support for Hybrid Address](#SupportforHybridAddress)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:20:47 PM IST