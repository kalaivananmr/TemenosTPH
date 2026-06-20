# Introduction to SWIFT MX

> Source: https://docs.temenos.com/docs/Solutions/Payments/International_Payments/PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   SWIFT MX > Introduction

- SWIFT MX;)
  - [Introduction](../../International_PaymentsCBPR/PPSWMX/Introduction.htm)
  - [Configuration](../../International_PaymentsCBPR/PPSWMX/Configuration.htm)
  - [Working with](../../International_PaymentsCBPR/PPSWMX/Workingwith.htm)
  - [Tasks](../../International_PaymentsCBPR/PPSWMX/Tasks.htm)
  - [Outputs](../../International_PaymentsCBPR/PPSWMX/Outputs.htm)

Payments

# Introduction to SWIFT MX

Updated On 12 April 2026 |
 424 Min(s) read

Feedback
Summarize

Temenos Payments Hub (TPH) supports International Payments, which is used to transfer funds between customers and banks across different countries in different currencies through the SWIFT based banking system. International transfers are also referred as cross border payments.

Banks perform international transfers using the SWIFT network using BIC (Bank Identifier Code). A BIC is a SWIFT address assigned to a bank to send or receive payment orders over the SWIFT network. The payment orders are sent in the format defined by SWIFT. SWIFT does not facilitate transfer of funds, it just transfers the payments orders between banks, which must settle the payment using correspondent accounts they maintain with each other. Therefore, to send or receive international payments and settle, banks are required to maintain relationship with other banks. Based on the relationship, payments can be sent or received directly between two banks or can be routed through intermediate banks. Therefore, an international payment instruction may flow from the sender to receiver through multiple parties or banks, each identified using BIC.

ISO20022 is a global standard for financial messaging, which provides a standard model across business domains such as Payments, Securities, Trade Services, and so on. SWIFT is migrating cross border payments from existing MT to MX (ISO20022) message standard. There is a co-existence period, where both MT and MX formats are supported to allow participant members to switch over. At the end of the co-existence period, the existing MT format is decommissioned and only MX format is supported.

The CBPR+ (Cross-Border Payments and Reporting Plus) working group is responsible for defining the MX message formats and usage guidelines (available in SWIFT CBPR+ portal).

Temenos Payments Hub support processing of cross border international payments using SWIFT MX (ISO20022) messages.

PPSWCQ module in TPH is compliant to CBPR+ User Handbook SR 2026 Edition.

## Co-existence of MT and MX Format for SWIFT Cross Border Payments

The financial institutions transacting cross border international payments through SWIFT need to upgrade their payment processing systems to support SWIFT CBPR+ MX (ISO20022) message processing. The timeline for SWIFT’s migration is November 2022. However, the migration is not big bang. There will be a three years co-existence phase for both existing MT and new MX format till 2025.



It means all the SWIFT participant financial institutions can receive and process MX messages from November 2022 (in addition to existing MT messages). Financial institutions can decide whether they want to send out cross border payments using MT or MX format during the co-existence phase. After the co-existence phase ends in 2025, financial institutions can send and receive only MX messages. MT messages will no longer be supported.

## Message Types

The following table lists the SWIFT CBPR+ messages supported.

| ISO20022 MX Message | Message Type | MT Equivalent | Module Code | Outward | Inward | Redirect |
| --- | --- | --- | --- | --- | --- | --- |
| pacs.008.001.08 | Single Customer Credit Transfer | MT103 | PPSWMX |  |  |  |
| pacs.008.001.08  STP | Single Customer Credit Transfer | MT103+ | PPSWMX |  |  |  |
| pacs.009.001.08 | Single Financial Institution Credit Transfer | MT202  MT200 | PPSWMX |  |  |  |
| pacs.009.001.08 | Single Financial Institution Credit Transfer (Cover) | MT202 COV | PPSWMX |  |  |  |
| pacs.009.001.08 ADV | Single Financial Institution Credit Transfer Pre Advice |  | PPSWMX |  |  |  |
| pacs.004.001.09 | Single Payment Return |  | PPSWMX |  |  |  |
| pacs.002.001.10 | Payment Status Report |  | PPSWMX |  |  | × |
| camt.054.001.08 | Bank to Customer Debit Credit Notification | MT900 | PPSWMX |  | × | × |
| camt.054.001.08 | Bank to Customer Debit Credit Notification | MT910 | PPSWMX |  |  | × |
| camt.057.001.06 | Notification to Receive | MT 210 | PPSWMX |  |  | × |
| camt.056.001.08 | Payment Cancellation Request | MT192 | PPSWMX  PPSWCR |  |  | × |
| camt.029.001.09 | Resolution of Investigation | MT196 | PPSWMX  PPSWCR |  |  | × |
| camt.055.001.08 | Customer Payment Cancellation Request | - | PPSWMX  PPSWCR | × |  | × |
| pain.001.001.09 | Customer Credit Transfer Initiation | MT101 | PPSWMX | × |  | × |
| pain.002.001.10 | Interbank Customer Payment Status Report | X | PPSWMX |  | × | × |
| camt.107.001.01 | Cheque Presentment Notification | MT110 | PPSWMX  PPSWCQ |  | × | × |
| camt.106.001.02 | Charge Payment Request | MT191 | PPSWMX  PPSWCL |  |  | × |
| admi.024.001.01 | Notification of Correspondence | MT199 | PPSWMX |  |  | × |

Read [SWIFT MX Cancellations and ROI (PPSWCR)](../../../PPSWCR/International_PaymentsCBPR/PPSWCR/Introduction.htm) to know more about the processing of Cancellation Request and ROI (camt.055, camt.056, camt.029).

Read [SWIFT MX Cheques (PPSWCQ)](../../../PPSWCQ/International_PaymentsCBPR/PPSWCQ/Introduction.htm) to know more about the processing of Cheque Presentment Notification (camt.107).

Read [SWIFT MX Claims and Charges (PPSWCL)](../../../PPSWCL/International_PaymentsCBPR/PPSWCL/Introduction.htm) to know more about the processing of Charge Payment Request and Notification (camt.106, camt.105).

Read [SWIFT SSI File Upload (PPSSIU)](../../../PPSSIU/International_PaymentsCBPR/PPSSIU/Introduction.htm) to know more about SSI upload.

- Temenos Payments Hub support processing of CBPR+ messages with single payment information. Temenos Payments Hub does not support processing of bulk payments (single message with multiple payment information).
- camt.025.001.08 (Receipt) is considered as out of scope for now.

## Related Features

Account statements are available in Temenos Transact under a separate license (IZ module). This is an optional module that banks can deploy if they require the system to produce SWIFT CBPR+ compliant Account Statements.

An optional connector to SWIFT through SWIFT Interact is also available under a separate license (SWFTAL).

Bank must have PP, and PH licenses as part of the Routing and Settlement (R&S) selection of currency correspondent. In addition, the bank must also have a PPSSIU license for uploading SSI files.

The following SWIFT CBPR+ messages are available in Temenos Transact under IZ module.

| ISO20022 MX Message | Description | MT Equivalent | Outward | Inward |
| --- | --- | --- | --- | --- |
| camt.052.001.08 | BankToCustomerAccountReport | MT941  MT942 |  | × |
| camt.053.001.08 | BankToCustomer Statement | MT940  MT950 |  | × |
| camt.054.001.08 | Account Report | MT900, MT910 |  | × |

## Payment Types

The system supports the following types of cross border international payment

| Payment Type | Description |
| --- | --- |
| Customer Transfer | - A customer transfer is a payment in which the ordering customer or the beneficiary customer or both are non-financial institutions.   - SWIFT supports both serial and cover method for customer transfer.   - pacs.008 and pacs.008 STP are the SWIFT CBPR+ messages used for serial customer transfer.   - pacs.008 and pacs.009 COV are the SWIFT CBPR+ messages used for customer transfer settled using cover. Here, pacs.008 is the direct or announcement message and pacs.009 COV is the cover which transfer the funds via reimbursement agents.   - Allows only single transaction per message. |
| Bank Transfer | A bank transfer is a payment in which the ordering institution and the beneficiary institution are both financial institutions.   - SWIFT supports both serial and cover method for bank transfer. - pacs.009 and pacs.009 COV are the SWIFT CBPR+ messages used for bank transfer and cover. - pacs.009 pre-advice is used as a pre-advice notification for bank transfer settled with cover. - pacs.009 ADV and pacs.009 are the SWIFT CBPR+ messages used for bank transfer with a pre-advice. Here, pacs.009 ADV is the direct or announcement message and pacs.009 is the message used to transfer the funds through reimbursement agents. The message used is pacs.009 and not pacs.009 COV (as pacs.009 COV is applicable only for customer transfer settled using cover). - Allows only single transaction per message. |
| Return Payment | SWIFT participant banks can return an incoming payment to the sender when,   - incoming payment cannot be processed successfully due to errors (such as creditor account is closed). - there is a cancellation request for the transaction. - the creditor wants to return the completed payment.   pacs.004 is the SWIFT CBPR+ message used for return, which allows only single transaction per message. |
| Foreign Currency cheques | FCY cheque is issued by drawer bank at the request of the payer favouring payee (Beneficiary).   - Swift supports ChequePresentmentNotification, that is, the message is sent by a drawer bank or a bank acting on behalf of the drawer bank to the bank on which a cheque has been drawn (the drawee bank). - camt.107 is the SWIFT CBPR+ message used for ChequePresentmentNotification. - ChequePresentmentNotification is restricted to a single cheque per message. |

## Payment Direction

Depending on the direction of flow of the funds, the system supports processing of following types of cross border international payments:

| Payment Type | Description |
| --- | --- |
| Incoming | The originating party (Debtor) of the payment does not reside in the processing bank’s ledger. The beneficiary party (Creditor) of the payment resides in the processing bank’s ledger. |
| Outgoing | The originating party (Debtor) of the payment resides in the processing bank’s ledger. The beneficiary party (Creditor) of the payment does not reside in the processing bank’s ledger. |
| Redirect | Neither the originating party (Debtor) nor the beneficiary party (Creditor) of the payment resides in the processing bank’s ledger. |

## Configurable Support for SWIFT MT or MX format to Send Cross Border Payments

To support co-existence of both MT and MX messages for cross border international payment, Temenos Payments Hub is enhanced to:

- Receive and process cross border payments using both MT and MX messages
- Configure company properties to decide if the bank wants to send out cross border payments using SWIFT MT format or MX format. SWIFT payments are routed using LORO or NOSTRO or Account channel. The user can configure this by setting a date in the *SWIFTMX Effective Date* field in the Company Properties. For more information, see Sending SWIFT Cross Border Payments in MX format (ISO20022).

Therefore, if the financial institution is migrating to SWIFT MX, then they should configure the migration date in the above mentioned field. If the financial institution is not migrating to SWIFT MX, then they should configure the migration date as blank. This configuration is referred for both outgoing and redirected cross border payments.

The following table shows how the *SWIFTMX Effective Date* field is considered to determine the outgoing message format for payments initiated in the system.

| Configuration in Company Properties | Message Format |
| --- | --- |
| Effective date is configured. The current business date is greater than or equal to the effective date. | Company is configured to send cross border payments in MX format. |
| Effective date is configured. The current business date is less than the effective date. | Company is configured to send cross border payments in MX format at a future date. Until the future date is reached, MT messages are sent. |
| Effective date is not configured (blank). | Company is configured to send cross border payments in MT format. |

The system can also redirect cross border payments through SWIFT based local RTGS clearings (for example, TARGET2, CHAPS and so on). These SWIFT based RTGS systems can either use MT format or MX format. For such redirections through the clearings, the system refers to the *SWIFT Based* and *Effective Date* fields configured at the clearing level in the PP.CLEARING application to decide whether to send the message in MT or MX format.

The following table shows how the *SWIFT Based* and *Effective Date* fields configured in clearing is considered to determine the outgoing message format for the clearing.

| Configuration in Clearing (PP.CLEARING application) | Message Format |
| --- | --- |
| The *Swift Based* field is configured as MX  The *Effective Date* field is blank | Clearing is configured to send messages in MX format |
| The *Swift Based* field is configured as MX  The *Effective Date* field is configured and the current business date is greater than or equal to the effective date | Clearing is configured to send messages in MX format |
| The Swift Based flag is configured as MX  The *Effective Date* field is configured and the current business date is less than the effective date | Clearing is configured to send messages in MX format at a future date.  Until the future date is reached, MT messages are sent. |
| The Swift Based flag is configured as Y  Effective Date is blank | Clearing is configured to send messages in MT format |

Based on the above mentioned configurations in company properties and clearing level, the system supports the following message conversions:

| MT to MX | MX to MT |
| --- | --- |
| - MT 103 to pacs.008 - MT 101 to pacs.008 - MT 202 to pacs.009 - M 202 COV to pacs.009 COV | - pacs.008 to MT103 - pacs.009 to MT202 - pacs.009 COV to MT202 COV - pain.001 to MT103 |

[Outgoing Scenario](#)

The following table shows the outgoing message format for cross border customer payments captured or initiated from the system.

| Company Configuration | Message Direction | Outgoing Message Type |
| --- | --- | --- |
| Company configured to send cross border payments in MX format | Outgoing | CBPR+ pacs.008  CBPR+camt.107 (cheque presentation notification) CBPR Pacs.009, Pacs.004, Pacs.002 and so on |
| Company configured to send cross border payments in MX format at a future date | Outgoing | MT 103 until future date  CBPR+ pacs.008 after future date  CBPR+camt.107 (cheque presentation notification on or after future date) |
| Company configured to send cross border payments in MT format | Outgoing | MT103  MT110 (Advice of Cheques) |

[Redirection Scenario](#)

For redirection scenarios, if the system receives the incoming message in MT format (for example – MT103 or MT202) and the message need to be redirected in MX format (for example – pacs.008 or pacs.009), then the system performs additional enrichments to ensure that the data is properly mapped. The same is applicable when incoming message is received in MX format and redirected in MT format.

[Redirection through Correspondent Bank](#)

The following table shows the outgoing message format for redirected cross border customer payments through the correspondent bank.

| Company Configuration | Message Direction | Incoming Message Type | Outgoing Message Type |
| --- | --- | --- | --- |
| Company is configured to send cross border payments in MX format | Redirect | MT103 | CBPR+ pacs.008 |
| Redirect | CBPR+ pacs.008 | CBPR+ pacs.008 |
| Company is configured to send cross border payments in MX format at a future date | Redirect | MT103 | MT103 until future date  CBPR+ pacs.008 after future date |
| Redirect | CBPR+ pacs.008 | MT103 until future date  CBPR+ pacs.008 after future date |
| Company is configured to send cross border payments in MT format | Redirect | MT103 | MT103 |
| Redirect | CBPR+ pacs.008 | MT103 |

When the system receives incoming payments from a SWIFT based RTGS clearing (for example, TARGET2, CHAPS and so on) and the payments need to be redirected through SWIFT using MT or MX format, the system refers to the above mentioned configuration (in company properties level).

[Redirection through SWIFT based RTGS Clearings](#)

When the system receives incoming cross border payments from SWIFT in MT or MX format and the payments need to be redirected through a SWIFT based RTGS clearing (for example, TARGET2, CHAPS and so on), the system refers to the clearing level configurations.

| Clearing Configuration | Message Direction | Incoming Message Type | Outgoing Message Type |
| --- | --- | --- | --- |
| Clearing is configured to send messages in MX format | Redirect | MT103 | pacs.008 (Clearing format) |
| Redirect | CBPR+ pacs.008 | pacs.008 (Clearing format) |
| Clearing is configured to send messages in MT format | Redirect | MT103 | MT103  (Clearing format) |
| Redirect | CBPR+ pacs.008 | MT103  (Clearing format) |
| Clearing is configured to send MX messages in future | Redirect | MT103 | MT103 (Clearing format) until future date  pacs.008 (Clearing format) after future date |
| Redirect | CBPR+ pacs.008 | MT103 (Clearing format) until future date  pacs.008 (Clearing format) after future date |

## CBPR+ Payment Capture

The system provides the following options to capture and initiate outgoing SWIFT CBPR+ payments.

[Payment Order](#)

The front office users can capture outgoing cross border international payment using the PAYMENT.ORDER (`PO`) application. The system provides a dedicated menu to capture payments. The following screens have the relevant ISO20022 fields.

- CBPR+ Customer Transfer – On successful processing, outgoing CBPR+ pacs.008 message is generated
- CBPR+ Bank Transfer – On successful processing, outgoing CBPR+ pacs.009 message is generated
- CBPR+ ChequePresentationNotification: A bank user can initiate a foreign currency (FCY) draft request favouring payee (Beneficiary) based on payer's (TPH customer) instruction. On successful processing, outgoing CBPR+ camt.107 message is generated

Dedicated payment order products are provided for CBPR+ customer and bank transfer.

Read the [Working with SWIFT MX](Workingwith.htm)  topic for more details on the fields available in the respective payment order screens.

[Order Entry](#)

The back office users can capture cross border international payment using the Order Entry (OE) screen. The system provides generic menus to capture ISO20022 format payments, such as SWIFT CBPR+, TARGET, SIC, CHAPS, and so on. The following screens have the relevant ISO20022 fields.

| Process | Screens |
| --- | --- |
| Outgoing Payment Capture | - Outgoing ISO Customer Transfer – On successful processing, CBPR+ pacs.008 (serial or cover) message is generated - Outgoing ISO Bank Transfer – On successful processing, CBPR+ pacs.009 (serial or cover) message is generated - Outgoing ISO Own Account Transfer – On successful processing, CBPR+ pacs.009 message is generated |
| Incoming Payment Capture | The system provides the following menus to manually capture incoming ISO format payments (for exceptional scenarios, where STP capture is not possible). These screens have the relevant ISO20022 fields.   - Incoming ISO Customer Transfer – The user can capture an incoming customer payment details manually and post accounting entries - Incoming ISO Bank Transfer – The user can capture an incoming bank payment details manually and post accounting entries   Routing agent details are not captured in the screen while manually creating incoming payments. |

Read the [Working with SWIFT MX](Workingwith.htm)  topic for more information on the fields available in the respective Order Entry (OE) screens.

[Delivery Preview of Outgoing Payment](#)

When the user captures an outgoing payment in the system using OE screens, the system provides an option to view the expected XML message to be generated by the system, based on the data captured. This feature is called delivery preview.

To view the expected XML message,

1. Capture and validate the payment details to ensure that there are no errors.
2. Click the Delivery Preview option. A new screen displays with the expected XML message.

The preview shows the payload without any business application header or technical header. In case of any payload XSD validation error, the error is displayed at the end of the message

- This option is applicable for single messages only, not applicable for bulk payments.
- This option is applicable for CBPR+ payments as well as SWIFT MX based RTGS payments (such as TARGET2) captured from the OE screen.

[Initiation using pain.001](#)

The system supports initiation of customer payment using pain.001 and Customer Status Report using pain.002 (v10).

pain.001 (v9) can be received through client channels as well as from corporates or financial Institutions through SWIFT (CBPR+). There are separate XSDs configured in the system in different path for pain.001 through client and SWIFT channel. The system has the ability to validate against corresponding XSD based on the input folder from which the message is picked up.

CBPR+ pain.001 (v9) is the MX format for MT101.

[pain.001 v9 through SWIFT Channel (CBPR+)](#)

During transaction processing as done for a MT101, the system performs the debit authority and netting agreement check (based on configuration) to validate whether the sending institution or organisation of the CBPR+ pain.001 message (BAH > From > Organisation Identification > Financial Institution Identification BICFI) has the right to send customer initiation message on behalf of the debtor.

In addition to the incoming message type (pain.001) and the sending bank BIC, the name and account line (if defined in the Netting Agreement table) are also matched with the name (Payment Information > Debtor > Name) and account number (Payment Information > Debtor Account > Identification > IBAN (or) Other > Identification) as specified in the received payment instruction.

- The Netting Agreement configuration can be specified with the incoming message type and the sending bank BIC that must be allowed. The agreement can be made more specific by also including account number and the name of the customer.
- A default record is released in NODA List for message type 'pain.001SW - SWIFT Credit Transfer Initiation'.
- If the bank intends to perform message validation and processing using netting agreement specific to SWIFT pain.001, the user can create netting agreement with *Incomingmessagetype* as 'pain.001SW - SWIFT Credit Transfer Initiation' and reverse the pain.001SW record in NODA list. Refer [Debit Authority](Configuration.htm#Debit) configuration for more information.

In case, the bank does not wish to do debit authority or netting agreement check for the pain.001 message, this can be achieved through the configuration in the NO.DA.LIST table. If the configuration is found for the message type in NO.DA.LIST, then default netting agreement record is checked and the message is processed based on the default record.

Refer to the [Debit Authority](Configuration.htm#Debit) section for more details.

If the debit authority check fails, the system routes the payment to repair. Refer to the [CBPR+ Payment Repair](#CBPR+) section for more details.

- pain.001 message can result in book transfer or outgoing customer transfer. The outgoing channel is picked up based on the existing product configuration and routing channel.

The system can receive customer initiation message MT101 and pain.001 (v9) from SWIFT channel, which can be routed as a MT or MX message based on the company configuration.

- CBPR+ also supports pain.001 relay messages, where initiating party (the Debtor or authorised party) sends the pain.001 message to the Forwarding Agent. The Forwarding Agent acts as a concentrating financial institution and forwards the payment initiation request message to the Debtor Agent. However, Temenos Payments Hub does not support this relay functionality as a forwarding agent.

[Message Elements Supported in CBPR+ pain.001](#)

Refer to the [Message Elements Supported in SWIFT CBPR+ Payments](#Supporte) section for more details on the message elements for pain.001.

Below are exceptions from the mentioned supported elements and their rules in a CBPR+ pain.001.

- For the roles such as Debtor, Debtor agent, Intermediary agent 1, Intermediary agent 2, Intermediary agent 3, Creditor Agent, and Creditor, the structured address tags (like Town Name and Country) can also be available along with unstructured address (Address Lines 1 & 2) in pain.001v9. When Temenos Payments Hub receives the pain.001 message with
  - **Town Name, Country, and Address Line** - The system processes the message and maps hybrid address in the outgoing message.
  - **Town Name, Country, and Other Structured Address fields** - The system processes the message and maps structured address in the outgoing message.

  Refer to [Hybrid Address Support](#Hybrid) for further details on mapping of address details.
- Both Related Information and Remittance Information are allowed in pain.001 v9. If both information are received in the incoming message and if the payment is routed through SWIFT CBPR+ or MX based channels, Temenos Payments Hub currently routes the payment to repair queue because of the common ISO validation present in the system that does not allow Related and Remittance information to be present at the same time. The user has to only cancel the payment manually from repair queue as these fields are not editable from the repair screen.

The tags below are not applicable for pain.001:

- Settlement Method
- Settlement Account
- Transaction Identification
- Settlement Priority
- Clearing Channel
- Settlement Time Indication
- Settlement Time Request
- Instruction for Next Agent

The additional elements that are specific to pain.001 message are described below.

[Forwarding Agent](#)

Forwarding Agent acts as a concentrating financial institution in a pain.001 relay scenario and forwards the pain.001 message to the Debtor Agent for execution. This role is applicable for customer transfer initiated using pain.001 message and is mandatory in a relay scenario, whereby the Initiating Party (the Debtor or authorised third party) provides Business Identifier Code (BIC FI) of the Forwarding Agent in the original pain.001 message.

Other options to identify the Forwarding Agent include:

- Clearing System Member ID
- LEI (Legal Entity Identifier)

When the user receives an incoming CBPR+ Credit Transfer customer initiation message pain.001, the forwarding agent details are stored in the system. The FWDAGT party role is used to store and map forwarding agent details. Temenos Payments Hub does not support this relay functionality as a forwarding agent. This agent details are not displayed in the ISO view or repair screens as individual fields but the user can see this information as part of the received message (as XML).

Refer to the [Viewing SWIFT CBPR+ pain.001](Workingwith.htm#Viewing) section for more information.

**Rules**

- If forwarding agent BIC is provided, then LEI or Clearing system member ID are optional.
- If forwarding agent LEI is provided, then it must adhere to the LEI format.

[Authorisation Code](#)

The Initiating Party can specify the authorisation level for the payment initiation request (/Document/CstmrCdtTrfInitn/GrpHdr/Authstn/Cd). The allowed values are as follows:

| Value | Description |
| --- | --- |
| AUTH | Pre-authorised file. Indicates that a file has been pre-authorised or approved within the originating customer environment and no further approval is required. |
| FDET | File Level Authorisation Details. Indicates that a file requires additional file-level approval with the ability to view both the payment information block and supporting customer credit transaction details. |
| FSUM | File Level Authorisation Summary. Indicates that a file requires additional file-level approval with the ability to view only the payment information block-level information. |
| ILEV | Instruction Level Authorisation. Indicates that a file requires all customer transactions to be authorised or approved. |

Temenos Payments Hub supports payment processing based on Authorisation code (Document > Group Header > Authorisation > Code) as AUTH only. When codes FDET, FSUM, ILEV are received, the payments are processed same as AUTH and does not involve any special approval processing.

[Payment Method (CHK)](#)

In CBPR+ pain.001 (v9), the initiating party can instruct to do the payment using cheque method. When Temenos Payments Hub receives the payment method as ‘CHK’ (Document > Group Header > Payment Information > Payment Method > ’CHK’), for book payment, it is routed to the repair queue as the creditor account is not present in the message. For outgoing payment, the payment is processed successfully as if TRF payment method is received.

[Instruction for Debtor Agent](#)

This specifies textual information related to processing of payment, provided by the initiating party and intended for the debtor agent. This is applicable only for the pain.001 message. This information can be present in <PmtInf> or in <CdtTrfTxInf> level. The debtor agent may want to refer to the instruction before processing or may overlook it and process in STP. Therefore, if instruction for Debtor Agent is received, the system stores it as a code word with a dummy information and instruction code.

- Information code = INSBNK
- Code word = DBTRAGT
- Code word text = <received instruction information>

This allows the bank users to configure code word processing and influence the payment processing based on textual instruction received, such as:

- Process the payment NON STP
- Change the priority
- Add a specific code word in the outgoing message

This information is not displayed in ISO view and repair screen as an individual field but the user can view this information as part of the received message (as XML).

Refer to the [Viewing SWIFT CBPR+ pain.001](Workingwith.htm#Viewing) section for more information.

The priority to map Instruction for Debtor Agent from the incoming CBPR+ pain.001 message should be:

- Payment Information > Instruction For Debtor Agent
- If the above tag is not present, use Payment Information > Credit Transfer Transaction Information > Instruction For Debtor Agent.

This information is not sent out in the generated outgoing customer payment.

[Charges Account and Charge Account Agent](#)

The initiating party can specify the charge account details in the incoming pain.001 message. Along with charge account, pain.001 may also contain details of the charge account agent to indicate that the charge account is in the debtor agent processing pain.001 or in another bank. Charges account agent in pain.001 is only to be used when the charges account agent is different from the debtor agent.

Temenos Payments Hub stores the charge account agent information and all fields of the charge account received in pain.001 message. Though the system saves all information of charge account, it uses only the charge account number from the message as the debit charge account for debiting the charges (if any) based on the charge account agent value as mentioned below.

- If the charge account is received in the message and it belongs to processing bank (Charge account agent in pain.001 is blank), the system imposes this as charge account for deducting charges (if applicable) during processing of the payment.
- If the charge account does not belong to processing bank (charge account agent is different bank), the system determines the charge account as per the client agreement configuration.

Temenos Payments Hub does not support the functionality of deducting charges from an account in a different bank.

This information is not sent out in the generated outgoing customer payment.

[Pooling Adjustment Date](#)

The Initiating Party sends the Pooling Adjustment Date in the pain.001 (V9) tag (/Document/CstmrCdtTrfInitn/PmtInf/PoolgAdjstmntDt). This specifies the date used for the correction of the value date of a cash pool movement that has been posted with a different value date. Temenos Payments Hub does not do any processing based on this tag. If received, this value is not stored in Temenos Payments Hub but the user can view as part of the received message (as XML).

Refer to the [Viewing SWIFT CBPR+ pain.001](Workingwith.htm#Viewing) section for more information.

[Cheque Instruction](#)

In the pain.001 message, the initiating party can choose to instruct bank to pay a certain amount of money from one person to another person through cheque (Payment method > CHK). For such cheque instructions, the type of cheque that needs to be issued to the Creditor can be specified in the message tag (/Document/CstmrCdtTrfInitn/PmtInf/CdtTrfTxInf/ChqInstr/ChqTp).

This information along with all other information under the tag ChqInstr is stored as an XML file (BLOB) in Temenos Payments Hub only for informational purpose. No processing is done on this data in Temenos Payments Hub. This information is not displayed in the ISO view or repair screens as individual fields but the user can view this information as part of the received message (as XML).

Refer to the [Viewing SWIFT CBPR+ pain.001](Workingwith.htm#Viewing) section for more information.

[Tax](#)

The Initiating Party sends the tax related information when the tax information is used by the Clearing or the local regulatory authority. This information is applicable for pain.001 message (tag /Document/CstmrCdtTrfInitn/PmtInf/CdtTrfTxInf/Tax). Temenos Payments Hub stores the tax information as an XML file (blob). No processing is required based on this. This information is not displayed in the ISO view or repair screens as individual fields but the user can view this information as part of the received message (as XML).

Refer to the [Viewing SWIFT CBPR+ pain.001](Workingwith.htm#Viewing) section for more information.

[Equivalent Amount](#)

The Equivalent Amount nested element captures currency and amount of money to be moved between the Debtor and Creditor, before the deduction of charges, and is expressed in the currency of the Debtor's account. The Currency Of Transfer element captures the equivalent currency to be transferred, which the first agent converts the credit transfer into.

Temenos Payments Hub does not support processing of payment based on the equivalent amount. If it is received in the pain.001 message, the system routes the payment to repair and the user has to manually cancel this payment from the repair queue as the *Instructed Amount* and *Currency* fields are not editable in the repair screen.

[Instructed Amount](#)

The Instructed Amount captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.

Temenos Payments Hub maps this information into transaction amount and currency.

## CBPR+ Payment Repair

The system provides ISO view and repair screens with relevant fields for viewing and repairing payments sent or received using ISO20022 format. SWIFT CBPR+ payments are repaired using the ISO repair screen.

The system moves the incoming, outgoing, or redirected SWIFT CBPR+ payments having active functional or technical error to repair status (235). The users can open such payments using the **Pending Repair** enquiry (Read the [Working with SWIFT MX](Workingwith.htm)  for more information) for viewing or modification (repair). In view mode, all the fields are displayed as read-only whereas in repair mode, the selected fields are editable (for which repair is allowed).

Modification is not allowed for debtor, ultimate debtor, ultimate creditor, creditor, debtor agent, and previous instructing agent details in repair mode.

The user can modify the details and validate the payment with modified details. If all validations are successful, then the user can commit the payment for further processing with the repaired details.

For a SWIFT CBPR+ payment in repair mode, the user can modify the following fields.

- Instruction Priority
- Output Channel
- Instructed Agent Details (BIC, Clearing System ID and Clearing Member ID)
- Credit Account
- Debit/Credit side FX rates (Customer Spread, Treasury Rate, Exchange Rate)
- Requested Execution Date
- Debit and Credit Value Date
- Charge Information
- Routing Information (BIC, Clearing System ID and Clearing Member ID, Name, LEI, Account Number, and Address details) for following agents
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
  - Next Agent Clrg. Channel Type
  - Instruction for Next Agent
  - Time Indication
- Regulatory Reporting Information
- Unstructured Remittance Information

## SWIFT CBPR+ Message Structure

The following diagram shows the structure of a SWIFT CBPR+ MX (ISO20022) message sent across SWIFT network using the FINPlus service.

/Introduction_1.png)

The RequestPayload section contains the business information consisting of following blocks:

| Block | Description |
| --- | --- |
| Application Header | It contains the business application header (BAH) |
| Document | It contains the actual business message (such as pacs.008, pacs.009, pacs.004 and so on) |

The RequestHeader section contains the details required to transport the request payload over a network provider. This is also referred as technical header.

Temenos Payments Hub support generation of the message containing the Technical Header, Business Application Header and the underlying document for sending the message over SWIFT.

[Document](#)

The Document block contains information about the actual business message. It consists of two sections:

The first section is Group Header, which contains common details applicable for the underlying business message. Some of the important fields in the Group Header section are:

| Field | Description |
| --- | --- |
| *Message Identification* | This is a unique identification for the business message. For CBPR+ messages, the system populates a unique identification. |
| *Creation Date Time* | The system populates the date and time when the XML document is created |
| *Number Of Transaction* | Indicates the number of transaction details in the business message. SWIFT allows only single transaction details to be sent or received using CBPR+ message formats. Hence, this field must always have value as 1 (single transaction details) |
| *Settlement Information* | Applicable for customer and bank transfer (including returns). This section is used to provide information on the following:   - Settlement Method – The system determines and populates INGA or INDA or COVE for CBPR+ transactions. - Settlement Account – The system populates settlement account to be used by the receiver for debiting the sender - Instructing / Instructed / Third Reimbursement Agents – The system populates reimbursement agents for customer payments settled using the cover method. These are not applicable for serial payments. |

The second section contains information about the business message such as:

| Block | Description |
| --- | --- |
| Credit Transfer Transaction Information | Contains details of the transaction for customer transfer (pacs.008) and bank transfer (pacs.009) or cover (pacs.009 COV) or bank transfer pre-advice (pacs.009 ADV) |
| Transaction Information | Contains details of return transaction (pacs.004) |
| Notification | Contains information regarding Notice To Receive (camt.057), Debit Credit Notification (camt.054), and Statement (camt.053) |

[](#)[Business Application Header](#)

The Business Application Header (BAH) is a mandatory element in the CBPR+ ISO20022 format message. The system provides a configurable option to generate the business application header for SWIFT CBPR+ messages. The configurations to generate business application header are maintained in Delivery module.

The system supports the following elements of BAH:

| Field | Description |
| --- | --- |
| *From* | Specifies the party or agent who has created the message. The system supports population of BIC tag under From / Financial Institution Identification. Other fields are not populated. |
| *To* | Specifies the receiving agent who processes the business document. The system supports population of BIC tag under To / Financial Institution Identification. Other fields are not populated. |
| *Business Message Identifier* | Specifies an identification for the message. This is useful to match with outgoing payment when acknowledgements are received. For CBPR+ payments, this field is populated with the same value as document or group header or messages identification. |
| *Message Definition Identifier* | The system provides a configurable option to populate the full ISO message name (such as pacs.009.001.08 for Bank Transfer) ` |
| *Business Service* | Identifies the service on SWIFT network for processing the message. The system provides a configurable option to populate the business service for supported CBPR+ messages. The business service and message definition identifier for each CBPR+ message is given below. |
| *Creation Date* | The system populates the date and time at which the message is generated. |
| *Possible Duplicate* | The system populates this field only in the event of resubmission of an outgoing message (for scenarios where technical acknowledgement is not received). For any other scenario, this field is not populated. |
| *Priority* | The system populates this field for customer and bank transfer with the same value as in the instruction priority in the underlying document. |

The following table shows the business service and message definition identifier for the supported CBPR+ messages:

| Message | Message Definition Identifier | Business Service |
| --- | --- | --- |
| Customer Transfer | pacs.008.001.08 | swift.cbprplus.03 |
| Customer Transfer STP | pacs.008.001.08 | swift.cbprplus.stp.03 |
| Bank Transfer (core) | pacs.009.001.08 | swift.cbprplus.03 |
| Bank Transfer (cover) | pacs.009.001.08 | swift.cbprplus.cov.03 |
| Bank Transfer (pre-advice) | pacs.009.001.08 | swift.cbprplus.adv.03 |
| Payment Status Report | pacs.002.001.10 | swift.cbprplus.03 |
| Return Payment | pacs.004.001.09 | swift.cbprplus.03 |
| Notice To Receive | camt.057.001.06 | swift.cbprplus.03 |
| Debit Credit Notification | camt.054.001.08 | swift.cbprplus.03 |
| Account Statement | camt.053.001.08 | swift.cbprplus.03 |
| Customer Credit Transfer Initiation | Pain.001.001.09 | swift.cbprplus.03 |
| Customer Status Report | pain.002.001.10 | swift.cbprplus.03 |
| Payment Cancellation Request | camt.056.001.08 | swift.cbprplus.03 |
| Resolution of Investigation | camt.029.001.09 | swift.cbprplus.03 |
| Customer Payment Cancellation Request | Camt.055.001.08 | swift.cbprplus.02 |

The following BAH tags are not supported:

- Character Set
- Market Practice
- Copy Duplicate
- Related

The following table shows the business service and message definition identifier for the supported CBPR+ messages.

| Message | Message Definition Identifier | Business Service |
| --- | --- | --- |
| Customer Transfer | pacs.008.001.08 | swift.cbprplus.03 |
| Customer Transfer STP | pacs.008.001.08 | swift.cbprplus.stp.03 |
| Bank Transfer (core) | pacs.009.001.08 | swift.cbprplus.03 |
| Bank Transfer (cover) | pacs.009.001.08 | swift.cbprplus.cov.03 |
| Bank Transfer (pre-advice) | pacs.009.001.08 | swift.cbprplus.adv.03 |
| Payment Status Report | pacs.002.001.10 | swift.cbprplus.03 |
| Return Payment | pacs.004.001.09 | swift.cbprplus.03 |
| Notice To Receive | camt.057.001.06 | swift.cbprplus.03 |
| Debit Credit Notification | camt.054.001.08 | swift.cbprplus.03 |
| Account Statement | camt.053.001.08 | swift.cbprplus.03 |
| Customer Credit Transfer Initiation | Pain.001.001.09 | swift.cbprplus.03 |
| Customer Status Report | pain.002.001.10 | swift.cbprplus.03 |
| Payment Cancellation Request | camt.056.001.08 | swift.cbprplus.03 |
| Resolution of Investigation | camt.029.001.09 | swift.cbprplus.03 |
| Customer Payment Cancellation Request | Camt.055.001.08 | swift.cbprplus.02 |

[](#)[Technical Header](#)

A technical header is required to transport the underlying request payload consisting of business application header and document.  The Swift Alliance Access provides a proprietary format, XMLv2 (also called DataPDU), which is used to exchange MX messages over Interact services. This format envelopes the request payload, adding a technical header and a technical trailer.

To increase the security of the communication between SWIFT interface and the business application, banks can use a local authentication method. Currently, Temenos Transact supports HMAC LAU for the exchange of the FIN messages with SWIFT Alliance Access and is extended for MX messages.

The system provides a configurable option to generate the technical header for sending messages through SWIFT. The configurations to generate technical header is maintained in Delivery module.

Read the Support for SWIFTNet Interact MX services user guide for more details on features and configurations related to BAH and Technical header, MX message routing.

## Message Elements Supported in SWIFT CBPR+ Payments

The following sections explains about the various elements in the ISO20022 format SWIFT CBPR+ payment messages (Customer Transfer - pacs.008, Bank Transfer - pacs.009) which can be captured and processed in Temenos Payments Hub.

[Party and Agent Roles](#)

ISO20022 format CBPR+ payment messages uses several roles to indicate the various parties and agents involved in the payment chain.

Some of these roles are static in nature and therefore transmitted through the payment chain. Some agents are not static, they are changed/swapped as and when payment is processed and redirected through agents.

The system supports the following party and agent roles for ISO20022 format payments.

[Debtor](#)

This element identifies the party which owes an amount of money to the (ultimate) creditor. This is a static role and remains unchanged in the entire payment chain. The debtor could be a customer account for customer transfer or financial institution account for bank transfer.

While capturing an outgoing payment using `OE` screen or `PO` screen, the system provides an option to enter the following details for the debtor:

| Details | Description |
| --- | --- |
| Name | Indicates the name of the debtor |
| Structured Address | Consists of the following elements:   - Department - Sub Department - Street Name - Building Number - Building Name - Floor - Post Box - Room - Post Code - Town Name - Town Location Name - District Name - Country Sub Division - Country   For an outgoing payment, the debtor name and address is fetched from the customer record (based on the debit account number) and populated in the outgoing message.  However, if the user uses the impose option for the debtor, then the manually entered name and address is populated in outgoing message (instead of the customer record details). |
| Organisation / Financial Institution Identification | For customer transfer, the Organisation Identification details are applicable. For bank transfer, Financial Institution Identification details are applicable.   - BIC – To capture the debtor BIC - LEI – Legal Entity Identifier of the debtor - Other Identification – Applicable for customer transfer only   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| Private Identification | Applicable for customer transfer only   - Date and Place of Birth   - Birth Date   - Province Of Birth   - City Of Birth   - Country Of Birth - Other Identification   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| Country of Residence | Indicates the debtor’s country of residence |

Based on the entered debit account, the debtor account tag is mapped in the outgoing message. If the user enters IBAN, then the system maps it under IBAN tag. If the user does not provide the IBAN, the system does not map it under Other Identification tag. For outgoing payments, the system maps only the account number, other optional fields are not mapped.

When the system receives an incoming CBPR+ payment, the debtor and debtor account details are stored in the system. If the payment is redirected, the received debtor and debtor account details are mapped in the redirected message. The ORDPTY role is used to store and map debtor details.

When the user opens a CBPR+ payment for repair, the system displays the debtor details in the read-only mode. The fields which are displayed for debtor in view and repair screens are same as in the capture screen mentioned above. Additionally, the system displays the address fields in view/repair screens as they are present in incoming payments. The system does not allow to modify the debtor details in repair mode.

- Debtor role is similar to ordering customer (tag 50) in MT103 message. The information that can be captured in a MT message is limited (with A/F/K options). ISO20022 format allows a large number of information to be captured for the party roles in structured format.
- Because of co-existence of MT and MX format, the system also supports address elements in CBPR+ format (for scenarios when the payment is initiated in SWIFT FIN and redirected as MX message).
- SWIFT recommends to use structured information when payments are initiated in MX.

The Transact Customer application captures structured address details as required in ISO20022 format. The banks should ensure that proper structured address details are maintained in the customer records, so that it is populated for debtor role in outgoing CBPR+ payments.

If the outgoing and redirected payments (for example, pacs.008) contain the debtor BIC, then the system does not populate the name and address (structured or unstructured) tags in the generated payment message even if the data is available.

Rules for capturing the debtor details are as follows:

- If the user provides the debtor BIC, then all other fields are optional.
- If the user provides the debtor LEI, then it must adhere to the LEI format.
- If the user provides structured address, then the *Town Name* and *Country Code* fields are mandatory.
- If the user provides address, then name of the debtor must be provided.
- The user must provide value in either Organization Identification or Private Identification fields. Do not provide both values. When a value is provided in the Other Identification field (within Organization or Private Identification), this tag can be populated in the message for a maximum of two occurrences.
- Only structured and hybrid address types are supported.

[Ultimate Debtor](#)

This element identifies the ultimate party, which owes an amount of money to the (ultimate) creditor. This is a static role and remains unchanged in the entire payment chain. Ultimate debtor is applicable only for customer transfer.

While capturing an outgoing payment using the `OE` screen or `PO` screen, the system provides an option to enter the following details for ultimate debtor:

| Details | Description |
| --- | --- |
| Name | Indicates the name of the ultimate debtor. |
| Structured address | Structured address consists of the following elements   - Department - Sub Department - Street Name - Building Number - Building Name - Floor - Post Box - Room - Post Code - Town Name - Town Location Name - District Name - Country Sub Division - Country |
| Organisation Identification | - BIC – to capture the ultimate debtor BIC - LEI – legal entity identifier of ultimate debtor - Other Identification   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| Private Identification | - Date and Place of Birth   - Birth Date   - Province Of Birth   - City Of Birth   - Country Of Birth - Other Identification   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| Country of Residence | Indicates the Ultimate Debtor’s country of residence |

When the user receives an incoming CBPR+ payment, the ultimate debtor details are stored in the system. If the payment is redirected, the received ultimate debtor details are mapped in the redirected message. The ULTDBT role is used to store and map ultimate debtor details.

When the user opens a CBPR+ payment for repair, the ultimate debtor details are displayed in the read-only mode. The fields which are displayed for ultimate debtor in view and repair screens are same as in the capture screen. The system does not allow to modify the ultimate debtor details.

There is no tag in SWIFT MT message for ultimate debtor information. In CBPR+ pain.001 message, UltimateDebtor can be present in the <PmtInf> or in the <CdtTrfTxInf> level.

Rules for capturing the ultimate creditor details are as follows:

- If the user provides the ultimate debtor BIC value, then all other fields are optional.
- If the user provides the ultimate debtor LEI value, then it must adhere to the LEI format.
- If the user provides the structured address, then the *Town Name* and *Country Code* fields are mandatory.
- If the user provides the address, then name of the ultimate debtor must be provided.
- The user must provide either the Organization Identification or Private Identification details. Do not provide both the values. When the user provide values for the Other Identification details (within Organization or Private identification), the system allows a maximum of two occurrences.
- Only structured and hybrid address are supported. Unstructured address is not supported.

[Creditor](#)

This element identifies the party to which an amount of money is due. This element is also referred as beneficiary. This is a static role and remains unchanged in the entire payment chain. The creditor could be a customer account for customer transfer or financial institution account for bank transfer.

While capturing an outgoing payment using the `OE` screen or `PO` application, the system provides an option to enter the following details for creditor:

| Field | Description |
| --- | --- |
| Name | Indicates the name of the creditor (beneficiary). |
| Structured address | The structured address consists of the following elements:   - Department - Sub Department - Street Name - Building Number - Building Name - Floor - Post Box - Room - Post Code - Town Name - Town Location Name - District Name - Country Sub Division - Country |
| Unstructured address lines | Unstructured address lines (maximum two lines) |
| Organisation / Financial Institution Identification | For customer transfer, Organisation Identification details are applicable. For bank transfer, Financial Institution Identification details are applicable.   - BIC – To capture the creditor BIC - LEI – Legal Entity Identifier of creditor - Other Identification – Applicable for customer transfer only   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| Private Identification | Applicable for customer transfer only   - Date and Place of Birth   - Birth Date   - Province Of Birth   - City Of Birth   - Country Of Birth - Other Identification   - Identification   - Scheme Name (Code or Proprietary)   - Issuer |
| Country of Residence | Indicates the Creditor’s country of residence |

The system provides an option to maintain creditor or beneficiary details using the `BENEFICIARY` application. While capturing outgoing CBPR+ payment using the `PO` application or OE screen, the user can select a valid beneficiary record id and click on Validate. The system fetches beneficiary details and populates the details on the screen.

Based on the entered credit account, the creditor account tag is mapped in the outgoing message. If IBAN is entered, then it is mapped under IBAN tag, else mapped under Other Identification tag. For outgoing payments, the system maps only the account number, other optional fields are not mapped.

When an incoming CBPR+ payment is received, the creditor and creditor account details are stored in the system. If the payment is redirected, the received creditor and creditor account details are mapped in the redirected message. The BENFCY (for customer transfer) or BENINS (for bank transfer) role is used to store and map creditor details.

When an incoming CBPR+ payment is received and the system is unable to credit the beneficiary account, the payment is moved to repair. Possible scenarios where the system is unable to credit the beneficiary account are:

- creditor account is not existing
- creditor account is closed
- posting restrictions on creditor account
- creditor account is not provided

When the user opens a CBPR+ payment for repair, the creditor details are displayed in the read-only mode, except the *Creditor Account* field. The fields which are displayed for creditor in view and repair screen are same as in the capture screen. The user can modify the creditor account details and submit the payment for processing.

- Creditor role is similar to beneficiary customer (tag 59) in MT103 message and beneficiary institution (tag 58) in MT202 message.
- SWIFT recommends using structured information when payments are initiated in MX format.

If the outgoing and redirected payments (for example pacs.008) contain the creditor BIC, then the system does not populate the name and address (structured or unstructured) tags in the generated payment message even if the data is available.

Rules for capturing the creditor details are as follows:

- If the Creditor BIC value is provided, then all other fields are optional.
- If the Creditor LEI value is provided, then it must adhere to the LEI format.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- If address is provided, then the name of creditor must be provided.
- Either Organization Identification or Private Identification details should be provided. Do not provide both. When Other Identification details are provided (within Organization or Private identification), maximum two occurrences are allowed.
- Only structured and hybrid address types are supported.

[Ultimate Creditor](#)

This element identifies the ultimate party to which an amount of money is due. This is a static role and remains unchanged in the entire payment chain. Ultimate creditor is applicable only for customer transfer.

While capturing an outgoing payment using the OE screen or `PO` application, the system provides an option to enter the following details for ultimate creditor:

| Field | Description |
| --- | --- |
| *Name* | Indicates the name of the ultimate creditor. |
| *Structured address* | Structured address consists of the following elements   - Department - Sub Department - Street Name - Building Number - Building Name - Floor - Post Box - Room - Post Code - Town Name - Town Location Name - District Name - Country Sub Division - Country |
| *Organisation Identification* | - BIC – to capture the creditor BIC - LEI – legal entity identifier of creditor - Other Identification   - Identification   - Scheme Name (Code or Proprietary)  - Issuer |
| *Private Identification* | - Date and Place of Birth   - Birth Date   - Province Of Birth   - City Of Birth   - Country Of Birth - Other Identification   - Identification   - Scheme Name (Code or Proprietary) - Issuer |
| *Country of Residence* | Indicates the Ultimate Creditor’s country of residence |

The system provides an option to maintain ultimate creditor details against a creditor or beneficiary using the `BENEFICIARY` application. While capturing outgoing CBPR+ payment using `PO` or OE screen, the user can select a valid beneficiary record id and click Validate. The system fetches the beneficiary details and populates on the screen. If the user maintains the ultimate creditor details, then those details are also defaulted based on the beneficiary record.

When an incoming CBPR+ payment is received, the ultimate creditor details are stored in system. If the payment is redirected, the received ultimate creditor details are mapped in the redirected message. The ULTCDT role is used to store and map ultimate creditor details.

When the user opens a CBPR+ payment for repair, the ultimate creditor details are displayed in the read-only mode. The fields which are displayed for ultimate creditor in view and repair screen are same as in the capture screen. Modification of ultimate creditor details is not allowed.

There is no tag is SWIFT MT message for ultimate creditor information.

Rules for capturing the ultimate creditor details are as follows:

- If the Ultimate Creditor BIC value is provided, then all other fields are optional.
- If the Ultimate Creditor LEI value is provided, then it must adhere to the LEI format.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- If address is provided, then name must be provided.
- Either Organization Identification or Private Identification details should be provided. Do not provide both. When Other Identification is provided (within Organization or Private identification), maximum two occurrences are allowed.
- Only structured and hybrid address are supported. Unstructured address is not supported.

[Initiating Party](#)

This element identifies the party which initiates the credit transfer on behalf of the debtor. This is a static role and remains unchanged in the entire payment chain. This role is applicable for customer transfer when initiated using pain.001 message containing Initiating Party details and also for customer credit transfer initiation message (pain.001). If the payment is initiated using the OE screen or `PO` application, this role is not captured on screen.

When the user receives an incoming CBPR+ payment, the initiating party details are stored in the system. If the payment is redirected, the received initiating party details are mapped in the redirected message. The INIPTY party role is used to store and map the initiating party details.

The initiating party details are not displayed in the ISO view or repair screens as individual fields but the user can view this information as part of the received message (as XML). Refer to the [Viewing SWIFT CBPR+ pain.001](Workingwith.htm#Viewing) section for more information.

Rules for capturing the initiating party details are as follows:

- If initiating party BIC is provided, then all other fields are optional.
- If initiating party LEI is provided, then it must adhere to the LEI format.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- If address is provided, then name must be provided.
- Either Organization Identification or Private Identification details should be provided. Do not provide both. When Other Identification details are provided (within Organization or Private identification), maximum two occurrences are allowed.
- Only structured and hybrid address are supported. Unstructured address is not supported.

[Instructing Agent](#)

This role identifies the agent that instructs the next agent in the payment chain to process the payment. It can be considered as the sender of the payment message. This is not a static role, it keeps on changing as and when the payment is redirected.

For outgoing and redirected payments, the system populates own company BIC (configured in company properties) as the instructing agent. No other fields are populated for this role in the generated message.

When the user opens a CBPR+ payment for repair, the following instructing agent related fields are displayed in the read-only mode and not allowed to be modified.

| Field | Description |
| --- | --- |
| *BIC* | Indicates the Sender/Instructing agent BIC. |
| *Clearing System ID* | Indicates the ISO clearing system identification. |
| *Clearing Member ID* | Indicates the national clearing code or member identification. |

Rules for capturing the instructing agent details are as follows:

- When the transaction is exchanged on the SWIFT network (that is, if the instructing agent or sender and instructed agent or receiver of the message are on SWIFT), then BIC is mandatory and other elements are optional.
- If instructed agent BIC is provided, then all other fields are optional.

[Instructed Agent](#)

This role identifies the agent that has been instructed in the payment chain to process the payment. The agent can be considered as the receiver of the payment message. This is not a static role, it changes as and when the payment is redirected.

While capturing an outgoing payment, the system provides option to enter the following details for the instructed agent:

| Details | Description |
| --- | --- |
| BIC | Indicates the Receiver/Instructed agent BIC. |
| Clearing System ID | Indicates the ISO clearing system identification. |
| Clearing Member ID | Indicates the National clearing code/member identification. |

For international payments, only BIC is sufficient to route the payment. In CBPR+ messages, it is mandatory to provide the instructed agent BIC. The system does not populate other fields for this role in the generated message.

When BIC is not provided, then both the *Clearing System ID* and *Clearing Member ID* fields must be provided together so that the system can fetch and populate the corresponding BIC.

The system populates the determined receiver BIC in the generated message as instructed agent (from RECVER role). Other optional fields are not mapped.

When the user opens CBPR+ payments for repair, the instructed agent details are displayed. The fields which are displayed for instructed agent in view and repair screen are same as in the capture screen mentioned above. Modification of instructed agent is allowed.

Rules for capturing the instructed agent details are as follows:

- When the transaction is exchanged on the SWIFT network (that is, if the instructing agent/sender and instructed agent/receiver of the message are on SWIFT), then BIC is mandatory and other elements are optional.
- If instructed agent BIC is provided, then all other fields are optional.

[Debtor Agent](#)

This role indicates the agent that service the account of the debtor. This is a static role and remains unchanged in the entire payment chain.

For outgoing payment, the processing company is considered as the debtor agent. However, there is an option to manually enter the debtor agent when it is different from own company.

While capturing an outgoing payment using the OE screen, the system provides option to enter the following details for debtor agent (to be used when debtor agent is different from own company):

| Field | Description |
| --- | --- |
| BIC | Indicates the debtor agent BIC. |
| Clearing System ID | Indicates the five character ISO clearing system identification. |
| Clearing Member ID | Indicates the national clearing code/member identification. |
| LEI | Indicates the Legal Entity Identifier (LEI) of the debtor agent. |
| Structured Address | The following three fields of structured address of the debtor agent can be captured:   - *Town Name* - *Country Code* - *Post Code* |
| Unstructured address line | The user can enter a maximum of two lines of unstructured address, each line can hold a maximum of 70 characters. |
| Account | Indicates the debtor agent account. |

For international payments, only BIC is sufficient. Hence, if BIC is provided, then other fields are not required. If the outgoing and redirected payments contain BIC, then the system does not populate the name and address (structured or unstructured) tags in the generated message.

When BIC is not provided and clearing system details are provided, then both the *Clearing System ID* and *Clearing Member ID* field must be provided together (along with other necessary information based on the rules).

For an outgoing payment, debtor agent is mapped with the own company BIC. However, if the user has entered debtor agent details while capturing payment, then those are mapped.

When an incoming CBPR+ payment is received, the debtor agent details are stored in the system. If the payment is redirected, the received debtor agent details are mapped in the redirected message. The ORDINS role is used to store and map debtor agent details.

When the user opens a CBPR+ payment for repair, the debtor agent details are displayed if received. The fields which are displayed for debtor agent in view and repair screen are same as in the capture screen. Modification of debtor agent is not allowed.

- SWIFT recommends using structured information when payments are initiated in MX format.

Rules for capturing the debtor agent details are as follows:

- If debtor agent BIC is provided, then all other fields are optional.
- If debtor agent LEI is provided, then it must adhere to the LEI format.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- Name and address must be provided together.
- Structured or hybrid address are supported.

[Creditor Agent](#)

This role indicates the agent that services the account of the creditor (beneficiary). The creditor could be a customer account for customer transfer or financial instruction account for bank transfer. This is a static role and remains unchanged in the entire payment chain.

While capturing an outgoing payment using the OE screen or `PO` application, the system provides option to enter the following details for creditor agent:

| Field | Description |
| --- | --- |
| BIC | Indicates the creditor agent BIC. |
| Clearing System ID | Indicates the ISO clearing system identification. |
| Clearing Member ID | Indicates the national clearing code/member identification. |
| LEI | Indicates the Legal Entity Identifier of the creditor agent. |
| Name | Indicates the name of the creditor agent. |
| Structured Address | The following three fields of the structured address of the creditor agent can be captured:   - *Town Name* - *Country Code* - *Post Code* |
| Unstructured address line | The user can enter a maximum of three lines of unstructured address, and each line can hold a maximum of 70 characters. |
| Account | Indicates the creditor agent account. |

For international payments, only BIC is sufficient. Hence, if BIC is provided, then other fields are not required. If the outgoing and redirected payments contains BIC, then the system does not populate the name and address (structured or unstructured) tags in the generated message.

If clearing system details are provided, then both the *Clearing System ID* and *Clearing Member ID* fields must be provided together (along with other necessary information based on the rules).

For outgoing and redirected payments, the system populates creditor agent BIC determined by Routing & Settlement (from ACWINS role). R&S does not support payment routing based on LEI.

When an incoming CBPR+ payment is received, the creditor agent details are stored in system. If the payment is redirected, the received creditor agent details are mapped in the redirected message. Role ACWINS is used to store and map debtor agent details.

When a bank transfer or return is received with a creditor agent (ACWINS) containing only the name and address and without a BIC or NCC, then the creditor agent details are ignored, and the direction is determined based on the Creditor details (BENINS).

When the user opens a CBPR+ payment for repair, the creditor agent details are displayed. The fields which are displayed for creditor agent in view and repair screen are same as in the capture screen mentioned above. Modification of creditor agent is allowed.

- This is similar to the account with institution (tag 57) in SWIFT MT message.
- Because of co-existence of MT and MX format, unstructured address elements are also supported in CBPR+ format (for scenarios when the payment is initiated in SWIFT FIN and redirected as MX message).
- SWIFT recommends to use structured information when payments are initiated in MX.

Rules for capturing the creditor agent details are as follows:

- If creditor agent BIC is provided, then all other fields are optional.
- If creditor agent LEI is provided, then it must adhere to the LEI format.
- If structured address is provided, then the *Town Name* and *Country Code* fields are mandatory.
- Name and address must be provided together.
- Structured or Hybrid address are supported.

[Reimbursement Agent](#)

The system supports three reimbursement agent roles. These roles are applicable only for customer or bank transfer settled using the cover method. These are not applicable for return payment.

When a cross border customer transfer is initiated and settled using cover method, the debtor agent sends the announcement message directly to the creditor agent informing details of the reimbursement agents through which the funds are made available. The actual fund moves through a separate cover payment (pacs.009 COV) through these reimbursement agents.

When a customer transfer is settled using cover method

- The Debtor Agent sends a pacs.009 pre-advice announcement message directly to creditor agent, informing details of the reimbursement agents through which the funds are made available to the creditor agent.
- A pacs.009 cover (pacs.009 COV) message is generated separately, to move the funds through these reimbursement agents to credit the creditor agent’s account

When a bank transfer is settled using pre-advice (cover) method

- The debtor agent sends a pacs.009 pre-advice announcement message directly to creditor agent, informing details of the reimbursement agents through which the funds are made available to the creditor agent
- A pacs.009 message is generated separately, to move the funds through these reimbursement agents to credit the creditor agent’s account

[Instructing Reimbursement Agent](#)

This role indicates the agent through which the instructing agent reimburses the instructed agent. This specifies the account or branch of the Sender or another financial institution through which the Sender reimburse the Receiver.

For an outgoing customer transfer settled using cover, the system populates instructing reimbursement agent BIC, if determined by Routing & Settlement or imposed (from SNDCBK role) in the direct or announcement message (pacs.008). In the corresponding cover message (pacs.009 COV), the instructing reimbursement agent is mapped as the receiver.

For an outgoing bank transfer settled using pre-advice (cover), the system populates instructing reimbursement agent BIC, if determined by Routing and Settlement or imposed (from SNDCBK role) in the direct or announcement message (pacs.009 ADV). In the corresponding cover message (pacs.009), the instructing reimbursement agent is mapped as the receiver.

In the corresponding pacs.009 cover message, the instructing reimbursement agent is mapped as the receiver.

[Instructed Reimbursement Agent](#)

This role indicates the agent at which the instructed agent is reimbursed. This field specifies the branch of the Receiver or another financial institution at which the funds will be made available to the Receiver.

For an outgoing customer transfer settled using cover, the system populates instructed reimbursement agent BIC if determined by R&S or imposed (from RCVCBK role). In the corresponding cover message (pacs.009 COV), the instructed reimbursement agent is mapped as intermediary agent 1.

For an outgoing bank transfer settled using pre-advice (cover), the system populates instructed reimbursement agent BIC, if determined by Routing and Settlement or imposed (from RCVCBK role) in the direct or announcement message (pacs.009 ADV).In the corresponding cover message (pacs.009), the instructed reimbursement agent is mapped as the creditor agent.

In the corresponding pacs.009 cover message, the instructed reimbursement agent is mapped as intermediary agent 1.

[Third Reimbursement Agent](#)

This role indicates the agent at which the instructed agent is reimbursed. This field specifies the Receiver's branch, when the funds are made available to this branch through a financial institution other than that indicated in Instructed Reimbursement Agent.

For outgoing customer payment settled through cover, system populates instructed reimbursement agent BIC if determined by R&S or imposed (from TRMINS role).

For bank transfer settled with pre-advice (cover), Third Reimbursement Agent is not allowed.

In the corresponding pacs.009 cover message, the creditor agent is mapped with either third reimbursement agent or instructed reimbursement agent based on availability.

While capturing an outgoing payment using Order Entry or Payment Order, system provides option to enter the following details for instructing, instructed and third reimbursement agents:

| Field | Description |
| --- | --- |
| BIC | Reimbursement agent BIC. |
| Clearing System ID | ISO clearing system identification. |
| Clearing Member ID | National clearing code/member identification. |
| LEI | Legal Entity Identifier of the creditor agent. |
| Name | Indicates the name of the reimbursement agent. |
| Structured Address | The following three fields of the structured address of the reimbursement agent can be captured:   - *Town Name* - *Country Code* - *Post Code* |
| Unstructured address line | The user can enter a maximum of two lines of unstructured address, each line can hold a maximum of 70 characters. |
| Account | Indicates the reimbursement agent account. |

For international payments, only BIC is sufficient. Hence if BIC is provided, then other fields are not required.

If the outgoing and redirected payments contain BIC, then the system does not populate the name and address (structured or unstructured) tags in the generated message.

If clearing system details are provided, then both the *Clearing System ID* and *Clearing Member ID* must be provided together (along with other necessary information based on the rules).

R&S does not support payment routing based on LEI.

When a CBPR+ payment is opened for repair, the reimbursement agent details are displayed. The fields which are displayed for each reimbursement agent in view and repair screen are same as in the capture screen mentioned above. Modification of reimbursement agent is allowed.

- Instructing Reimbursement Agent is similar to the sender’s correspondent (tag 53) in SWIFT MT message
- Instructed Reimbursement Agent is similar to the receiver’s correspondent (tag 54) in SWIFT MT message.
- Third Reimbursement Agent is similar to the third reimbursement agent (tag 55) in SWIFT MT message
- SWIFT recommends using structured information when payments are initiated in MX format.

Rules for capturing the reimbursement agent details are as follows:

- If BIC is provided, then all other fields are optional.
- If LEI is provided, then it must adhere to the LEI format.
- If structured address is provided, then Town Name and Country Code are mandatory.
- Name and address must be provided together.
- Structured or hybrid address are supported.

[Previous Instructing Agent 1, 2 and 3](#)

This role identifies the previous agents, which have processed the payment, prior to the current agent. This role ensures when a payment is processed serially through multiple intermediary agents, all the previous agents are retained in the payment chain. This is useful when payment is returned (using pacs.004).

When a redirected payment is processed, R&S component determines and populates the previous instructing agent roles. CBPR+ allows maximum three previous instructing agent roles in the payment chain. For a redirected payment, the system supports population of up to three previous instructing agents (PRVINS, PRVIN2 and PRVIN3 roles).

For an outgoing payment, previous instructing agent is not populated in the generated message.

When an incoming CBPR+ payment is received, the previous instructing agent details are stored in system. If the payment is redirected, Routing & Settlement determines the swapped roles and generates previous instructing agent roles which are mapped in the redirected message.

When the user opens a CBPR+ payment for repair, the previous instructing agent 1, 2 and 3 details are displayed in the read-only mode. Modification of previous instructing agent details is not allowed. The system displays the following details for each previous instructing agent:

| Field | Description |
| --- | --- |
| BIC | Indicates the previous instructing agent BIC |
| Clearing System ID | Indicates the ISO clearing system identification |
| Clearing Member ID | Indicates the national clearing code/member identification |
| LEI | Indicates the Legal Entity Identifier (LEI) of the previous instructing agent |
| Name | Indicates the name of the previous instructing agent |
| Structured Address | The following three fields of structured address of the previous instructing agent are displayed   - *Town Name* - *Country Code* - *Post Code* |
| Unstructured address line | The user can enter a maximum of two lines of unstructured address, each line can hold a maximum of 70 characters. |
| Account | Indicates the previous instructing agent account |

SWIFT MT format does not have any explicit tag to hold this information. However, optional provision is there in MT message to pass this information as part of tag 72 (Sender to Receiver Information) with code word ‘INS’ followed by the previous instructing agent BIC.

If incoming MT message is received with code word ’INS’ and BIC in Tag 72, and the payment is to be redirected in MX format, then the system performs an enrichment to populate the Previous Instructing Agent role.

If the redirected payments contain BIC, then the system does not populate the name and address (structured or unstructured) tags in the generated message.

Rules for capturing the previous instructing agent details are as follows:

- If BIC is provided, then all other fields are optional.
- If LEI is provided, then it must adhere to the LEI format.
- If structured address is provided, then *Town Name* and *Country Code* fields are mandatory.
- Name and address must be provided together.
- If previous instructing agent 2 details are provided, then previous instructing agent 1 must be provided.
- If previous instructing agent 3 details are provided, then previous instructing agent 2 must be provided.
- Structured or Hybrid address are supported.

[Populating Previous Instructing Agent](#)

The following diagram illustrates the change of agent roles at different stages when the payment is processed by different agents.

/Introduction_2.png)

When acting as a redirecting agent, the system generates the previous instructing agent roles. The system ensures that maximum three previous instructing agents are populated while redirecting payments when the payment is sent through a MX based channel.

For a redirected MX payment, the system generates the previous instructing agents based on the following conditions:

- If previous instructing agent 1 is present, it remains as previous instructing agent 1.
- If previous instructing agent 2 is present, it remains as generated previous instructing agent 2.
- If previous instructing agent 1 is present, then the current instructing agent (sender of the payment instruction) becomes previous instructing agent 2. Previous instructing agent 1 remains unchanged.
- If previous instructing agent 1 and 2 are present, then the current instructing agent (sender of the payment instruction) becomes previous instructing agent 3. Previous instructing agent 1 and 2 remains unchanged.
- If previous instructing agent 1 is not present and the debtor agent is different from the instructing agent, then the instructing agent becomes previous instructing agent 1.

| Incoming Message | | | Redirected Message |
| --- | --- | --- | --- |
| Sender | Is Previous Instructing Agent Present | Is Debtor Agent present | NA |
| Bank A | No | No | Sender Bank A becomes debtor agent in redirected message |
| Bank A | No | Yes | Sender Bank A becomes Previous Instructing Agent 1 in redirected message |
| Bank A | Previous Instructing Agent 1 Present | NA | Previous Instructing Agent 1 remains as it is Sender becomes Previous Instructing Agent 2 |
| Bank A | Previous Instructing Agent 1 and Previous Instructing Agent 2 Present | NA | Previous Instructing Agent 1 and 2 remains as it is Sender becomes Previous Instructing Agent 3 |
| Bank A | Previous Instructing Agent 1  and  Previous Instructing Agent 2  and  Previous Instructing Agent 3  Present | NA | Not Possible as maximum three previous instructing agents are allowed |

[Intermediary Agent 1, 2 and 3](#)

An intermediary is an agent which is between the debtor’s agent and creditor’s agent. When debtor agent and creditor agent does not have direct relationship, the payment may be sent serially through one or more intermediary agents to reach the creditor agent. The intermediary agents in the payment chain acts as redirecting agents. These are not static roles, they change as and when a payment is redirected.

When payment is processed, R&S component determines the intermediary agents required to send the payment. CBPR+ allows maximum three intermediary agent roles in the payment chain. For outgoing and redirected payments, the system supports population of up to three intermediary agents (role INTINS, INTIN2 and INTIN3).

While capturing an outgoing payment using the OE screen or `PO` application, the system provides an option to enter the following details for intermediary agent 1, 2, and 3:

| Details | Description |
| --- | --- |
| BIC | Indicates the intermediary agent BIC |
| Clearing System ID | Indicates the ISO clearing system identification |
| Clearing Member ID | Indicates the national clearing code/member identification |
| LEI | Indicates the Legal Entity Identifier of the intermediary agent |
| Structured Address | The following three fields of structured address of the intermediary agent can be captured   - *Town Name* - *Country Code* - *Post Code* |
| Unstructured address line | The user can enter a maximum of two lines of unstructured address, each line can hold a maximum of 70 characters. |
| Account | Indicates the intermediary agent account |

For international payments, BIC is sufficient to route the payment. Hence, if BIC is provided, then other fields are not required. If the outgoing and redirected payments contain BIC, then the system does not populate the name and address (structured or unstructured) tags in the generated message.

If clearing system details are provided, then both the *Clearing System ID* and *Clearing Member ID* fields must be provided together (along with other necessary information based on the rules).

For an outgoing and redirected payment, Routing & Settlement determines the intermediary agents and then mapped in the generated message. R&S does not support payment routing based on LEI.

When an incoming CBPR+ payment is received, the intermediary agent details are stored in system. If the payment is redirected, R&S components determines the swapped roles and the regenerated intermediary details are mapped in the redirected message.

When the user opens a CBPR+ payment for repair, the intermediary agent 1, 2 and 3 details are displayed. The fields which are displayed for each intermediary agent in view and repair are same as in the capture screen. The system allows the user to modify the intermediary agent details.

- SWIFT MT format supports only one intermediary role using Tag 56. However optional provision is there in MT message to pass additional intermediary agent details as part of Tag 72 (Sender to Receiver Information) with code word ’INT’ followed by the previous instructing agent BIC.
- If incoming MT message is received with code word ’INT’ and BIC in Tag 72, it is not treated as an intermediary agent in system. It is saved like a code word like any other details of Tag 72.
- When a payment is received in MX format and redirected in MT format, system populates only one intermediary in tag 56 and does not populate any additional intermediary details with ‘INT’ code word in Tag 72.

Rules for capturing the intermediary agent 1, 2 and 3 details are as follows:

- If BIC is provided, then all other fields are optional.
- If LEI is provided, then it must adhere to the LEI format.
- If structured address is provided, then *Town Name* and *Country Code* fields are mandatory.
- Name and address must be provided together.
- If Intermediary agent 1 account is entered, other details (like BIC, clearing identification and so on) should also be provided.
- If Intermediary agent 2 account is entered, other details (like BIC, clearing identification and so on) should also be provided.
- If Intermediary agent 2 details are provided, then Intermediary agent 1 must be provided.
- If Intermediary agent 3 account is entered, other details (like BIC, clearing identification and so on) should also be provided. If Intermediary agent 3 details are provided, then Intermediary agent 2 must be provided.
- Structured or hybrid address are supported.

[Number of Credit Agents in the Payment Chain](#)

The following table displays the maximum number of credit agents that can be present in an outgoing or redirected payment. Routing & Settlement component validates the same while processing the payment and an error is raised in case of breach.

| Scenario | Number of Previous Agents | Direction | Max Credit Agents | Allowed Agent Roles |
| --- | --- | --- | --- | --- |
| Payment is sent through serial method | 0 | Outgoing | 5 | 1. Creditor Agent 2. Intermediary Agent 1 3. Intermediary Agent 2 4. Intermediary agent 3 5. Instructed Agent (Receiver) |
| Payments is sent through cover method | 0 | Outgoing | 8 | 1. Creditor Agent 2. Intermediary Agent 1 3. Intermediary Agent 2 4. Intermediary agent 3 5. Instructed Agent (Receiver) 6. Instructing Reimbursement  Agent 7. Instructed Reimbursement Agent 8. Third Reimbursement Agent |
| Payments is sent through serial method | 0 | Redirected | 4 | 1. Creditor Agent 2. Intermediary Agent 1 3. Intermediary Agent 2 4. Instructed Agent (Receiver) |
| Payments is sent through cover method | 0 | Redirected | 7 | 1. Creditor Agent 2. Intermediary Agent 1 3. Intermediary Agent 2 4. Instructed Agent (Receiver) 5. Sender’s Correspondent  Agent 6. Receiver’s Correspondent Agent 7. Third Reimbursement Agent |
| Payments is sent through serial method | 1 | Redirected | 3 | 1. Creditor Agent 2. Intermediary Agent 1 3. Instructed Agent (Receiver) |
| Payments is sent through cover method | 1 | Redirected | 6 | 1. Creditor Agent 2. Intermediary Agent 1 3. Instructed Agent (Receiver) 4. Instructing Reimbursement  Agent 5. Instructed Reimbursement  Agent 6. Third Reimbursement Agent |
| Payments is sent through serial method | 2 | Redirected | 2 | 1. Creditor Agent 2. Instructed Agent (Receiver) |
| Payments is sent through cover method | 2 | Redirected | 5 | 1. Creditor Agent 2. Instructed Agent (Receiver) 3. Instructing Reimbursement  Agent 4. Instructed Reimbursement  Agent 5. Third Reimbursement Agent |
| Payments is sent through serial method | 3 | Redirected | 1 | 1. Creditor Agent /Instructed Agent   Creditor Agent and Instructed agent are same |
| Payments is sent through cover method | 3 | Redirected | 4 | 1. Creditor Agent /Instructed Agent (Receiver of underlying transaction) 2. Instructing Reimbursement  Agent 3. Instructed Reimbursement  Agent 4. Third Reimbursement Agent   Creditor Agent and Instructed agent are same |

The credit agents are:

- Instructed Agent (RECVER)
- Creditor Agent (ACWINS)
- Intermediary Agent 1 (INTINS)
- Intermediary Agent 2 (INTIN2)
- Intermediary Agent 3 (INTIN3)
- Sender Correspondent (SNDCBK)
- Receiver Correspondent (RCVCBK)
- Third Reimbursement Agent (TRMINS)

All other party or agent roles are considered as debit parties or agents.

[](#)[Hybrid Address Support](#)

As part of SWIFT annual rulebook 2025 changes, SWIFT allows using hybrid address for various parties and agents in the payment chain. Previously, SWIFT supported either structured or unstructured address for parties and agents. SWIFT supports fully structured or hybrid address (combination of structured and unstructured) for parties and agents.

The hybrid address is used to accommodate details that cannot be captured within the structured address format. This is particularly useful for banks or countries that cannot provide complete structured information, especially when their core systems do not comply with structured address requirements.

Hybrid is the combination of structured and unstructured. In hybrid, unstructured address is supported for two lines of 70 characters.

- Fully structured - All the structured details under postal address tag can be populated whereas town name and country are mandatory tags.
- Hybrid - Structured (all other structured tags with a mandatory town name and country) + Unstructured address (two lines of 70 characters).

The rulebook changes for 2025 are added in the module PPSWMX for the DEV release. User has to enable the current release in SWIFT parameter table of CBPRPLUS record as 2025 to enable this rulebook changes. For the backpatch clients, user requires CBPR25 license module to enable these rulebook changes.

[Address Type for Parties and Agents](#)

[Parties and Agents that supports structured or unstructured or Hybrid](#)

- Previous Instructing Agent 1, 2, 3
- Debtor Agent
- Creditor agent
- Debtor
- Creditor
- Intermediary agent 1, 2, 3
- Instructing Reimbursement Agent
- Instructed Reimbursement Agent
- Third Reimbursement Agent

[Parties that support only structured or Hybrid](#)

The following parties in a SWIFT CBPR+ payment continue to support only structured or hybrid address format.

- Ultimate Debtor
- Ultimate Creditor
- Initiating Party
- Structured remittance information tags
  - Invoicer
  - Invoicee
  - Garnishee
  - Garnishment Administrator

[System Impact for Hybrid Address](#)

The clearing parameter indicates that the output channel (clearing or SWIFT) of the transaction supports hybrid address or only structured/unstructured. Based on this configuration, system formats the address types for various parties and agents in the outward message.

| Field | Description |
| --- | --- |
| *Address Type* | This field indicates if the clearing or channel supports the Hybrid address for the outward messages.   - Hybrid, Str, Unstr -   Indicates that the clearing or channel supports Hybrid Address   (Structured and unstructured 2\*70) in the outward message. System tries   to send the Hybrid address and then second preferrence to Structured and   then to Unstructured. - Blank (Default value) -   All the details are emitted out. Both structured and unstructured   details are emitted for mapping the outward message. Based on the   condition in the schema, respective address type are generated. |

[For Outgoing Payments – Order Entry, Payment Order and Pain.001](#)

- For payments initiated through Order Entry (for Debtor), if the user enters the debit account and the debtor information is not imposed, system fetches address details from customer database and populates the same in order entry screen. For creditor, ultimate debtor, and ultimate creditor, the user can enter structured data along with unstructured address lines.
- For agents under Routing Information tab, Creditor agent, Debtor agent, Instructing Reimbursement Agent, Instructed Reimbursement Agent, Third Reimbursement Agent, Intermediary Agent 1, 2, and 3, the user can enter town name, country, and postcode for structured details and address line for unstructured address details.
- User can multi-value and enter any number of lines for address lines for parties and agents. The system does the necessary concatenation and forms the address line as per the hybrid address format and send in the outgoing message if the clearing configuration is set as Hybrid.
- The system concatenates all the address lines without a space and forms two lines of 70 characters each.
- The system throws a warning for hybrid address as 'Name and Structured Postal Address (at least Town Name and Country) and unstructured Address Lines must be present together for sending Hybrid Address' (based on Hybrid address configuration in the clearing parameter) in the below scenarios.
  - When the user enters town name and address line without country.
  - When the user enters country and address line without town name.

This warning is raised for only outgoing payments initiated from Order Entry and from Payment Order (when transparency is enabled as part of payment product) and if the payment is processed from repair queue.

- For the payments initiated through pain.001, the system forwards all the details as received in the pain.001 to pacs.008. The debtor information received in the pain.001 is not forwarded, instead the details are forwarded from the customer database for Debtor tag in the outward message. Based on the details present in the pain.001, the system tries to send Hybrid, Structured, or Unstructured for parties and agents. This is based on the Addresstype configuration in the clearing parameter.
- For the payments initiated through payment order, the user can enter both structured and unstructured address details for parties and agents. If the transparency check is enabled as part of the payment order product, then the warning message for hybrid address is displayed in the payment order screen if either country or town name are missing for any parties and agents. Warning message is raised only for the transaction which output channel supports hybrid.
- The address details entered in the payment order screen for any parties and agents are concatenated as per the hybrid address format in payment system before generating the outward message. So, all the details entered in the payment order is mapped to TPH as it is and formatted only during the message generation.
- Payment initiated from other modules (FX, MM, LD, and so on) which is routed to TPH through payment order supports structured address or hybrid address format.
- For the payment initiated through bulk master, the user can enter structured and unstructured address details through CSV upload or xml upload. Once the message is received and processed in TPH, based on the clearing configuration for address type, the system formats hybrid or structured address for parties and agents.
- When the payment is initiated from order entry or from payment order using *Beneficiary Id*, then all the details stored in BENEFICIARY is fetched and displayed in the POA and OE screens in the respective tabs. Both structured and unstructured address are fetched and displayed on the screen. Once the message is processed, if the messages contains the details for hybrid address, then the same gets populated in the outward messages.

[For Redirected Payments](#)

On receiving payment with hybrid address details, system tries to send same details in the outward message if the clearing or channel supports hybrid based on the configuration in clearing parameter. if the output channel of the transaction doesn’t support hybrid, then system tries to send structured or unstructured.

On receiving the MT message with 50F or 59F option, then the same gets enriched as hybrid address and populated in the outward message.



System’s decision to send address format for outgoing and Redirected Payments is shown below.

| Country | Town Name | Address Lines | Outward Message |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Send Hybrid Address |
| No | Yes | Yes | Raise a warning for OE and PO (if transparency is enabled) |
| Yes | No | Yes | Raise a warning for OE and PO (if transparency is enabled) |
| Yes | Yes | No | Send only structured address |
| No | No | No | Do not send any address details.  Existing behavior. |

The concatenation logic for address format is shown below.

If the number of occurrences of addresslines are 2 and the length is less than or equal to 70 in each occurrence, then do not concatenate, else, concatenate all the lines and store as below.

- Addressline 1 = (1,70)
- Addressline 2 = (71,70) (without space)

[For Incoming Payments](#)

On receiving messages with hybrid address for various parties and agents, the messages get stored in the system and viewable for the user. Both structured and unstructured address details get displayed on the view screen. It is with the assumption that all the incoming messages that comes from clearing or network undergoes the validation and come in the proper format. So, there is no validation or warning message for the incoming messages.

[Message Identification](#)

This is a point-to-point reference, as assigned by the instructing party and sent to the next party in the chain to unambiguously identify the message. When the message is received and redirected, every agent generates a unique new Message Identification. This is a mandatory information.

The system supports population of message id in outgoing and redirected payments. For payments, bulk reference id is assigned as the message identification.

For CBPR+ payments, this message id is also mapped in the business application header.

[Settlement Method](#)

It indicates the method used to settle the payment instruction. This is a mandatory information.

Cross border international payments are settled between correspondent banks using NOSTRO or VOSTRO relationship. The system supports population of following values as settlement method in outgoing and redirected messages.

| Value | Description |
| --- | --- |
| INGA | Indicates that an instructing agent settles the payment.  In this scenario, sending bank holds the actual VOSTRO account of receiver and credits while sending the payment. The receiver maintains NOSTRO. |
| INDA | Indicates that an instructed agent settles the payment.  In this scenario, sending bank holds the NOSTRO account of receiver and credits while sending the payment. The receiver maintains actual VOSTRO account. |
| COVE | Indicates that the payment being settled through cover.  When a customer payment is settled using cover method, the debtor agent sends a direct message to the creditor agent. This announcement message should have settlement method as COVE.  A separate cover message moves the funds through reimbursement agents, which follows INDA/INGA as settlement method. |
| CLRG | When the payment is sent through a MX based local clearing (like TARGET2), then the settlement method is populated with value CLRG. |

For an outgoing payment captured in `PO` application or OE screen, system maps the settlement method as mentioned below:

- If the credit account type is NOSTRO, it is mapped as INDA
- If the credit account type is VOSTRO, it is mapped as INGA
- If the customer payment is settled using cover, then for the customer payment it is mapped as COVE
- If the routing channel is clearing, then it should be mapped as CLRG (in the respective mapping of the clearing)

When this field is received in an incoming message, the settlement priority details is stored in the system. There is no specific processing done in the system for this information. In a redirected payment, the settlement method is populated based on the logic mentioned above. This information is not displayed in the view and repair screens.

While an incoming CBPR+ payment is received and cannot be processed, the system checks the settlement method to decide whether to reject or return.

- If settlement method of incoming message is INGA, then it should be returned (as the instructing agent has already performed the settlement)
- If settlement method of incoming message is INDA or COVE, then it should be rejected (since the instructed agent have not yet performed the settlement)

[Settlement Account](#)

For correspondent banking scenario, settlement is done using NOSTRO or VOSTRO relationship. There is a possibility for a bank to maintain multiple VOSTRO account with their correspondent. In such a scenario while sending a payment instruction, the sending bank can instruct the receiver to use a specific VOSTRO account for debiting, instead of using the preferred VOSTRO. This is an optional information.

The *Settlement Account* field in the LORO NOSTRO table is used to provide this specific account details to the receiver, when multiple account relationship is available. The actual account number (in the receiver bank) should be maintained in the LORO NOSTRO configuration. The system populates the actual account number in settlement account tag while sending the message.

This is similar to Tag 53B of SWIFT MT message.

[Instruction Identification](#)

The instruction identification is a point-to-point reference that can be used between the instructing agent and the instructed agent to refer to the individual instruction. This is a mandatory information.

Since this is a point-to-point reference in a redirected payment, the received instruction identification is not passed, and a new value is assigned.

For payments, the system assigns the generated FTNumber as the instruction identification for outgoing and redirected payments.

Instruction identification must not start or end with a slash '/' and must not contain two consecutive slashes '//'.

[End To End Identification](#)

Identification as assigned by the initiating party, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire payment chain. This is a mandatory information.

While capturing a payment (for example, using OE, POA or pain.001), if end-to-end identification is provided, the same value is populated in the outgoing message. Otherwise the fixed value, NOTPROVIDED is populated.

For a redirected payment, the system populates the same value as received.

For a customer payment settled using cover method, the end-to-end identification in the cover message (pacs.009 COV) is populated with the instruction identification of the customer payment.

[Transaction Identification](#)

Identification as assigned by the first instructing agent, to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire interbank chain. This is an optional information.

For an outgoing payment captured in the system, transaction identification is populated with the FTNumber.

The system populates the same value as received for a redirected payment.

[Unique End to End Reference (UETR)](#)

Unique End to End Reference (UETR) is a universal unique identifier to provide an end-to-end reference of a payment transaction. This is a mandatory information.

The system supports generation of UETR for outgoing payments captured in the system.

The system populates the UETR as received for a redirected payment.

It is possible to receive UETR in a pain.001 message. For example – CBPR+ pain.001 has mandatory UETR tag. However, it may be optional in other pain.001 messages that are supported through client channels.

- If UETR is received in pain.001 message, it is stored as part of the payment instruction in the system.
- If the payment results in an outgoing Customer Transfer (CBPR+ or through a clearing such as TARGET2, CHAPS or SIC), the received UETR is passed in the UETR element in the outgoing interbank customer transfer (pacs.008)

[Instruction Priority](#)

Instruction Priority is an indicator of the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the instruction. This is an optional information.

This field allows the following values for instruction priority:

| Value | Description |
| --- | --- |
| NORM | Indicates that the priority level is normal |
| HIGH | Indicates that the priority level is high |

The system supports the capture and population of instruction priority as mentioned below –

- When a payment is captured using the `PO` application, the user can specify the message priority as NORM or HIGH
- When a payment is captured or repaired using the OE screen, the user can specify the message priority as a numerical value (from 1 to 9)
  - value greater than 5 is mapped as HIGH
  - value blank or less than or equal to 5 is mapped as NORM

The system allows the user to modify the received instruction priority. The priority is passed either as received or as modified, for a redirected payment.

The priority to map this information from the incoming CBPR+ pain.001 message is as follows:

- Payment Information level
- If the information is not present at Payment Information level, then Payment Information > Credit Transfer Transaction Information level is used.

[Settlement Priority](#)

The Settlement Priority indicates the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the settlement instruction. This is an optional information.

The following are the values allowed for settlement priority:

| Value | Description |
| --- | --- |
| NORM | Indicates that the priority level is normal |
| HIGH | Indicates that the priority level is high |
| URGT | Indicates that the priority level is urgent (highest priority possible) |

The system supports capturing of settlement priority when outgoing payment is initiated using the `PO` application or OE screen.

When this field is received in an incoming message, the details are stored in the system like a code word, as follows:

- Information code = INSSDR
- Code word = STTLMTPY
- Code word text = <settlement priority value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

For a redirected payment, the settlement priority is passed as received.

[Clearing Channel](#)

Specifies the clearing channel to be used for processing the payment. This is an optional information.

Allowed values are:

- BOOK - BookTransfer (Payment through internal book transfer)
- MPNS - MassPaymentNetSystem (Clearing channel is a mass payment net settlement system)
- RTGS - RealTimeGrossSettlementSystem (Clearing channel is a real-time gross settlement system)
- RTNS - RealTimeNetSettlementSystem (Clearing channel is a real-time net settlement system)

The system supports capturing clearing channel while initiating payment using Payment Order or Order Entry.

When this field is received in an incoming message, the details are stored in system like a code word:

- Information Code = INSBNK
- Code Word = RT
- Code Word text = <clearing channel value received>

There is no specific processing done in system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

[Service Level](#)

This indicates agreement under which or rules under which the transaction should be processed. Service level can be provided in coded or proprietary form. SWIFT recommends to use the coded form.

This is an optional information and if provided maximum three occurrences of service level is mapped (which could be combination of codes and proprietary form).

Service Level / Code is also used to transport the GPI (Global Payments Innovation) Service Identifier. Hence when an outgoing or redirected message is generated, the system checks if the bank is GPI enabled (configured in company properties). If the bank is GPI enabled, then the system automatically adds ‘G001’ as the service level:

- Customer Transfer (pcs.008)
- Bank Transfer Cover (pacs.009 COV)

Therefore users should not select G001 service level code while capturing payments, whereas it is automatically added in the generated message. GPI identifier is not added for any other outgoing or redirected messages except the two mentioned above.

When coded form is used, the code should be a valid one as per ExternalServiceLevel1Code list. This information is available at [External code sets | ISO20022](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets).

When the user captures the payment using `PO` application or OE screen, dropdown fields lists the service level codes. The user can select the appropriate service level code from the dropdown. No separate validation is done on the applicable codes.

When this field is received in an incoming message, the service level details are stored in the system like code word, as follows:

- Information code = INSBNK
- Code word = SVCLVL (code) or SVCLVLPY (proprietary)
- Code word text = <the code or proprietary value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if configured for outbound code word generation.

When an incoming customer transfer (pacs.008) is processed, all received service level codes except ‘G001’ is stored as mentioned above. If the system receives ‘G001’ as service level code, it is updated as ‘001’ in the *ServiceTypeIdentifier* field (of POR.SUPPLEMENTARY.INFO).

The priority to map this information from the incoming CBPR+ pain.001 message is as follows:

- Payment Information level
- If the information is not present at Payment Information level, then Payment Information > Credit Transfer Transaction Information level is used.

[Local Instrument](#)

This indicates a user community specific instrument. Local instrument can be provided in coded or proprietary form. SWIFT recommends to use the coded form. This is an optional information.

When using a coded form, the code should be a valid one as per the ExternalLocalInstrument1Code list. This information is available at [External code sets | ISO20022](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets).

When the user captures a payment using the `PO` application or OE screen, dropdown fields, which lists the local instrument codes, are provided. The user can select the appropriate local instrument code from the dropdown. No separate validation is done on the applicable codes.

When Temenos Payments Hub receives this field in an incoming message, the local instrument details are stored in the system as code words:

- Information code = INSBNK
- Code word = LCLINSCD (code) or LCLINSPY (proprietary)
- Code word text = <the code or proprietary value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

The received information is passed as it is in a redirected payment.

The priority to map this information from the incoming CBPR+ pain.001 message is as follows:

- Payment Information level
- If the information is not present at Payment Information level, then Payment Information > Credit Transfer Transaction Information level is used.

[Category Purpose](#)

The Category Purpose specifies the high-level purpose of the payment instruction based on a set of pre-defined categories. Category purpose can be provided in coded or proprietary form. SWIFT recommends to use the coded form. This is an optional information.

When the coded form is used, the code should be a valid one as per the ExternalCategoryPurpose1Code list. This information is available at [External code sets | ISO20022.](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets)

When the user captures the payment using the `PO` application or OE screen, dropdown fields, which lists the category purpose codes, are provided. The user can select the appropriate category purpose code from the dropdown. Separate validation is not done on the applicable codes.

When this field is received in an incoming message, the category purpose details are stored in the system as code words:

- Information code = INSBNK
- Code word = CYPURPCD (code) or CYPURPPY (proprietary)
- Code word text = <the code or proprietary value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if configured for outbound code word generation.

The priority to map this information from the incoming CBPR+ pain.001 message is as follows:

- Payment Information level
- If the information is not present at Payment Information level, then Payment Information > Credit Transfer Transaction Information level is used.

[Settlement Time Indication](#)

This provides the information on the occurred settlement time of the payment transaction. This is an optional information. This is not relevant for outgoing payment capture.

When this field is received in an incoming message, settlement time indication fields are stored in the system as code words:

- Information code = TIMIND

- Code word = DBTTIME or CDTTIME
- Code word text = <time value received>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed as received.

The system supports the following Settlement Time Indication fields.

| Field | Description |
| --- | --- |
| *Debit Date Time* | Specifies date and time at which the payment is debited at the transaction administrator. The date and time is defined with UTC offset (YYYY-MM-DDThh:mm:ss.sss+/-hh:mm).  For TARGET2, it indicates the date and time at which the payment is processed and debited at the central bank |
| *Credit Date Time* | Specifies date and time at which the payment is credited at the transaction administrator. The date and time is defined with UTC offset (YYYY-MM-DDThh:mm:ss.sss+/-hh:mm).  For TARGET2, it indicates the date and time at which the payment is processed and credited at the central bank |

This is not relevant for outgoing payment capture. When received in an incoming payment, the system stores the data.

[Settlement Time Request](#)

The user can provide information on the requested settlement time(s) of the payment instruction. The system supports to capture the following settlement time indication fields and sends in the generated message.

The user should enter the data in the settlement time request fields using format HH:MM:SS+/-hh:mm (where, HH – hour, MM – minute, SS – second, +/- hh:mm indicates offset in hour and minute).

The user should enter the offset while capturing the details, otherwise the system considers offset as +00:00.

- If time is entered as HH:MM+/-hh:mm, the system considers the time as HH:MM:00+/-hh:mm and processes further
- If time is entered as HH:MM, then systems consider the time as hh:mm:00+00:00 and processes further.
- If time is entered as HH:MM+/-, then systems consider the time as hh:mm:00+/-00:00 and processes further.

When this field is received in an incoming message, the time settlement and time indication fields are stored in system as code words:

- Information code = TIMIND

- Code word = CLSTIME or TILLTIME or FROMTIME or RJCTTIME
- Code word text = <time value received>

There is no specific validation or processing done in system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed as received if configured for outbound code word generation.

The system supports the following fields in the Settlement Time Request field.

| Field | Description |
| --- | --- |
| *CLS Time* | Indicates the time by which the money must be credited, with confirmation, to the CLS Bank’s account at the central bank.  Time must be expressed in central European time (CET). |
| *Till Time* | Indicates the time until when the payment may be settled |
| *From Time* | Indicates the time from when the payment may be settled |
| *Reject Time* | Indicates the time by when the payment must be settled to avoid rejection. |

[Instruction for Creditor Agent](#)

This specifies further information related to processing of the payment instruction, provided by the initiating party and intended for the creditor agent. This is an optional information consisting of instruction code and information.

Following are the allowed values for instruction code:

| Value | Description |
| --- | --- |
| CHQB | Pay Creditor By Cheque ((Ultimate) creditor must be paid by cheque) |
| HOLD | Hold Cash For Creditor (Amount of money must be held for the (ultimate) creditor, who will call. Pay on identification.) |
| PHOB | Phone Beneficiary (Please advise/contact (ultimate) creditor/claimant by phone) |
| TELB | Telecom (Please advise/contact (ultimate) creditor/claimant by the most efficient means of telecommunication) |

If the user selects a code, additional information can be provided using the information field, such as the phone number of beneficiary and so on.

For customer payment, all the above mentioned codes are allowed. For bank transfer, CHQB and HOLD are not allowed.

The same code cannot be repeated, each code is allowed only once.

Maximum two occurrences of instruction for creditor agent are mapped.

- If the user enters the CHQB Instruction Code, then HOLD is not allowed
- If the user enters the PHQB Instruction Code, then TELB is not allowed

When a payment is captured using the `PO` application or OE screen, dropdown fields, which lists the instruction codes, are provided. The user can select the appropriate instruction code from the dropdown and enter additional information.

When this field is received in an incoming message, the instruction for creditor agent details are stored in system as code words:

- Information code = INSBNK
- Code word = <received instruction code>
- Code word text = <received instruction information>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if configured for outbound code word generation.

In case of direct and cover message, the Instruction for Creditor Agent from the underlying announcement message is not included in the cover message in Instruction for Creditor Agent under Credit Transfer Transaction Information tag element.

Since this information is for the creditor agent with respect to underlying credit transfer which is passed in the pacs.008 or pacs.009 ADV message and not included in the pacs.009 COV (cover for customer transfer) or pacs.009 (cover for bank transfer) message.

[Instruction for Next Agent](#)

Specifies further information related to processing of the payment instruction, which may need to be acted upon by the next agent. This is an optional information consisting of only textual information (no code).

A maximum of six occurrences of Instruction for Next agent is mapped.

When the user captures a payment using the `PO` application or OE screen, dropdown fields, which lists the instruction codes, are provided. The user can select the appropriate instruction code from the dropdown and enter additional information.

If the user enters more than six occurrences of information using the PO application or OE screen, then the system displays an error message as **Instruction for Next Agent cannot exceed 6 lines**. Similarly, when the user enters more than the allowed number of characters, then the system displays an error message as **Max 35 characters allowed in each line of instruction information**.

When this field is received in an incoming message, the instruction for next agent details are stored as mentioned below (even though it does not have a code):

- Information code = INSSDR
- Code word = NULL (no value)
- Code word text = <received instruction information>

There is no specific processing done in the system for this information. The inbound code word configuration can be used to influence payment processing based on this information.

In a redirected payment, the received information is passed if configured for outbound code word generation. In a redirected payment, if more than six occurrences of instruction information is received, then the system maps only six occurrences in the outgoing message and ignores the remaining occurrences. Similarly, if more than 35 characters of additional information is received in the redirected message, then the system maps only 35 characters in the outgoing message and truncates the remaining characters.

In a redirected payment the received information is passed if configured for outbound code word generation.

[Purpose](#)

Specifies the underlying reason for the transaction. It is used by the end-customers such as initiating party, (ultimate) debtor, and (ultimate) creditor to provide information on reason of the transaction. It is not used for processing by any of the agents involved in the payment chain. This is an optional information.

The user can provide the purpose in coded or proprietary form. SWIFT recommends to use the coded form.

When the user uses the coded form, the code should be a valid one as per the ExternalPurpose1Code list. This information is available at [External code sets | ISO20022.](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets)

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
- Details – Provides details on the regulatory reporting information. Multiple occurrence are allowed. It consists of the following fields
  - Type
  - Date
  - Country
  - Code
  - Amount
  - Information (multiple occurrence)

When an incoming payment is received with regulatory reporting information, the details are stored in the system. If the payment is redirected, the received regulatory reporting information is passed unchanged.

There is no specific validation or processing done in the system for this information.

In ISO20022 format message processing, regulatory reporting details is not considered as code word.

- This is similar to regulatory reporting Tag 77B of MT message.
- In MT message, the details are very limited whereas in ISO20022 format the details are more with multiple repeating values

[Related Remittance Information](#)

This provides information related to the handling of the remittance information by any of the agents in the transaction processing chain. This is an optional information.

The system does not provide option to capture related remittance information while capturing payments using the `PO` application or OE screen. This information is not displayed in view or repair screens.

However, if this information is received in incoming message, the same is stored in the system. For a redirected payment the received information is passed unchanged.

Either Related remittance Information element or Remittance Information element should be used. Do not use both the elements.

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
- When structured remittance information is received in a pain.001 (v9) message or in an incoming SWIFT ISO20022 format payment, the system stores the entire details in the XML format (maximum ten occurrences). While redirecting the payment, only the first occurrence from the received XML is passed (because of system limitation) without any modification.
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

Rule for capturing the remittance information are as follows:

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

SLEV (following service level) charge code is not supported in system. Hence this option is not provided in the `PO` application and OE screen. If SLEV is received in an incoming message, the system saves it and treats as SHAR.

The priority to map Charge Bearer from the incoming CBPR+ pain.001 message is as follows:

- Payment Information > Charge Bearer
- If the above tag is not present, Payment Information > Credit Transfer Transaction Information > Charge Bearer is used.

[Charges Information](#)

Provides information about the agents in the payment chain who have paid the charges or to whom charges are due. This is a mandatory information if charge is deducted and optional for initiator if charges are not deducted.

It consists of following two elements. If the user provides the charges information, then both these elements must be provided.

| Element | Description |
| --- | --- |
| Amount | Indicates the charge amount along with the currency. |
| Agent | Identifies the agent who has paid the charges or to which it is due. In ISO20022 format, charge agent can be represented using the following elements:   - BIC - LEI - Clearing System id and Clearing Member id - Name - Postal Address - structured or hybrid |

When outgoing payment is processed in the system and charges are deducted, the system populates the BIC of the charge agent only along with the charge amount and currency in the generated message.

When an incoming message is received, the system stored all the charge information. If the payment is redirected, the system populates the received charges information and then adds its own charges (BIC, amount and currency) for SHAR and CRED scenarios.

- Charge bearer is similar to Tag 71A (details of charges) in MT message, which can have SHA/BEN/OUR as charge code.
- Charges information is similar to 71F (sender’s charges) and 71G (receiver’s charges) in MT message.
- In MT message, only charge amount and currency is specified and charge agent details are not specified. However in MX, charge agent is also required. Therefore, if an incoming MT message with charge is received and redirected as MX message, the charge agent Name and Address lines are populated as NOTPROVIDED.

## Supported Characters in ISO Message

All SWIFT ISO MX message elements (fields) that have data type defined as Text are allowed to have only FIN X characters. The table below shows the basic FIN X characters:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| a-z | A-Z | 0-9 | / | - | ' |
| ? | : | ( ) | . | , | + |

- End to end identification
- Instruction information
- Regulatory reporting tags
- Organization and private XML elements and sub-elements

In addition, SWIFT MX allows certain special characters in specific text elements. The list of XML elements are:

- Name and address fields of all party and agents of the transaction.
- Remittance information of unstructured and structured tags.
- Related remittance information tags.
- Province of birth, city of birth fields of all parties which comes under private identification tags.
- Email address elements, for example, proxy identification fields of debtor account, debtor agent account, creditor account, creditor agent account and so on.

The list of allowed special characters are:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ! | # | & | % | \* | = | ; | [\] | > < |
| ^ | \_ | ’ | {|} | ~ | " | @ | $ |  |

[Supporting SWIFT MX Messages Sent to SWIFT](#)

Temenos Payments Hub sends SWIFT ISO MX messages to SWIFT through the Delivery module in Transact. The Delivery module has the capability to define or configure the basic Latin characters and the list of allowed special characters are per ISO message type and carrier (such as, CBPR+, TARGET2, CHAPS). The XML elements for basic Latin characters and for special characters before validation are configured in the Delivery module:

- Temenos Payments Hub interacts with the Delivery module through an API to validate the character set as per the configuration in the Delivery module before forming the document section of the XML. This ensures that the formed XML document contains only the valid character set.
- As part of character validation process, if there are any XML elements found with the character that is not allowed as per the CBPR+ guidelines, then the elements are replaced with the defined replacement character, configured for all carriers sent through the Delivery module.
- If there is no replacement character found in the configuration for any of the restricted character, then the restricted characters are replaced with the default character (full stop) in the outgoing SWIFT MX message.
- After replacement, if the number of characters exceed the allowed length of any tags, then the system does not truncate the characters and forwards the message to the network as is.
- The replaced character is visible only as part of the outgoing message and is not reflected in the payment transaction present in the system.

For SWIFT MX, the following message types are configured in the Delivery module for character conversion and validation:

- pacs.008
- pacs.009, pacs.009 COV, and pacs.009 ADV
- pacs.004
- camt.056
- camt.029
- camt.054
- camt057
- TRCK.001
- pacs.002

- For pacs.002 and pain.002, party details are not populated in the outgoing message, hence there is no validation for special characters. Only additional information tag needs to be validated.
- For all the SWIFT MX messages except camt.054, Temenos Payments Hub is responsible for generating the document section of XML. For these message types, instead of configuring each XML element that must be validated, the user must configure the two types (basic and extended) in the Delivery module. Temenos Payments Hub has grouped these elements in two logical groups to avoid manual effort of configuring every XML element that requires character validation.

Refer to the [Configuration](Configuration.htm) section for more information.

[Support for SWIFT MX Messages Received through SWIFT](#)

When Temenos Payments Hub receives the incoming SWIFT ISO message with the escape characters such as ‘&lt’, ‘‘&gt’, ‘&amp’, ‘&quot’, ‘&apos’, the system converts these escape characters to (<), (>), (“), (‘), (&) and stores it as part of the payment transaction.

If the payment must be redirected to the next agent in the payment chain, these characters are replaced again as ‘&lt’, ‘‘&gt’, ‘&amp’, ‘&quot’, ‘&apos’ before they are sent out to the SWIFT network. This process is done as part of XML convertor.

## Data Enrichment for MT and MX Format Conversion

SWIFT’s migration to MX (ISO20022) format does not follow a big bang approach, there is a co-existence of MT and MX format.

Banks can receive and process incoming messages in both MT as well as MX format. The system provides configurable option for a bank to decide whether they want to send cross border payments in MT (means staying in MT format) or MX format (means migrating to MX format). When a bank sends outward messages (outgoing or redirected) following scenarios are possible:

- Receive an incoming payment in MT format and redirect in MX format through SWIFT
- Receive an incoming payment in MT format and redirect through a PMI (Payment Market Infrastructure) in MX format
- Receive an incoming payment in MX format and redirect in MT format through SWIFT
- Receive an incoming payment in MX format from a PMI and redirect through SWIFT in MT format

PMI is a payment market infrastructure such as TARGET2, CHAPS, CHATS, and so on. The PMIs are using MT or MX or proprietary format messaging.

The system provides the functionality to perform automatic enrichment of data for such scenarios.

Similarly, banks can receive payment initiation request through pain.001 (v9), which is XML-based. If the processed customer payment is to be routed as MT103 message through a SWIFT based channel, then the system performs enrichments so that proper MT message is generated.

These enrichments are performed as part of R&S (Routing and Settlement) when outgoing channel is being determined. The system performs the data enrichments based on the incoming and outgoing channel formats.

[Incoming MT format and Outgoing Non MT](#)

The following section explains about various data enrichments performed by the system when it receives an incoming message in the MT format (a SWIFT cross border payment or from a SWIFT Based PMI) and to be redirected in MX format.

The system supports the following MT to MX conversions

- MT103 to pacs.008
- MT101 to pacs.008
- MT 202 to pacs.009
- MT202 COV to pacs.009 COV

In case of a cover message (MT202 COV to pacs.009 COV), the sequence B data is transformed into pacs.009 COV underlying customer credit transfer block through mapping routine while the message is generated. No automatic enrichment is performed for this sequence B data.

[Name and Address Enrichment](#)

The system performs name and address enrichment for debtor (Tag 50) and creditor (Tag 59) as per PMPG guidelines. The same logic is applied even for agent roles (tag 52, 53, 54, 55, 56, 57) as well.

[Structured SWIFT FIN (MT) to Unstructured MX](#)

When the system receives an incoming MT message with structured address in the party roles (Tag 50F and 59F), then it should be enriched to map to the unstructured address lines in MX message. The following snippet shows the sample enrichment.

/Introduction_3.png)

If LEI (Legal Entity Identifier) is received for ordering customer and beneficiary customer, they are enriched in the following way.

- Ordering Party - Tag 50F: if LEI is received as 6/XY/LEIC/<LEI>, then it is mapped to LEI element for debtor role.
- Beneficiary - Tag 59F: if LEI is received as 3/XY/LEIC/<LEI>, then it is mapped to LEI element for the creditor role

Here, XY indicates country code and /LEIC/ indicates that the following data is legal identifier code. All the data before the actual LEI is ignored while enriching.

If the name and address data are truncated as part of conversion, a ‘+’ sign is added at the end of the data field to indicate truncation.

- SWIFT deprecates MT103 and MT202 (and variants) messages from CBPR+ flow with SR2026 go-live (November 2026).
- Support of Unstructed address will end with SR2026 go-live.

[Unstructured SWIFT FIN to Unstructured MX](#)

When incoming MT message is received with unstructured address in the party roles (Tag 50 and 59 without using F format), then it should be enriched to map to the unstructured address lines in MX message. The following snippet shows the sample enrichment.

/Introduction_4.png)

Apart from Debtor and Creditor, the above mentioned address format conversion is also applied for all the agent roles.

- SWIFT deprecates MT103 and MT202 (and variants) messages from CBPR+ flow with SR2026 go-live (November 2026).
- Support of Unstructed address will end with SR2026 go-live.

[National Clearing Code (NCC) Enrichment](#)

If NCC is received in MT message for any agent, then the system performs enrichment so that it can be mapped as clearing system identification and clearing member identification in MX format.

- Incoming MT103 has NCC details as //SC123456. Then in the outgoing MX message, it should be populated with clearing system id as GBDSC and member id as 123456. Here SC is the two character code used for MT messages, GBDSC is the five characters ISO clearing system identification used in MX messages and // indicates NCC in MT format.
- When the Reference Data (RD) module is installed, the system refers to the RD.CTRY.NAT.SYS.IDENTIFIER application to perform this NCC conversion.

If RD module is not installed, then the system refers to the ISO.CLEARING.SYSTEM.ID application where the details are maintained.

[Instruction Code (Tag 23E)](#)

If the following code words are received in Tag 23E of MT103, then the system performs the following enrichment by inserting new records so that these code words are mapped in the respective MX fields:

- INTC and CORT are enriched as Category Purpose Code
- OTHR is enriched as Category Purpose Proprietary
- CHQB,HOLD,PHOB,TELB enriched as Instruction for Creditor Agent
- SDVA is enriched as Service Level Code

Apart from the code words mentioned above, if the system receives any other code words in 23E, the code words are not enriched.

When the system enriches these code word records, new records are inserted and received data is not deleted.

[Time Indication (Tag 13C)](#)

If the following code words are received in tag 13C, then the system performs the following enrichment by inserting new records so that these code words can be mapped in the respective MX fields:

- CLSTIME (CLS Time) is enriched to be mapped to Settlement Time Request/CLS Time
- SNDTIME (Receive Time) is enriched to be mapped to Settlement Time Indication/Debit Date Time
- RNCTIME (Send Time) is enriched to be mapped to Settlement Time Indication/Credit Date Time

The MT time format is also converted into MX format in the enriched record.

When the system enriches these code word records, new records are inserted and received data is not deleted.

[Transaction Type Code (Tag 26T)](#)

If transaction type code is received in Tag 26T, then the system inserts a new record so that it can be mapped to the *Transaction Purpose Proprietary* field of the respective MX message.

When these code word records are enriched, new records are inserted and received data is not deleted.

[Remittance Information (Tag 70)](#)

If remittance information is received in Tag 70, then it is mapped to *Unstructured Remittance Information* field of respective MX message.

If Tag 70 contains /ROC/, then the subsequent content is populated as Customer Specified Reference (so that it can be mapped as End to End identification).

If Tag 70 contains /ROC/INFORMATION1234, then enrichment is done to populate a new record as shown below.
POR.Transaction > CustomerSpecifiedReference = INFORMATION1234
where, the received message INFORMATION1234 is stored in the *CustomerSpecifiedReference* field of the POR. Transaction table

[Sender to Receiver Information (Tag 72)](#)

The system enriches the information received in Tag 72 as mentioned below.

- For each occurrence of /INS/<BIC>, the system creates a new record for previous instructing agent role and maps the BIC (maximum 3 roles are populated)
- Remaining details of Tag 72 are mapped to the *Instruction for Next Agent* field in the MX message.

[Charge Details (Tag 71A, 71F/G)](#)

The system enriches/maps the charge details received in the incoming MT message as mentioned below:

| Charge Details | Enrichment |
| --- | --- |
| Charge code (Tag 71A) mapping | SHA is mapped as SHAR  BEN is mapped as CRED  OUR is mapped as DEBT |
| Charge Agent mapping | If the system receives one or more charge details (Tag 71G or 71F), then a new corresponding record is inserted for each charge details to populate the charge agent role:  If charge code = SHA or BEN, then a charge agent record is added with received amount and currency. Name and Unstructured address lines are saved as NOTPROVIDED (as charge agent details are not available in Tag 71). |

[Regulatory Reporting (Tag 77B)](#)

If the regulatory reporting details is received in Tag 77B, then the system inserts a new record to create a regulatory reporting record as per MX format as mentioned below:

- ORDERRES is mapped as DEBT
- BENEFRES is mapped as CRED
- Country code is mapped as Country code
- Information after code word is mapped as Information Line (removing //).

[Incoming MX Format and Outgoing MT Format](#)

The following section explains about the various data enrichments performed by system when an incoming message is received in MX format (a SWIFT cross border payment or from a SWIFT Based Payment Market Infrastructure (PMI)) and to be redirected in MT format.

The system supports the following MX to MT conversions:

- pacs.008 to MT103
- pacs.009 to MT202
- pacs.009 COV to MT202 COV
- pain.001 to MT103

In case of a cover message (pacs.009 COV to MT 202 COV), the underlying customer credit transfer information is transformed into sequence B through mapping routine while the message is generated. No automatic enrichment is performed for this sequence B data.

[Name and Address Enrichment](#)

The system performs name and address enrichment for debtor (Tag 50) and creditor (Tag 59) as per PMPG guidelines. The same logic is applied also for agent roles (tag 52, 53, 54, 55, 56, 57).

[Structured MX to Structured MT](#)

When the incoming MX message is received with name and structured address, then the system performs the following enrichments so that name and structured address are properly mapped in MT message.

/Introduction_5.png)

/Introduction_6.png)

/Introduction_7.png)

- If BIC is not present, then enrich the XML name and address elements into corresponding F option (if supported by the MT tag). Use comma (‘,’ without space) as a delimiter to separate various available data elements in the sub-fields 2/… (address) and 3/XY/… (town).
- If LEI is present, do not use the second line for name, truncate if needed using the ‘+’ sign as the last character. Truncate any other line the same way. Enrichment rules for LEI element are as follows:
  - Place LEI on last line of 50F or 59F, if space allows.
  - For 50F, insert a 6/XY/LEIC/ followed by the actual LEI. XY is the country code of the debtor.
  - For 59F, insert a 3/XY/LEIC/ followed by the accrual LEI. XY is the country code of the creditor.
- If LEI not present, use two lines for the name and truncate any other line, indicating truncation with the + character.
- If there is no LEI and single line name, then use two lines for the Country, Town fields and so on.
- If there is no second line for any other field, use two lines for the Street and Building fields.

[Unstructured MX to Structured MT](#)

If name and unstructured address is received, the system performs the following enrichments to map the data as structured name and address in the MT message.

If all occurrences of the unstructured address line starts with a SWIFT FIN qualifier, such as 2/ (up to two occurrences allowed) or 3/, then F format should be created for Tag 50 and 59. The mapping of the fields should be as follows:

| Field | Enrichment |
| --- | --- |
| *Name* | Enrich the Nm element (Name) so that it gets mapped as line 1 in MT field 50 / 59 with option F with the prefix ‘1/’ at the beginning of the line |
| *Address* | Enrich all occurrences of the unstructured AdrLine element to the residual lines of MT field 50 / 59 using option F preserving the prefix (2/, 3/) |

/Introduction_8.png)

The same enrichment (as mentioned above) is applicable for the address line starting with 4/, 5/, 6/, 7/, 8/.

- SWIFT deprecates MT103 and MT202 (and variants) messages from CBPR+ flow with SR2026 go-live (November 2026).
- Support of Unstructed address will end with SR2026 go-live.

[Unstructured MX to Unstructured MT](#)

If the system receives name and unstructured address in the incoming MX message, then the system performs the following enrichments, so that these can be mapped as unstructured address in the MT message.

For this scenario all the unstructured address lines in the MX message does not start with 1/ or 2/ or 3/.

| Field | Enrichment |
| --- | --- |
| *Name* | Map the Nm element (Name) to line 1 of the MT field 50 (with K letter option)  / field 59 (No letter option) |
| *Address* | Map all occurrences of AdrLine elements to the residual lines of the MT FIN field 50 / 59 |

/Introduction_9.png)

- SWIFT deprecates MT103 and MT202 (and variants) messages from CBPR+ flow with SR2026 go-live (November 2026).
- Support of Unstructed address will end with SR2026 go-live.

[National Clearing Code (NCC) Enrichment](#)

If the system receives the clearing system identification and clearing member identification in the MX message for any agent, then the system enriches the data in the equivalent MT format and populates in the account line.

Incoming pacs.008 has clearing system id as ‘GBDSC’ and member id as ‘123456’ for an agent. Then in the MT outgoing message, if NCC details is sent out, it should be populated as ‘//SC123456’. Here ‘SC’ is the two character code used for MT messages, ‘GBDSC is the five characters ISO clearing system identification used in MX messages and ’//’ indicates NCC in MT format.

When the Reference Data module (RD) is installed, the system refers the Country National System Identifiers (RD.CTRY.NAT.SYS.IDENTIFIER) application to perform the NCC conversion.

If the RD module is not installed, then the system refers to the ISO.CLEARING.SYSTEM.ID application where the details should be maintained.

[Instruction Code (Tag 23E)](#)

If the following code words are received in various XML tags of the incoming MX message, then the system performs the following enrichment by inserting new records so that these code words are mapped in the respective MT fields:

- Category Purpose Code - INTC and CORT are enriched so that it gets mapped to 23E
- Category Purpose Proprietary - OTHR are enriched so that it gets mapped to 23E
- Instruction for Creditor Agent - CHQB, HOLD, PHOB, and TELB are enriched so that it gets mapped to 23E
- Service Level Code - SDVA is enriched as 23E

Apart from the code words mentioned above, if the system receives any other code word in various MX tags, those codes are not enriched for mapping in 23E.

When these code word records are enriched, new records are inserted and the received data is not deleted.

[Time Indication (Tag 13C)](#)

If settlement time indication related XML tags are received in MX message, then the system performs following enrichments by inserting new records so that these code words can be mapped in the respective MT fields:

- Debit Time (DBTTIME) is enriched as SNDTIME
- Credit Time (CDTTIME) is enriched as RNCTIME

The MX time format is also converted into MT format in the enriched record.

When these code word records are enriched, new records are inserted and the received data is not deleted.

[Remittance Information (Tag 70)](#)

The system performs the following enrichments by inserting new record with information code RMTINF so that Tag 70 is populated as mentioned below:

- If the system receives the Ultimate Debtor information, then it is mapped as /ULTD/<ConditionalData>.

For /ULTD/, < ConditionalData> is derived as mentioned below:

```
If NAME is present
{
If both TOWN.NAME and COUNTRY are present then
            ConditionalData = /ULTD/NAME/COUNTRY/ TOWN.NAME
        Else if ORGANISATION IDENTIFICATION à OTHER IDENTIFICATION is
present then
            ConditionalData = /ULTD/NAME/ORG.ID.OTHER.ID
        Else
            ConditionalData = /ULTD/NAME
}
Else (means NAME is absent)
{
if ORGANISATION IDENTIFICATION à OTHER IDENTIFICATION is present then
ConditionalData = /ULTD/ ORG.ID.OTHER.ID
Else
ConditionalData = Empty
Do not populate any record with RMTIF and /ULTD/ combination
if DerivedData is empty.)
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

- If second intermediary agent is available, then it is mapped as /INTA/<BIC of Intermediary 2>.
- If third intermediary agent is available, then it is mapped as /INTA/<BIC of Intermediary 3>.
- If the Service Level code or proprietary is received, then the received purpose code is mapped as /SVCLVL/<received value> (except for service level code = SDVA or starting with G00).
- If the local instrument code or proprietary is received, then the received purpose code is mapped as /LOCINS/<received value>.
- If the category purpose code or proprietary is received, then the received purpose code is mapped as /CATPURP/<received value> (except for Category Purpose Code = CORT or INTC).
- If the instruction for next agent information is received, then the received information text is mapped as /REC/<received value>.
- If the Previous Instructing Agent 1 is available, then it is mapped as /INS/<Previous Instructing Agent 1BIC>.
- If the Previous Instructing Agent 2 is available, then it is mapped as /INS/<Previous Instructing Agent 2BIC>.
- If the Previous Instructing Agent 3 is available, then it is mapped as /INS/<Previous Instructing Agent 3BIC>.

If all the received information does not fit into Tag 72 of the MT message (due to length and number of line limitation), some information does not get transmitted in the generated MT message.

[Regulatory Reporting (Tag 77B)](#)

If the system receives the regulatory reporting details in the MX message, then the data is enriched so that it can be properly populated in Tag 77B of MT message.

- DEBT is mapped as ORDERRES
- CRED is mapped as BENEFRES
- Country code is mapped as Country code
- Regulator Reporting Information is mapped as Information Line after code

## BIC Directory

To send or receive SWIFT messages, the system uses BIC as the address. The system provides option to maintain the list of BICs for SWIFT enabled banks. The system looks up this BIC directory to validate a BIC used in SWIFT messages.

The centralized Reference Data module (RD) enables to upload swift reference files to maintain BIC directory.

Read the [Centralised Reference Data](https://docs.temenos.com/docs/Solutions/T24_Transact/Framework/RD/CRD/Misc/Introduction.htm) user guide for more information.

## Code Word

Code words are added as part of a cross border payment messages to convey payment processing information. SWIFT CBPR+ payments uses defined set of code words (as per SIO External Code list) for consistent processing across financial institutions. Additionally, banks can also make special agreements and define code words for payment processing as per their agreement among themselves. These are known as Bilaterally agreed code words.

The system supports processing of payments with code words. A payment can contain multiple code words. Based on code word ranking, a final code word is arrived at and used for further processing. The code words can be used to influence:

- Payment routing
- Fees
- Posting

When the system processes CBPR+ XML format messages, the following information is stored in the system as code word:

- Service Level
- Local Instrument
- Category Purpose
- Purpose
- Instruction for Creditor Agent
- Settlement Time Request

In SWIFT MT format payment messages, code words were allowed in Tag 23E (Instruction Code), Tag 70 (Remittance Information), Tag 72 (Sender to Receiver Information) and Tag 13C (Time Indication).

In ISO20022 format message there are several fields (as mentioned above) which may contain a code word (as per ISO external code list) or proprietary value. There is no one-to-one correspondence between the MT fields and MX fields, which may contain code words.

Read the [Code Words](../../../../Payments/PP/Payments_Hub_(PP)/Code_Word/Introduction.htm#) user guide for more details on booking related features and configurations.

## Duplicate Check

The system can be configured to perform duplicate check on payment instructions received from SWIFT. Duplicate criteria can be configured using the EB.DUPLICATE.TYPE application. The ID of record should be configured against the heavy weight products defined to process SWIFT payments (in *Duplicate Type* field).

The Business Application Header (BAH) of CBPR+ payments contains a possible duplicate field. This field is not used to determine duplicate payment. The users must define their own duplicate criteria using the EB.DUPLICATE application.

## Warehousing

The system provides option to create or receive future dated SWIFT payments in advance. These payments are held by the bank in warehouse and processed in time, honoring the future date as requested. The SWIFT payments are processed using STP engine and can be moved to one of the following warehouses:

- Payment (STP) warehouse – When the value of *Requested Execution Date* (Tag <ReqdExctnDt> in pain.001 message) or *Requested Credit Value Date* field is in future and the bank conditions indicate that the payment has to be warehoused, the payments are warehoused at the start of STP flow based on bank conditions
- Future due date warehouse – When calculated Credit Value date is in future and processing date is also pushed to future to meet the credit value date (Based on routing and cut off shifts)
- Send date warehouse – When Send date is in future

The warehoused payments are released based on the execution date or requested credit value date, when start of day (SOD) is performed.

The system provides options to manually cancel or release a warehoused payment.

Read the [Warehousing](../../../../Payments/PP/Payments_Hub_(PP)/Warehousing/Introduction.htm) user guide for more details on warehouse related features and configurations.

## Forex (FX)

The system supports processing SWIFT payments in currencies other than the local currency. FX is considered if the debtor’s or creditor’s account currency is different from the payment currency. The system does not support all three to be different currencies. Either debit account currency or credit account currency need to be the same as payment currency. Therefore FX happens either on the debit side or on the credit side but not on both sides.

The system uses the exchange rates maintained by the Temenos Transact FX module. The FX module stores the currency-wise rates date wise.

The system provides configurable options to:

- process FX transactions using STP or manually
- configure discount on exchange rate for customers through client agreements
- Rate Fixing – to process transactions using previous day’s rate or manually provided rate, when rates are not available for the current date.

Read the [Forex](../../../../Payments/PP/Payments_Hub_(PP)/FX/Introduction.htm) user guide for more information on forex related features and configurations.

## Payment Product for Processing SWIFT Payments

SWIFT based cross border international payments are processed using heavy weight product. The system is pre-configured with heavy weight products to process CBPR+ payments initiated from Payment Order, Order Entry and STP SWIFT payments.

The users can modify or define their own heavy weight products using the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Bank Operations Configuration** > **Product Determination** > **Product Condition – Heavy.**

Read the [Product Determination](../../../../Payments/PP/Payments_Hub_(PP)/Product_Determination/Introduction.htm) user guide (for more details on heavy weight product related features and configurations.

The camt.107 messages are processed using new heavy-weight product conditions.

## Filtering (Sanction Screening)

The system can be optionally interfaced with Filtering module to scan the payments before they are booked. Filtering helps to monitor various risks which are required for cross border payments such as:

- Disallowed counterparties, country, and currency
- Allowed exposure for a counterparty, country, and currency

Based on the filtering response, the system can be configured to:

- Park payment in repair
- Seize funds
- Return / reject based on payment type

Read the [Sanction Screening](../../../../Payments/PP/Payments_Hub_(PP)/Sanction_Screening/Introduction.htm) user guide (for more details on filtering related features and configurations.

## Booking

The system provides comprehensive configuration to define rules for booking entries based on payment characteristics. The system invokes the Temenos Payment DDA by providing all necessary information to book the entries. Payment characteristics are the characteristics included in payment product definition.

Different booking entries include:

- Principal, Charge, VAT bookings
- Rules to determine the Debit /Credit Accounts/Amount/Value Date for Principal, Charges and VAT
- Rules to suppress entries with zero amount

The user can also configure the posting of charges accounting entry. For instance, the following are possible:

- Posting charge separately from principal or along with principal
- Post charges separately and also in detail

The user can configure statement lines to produce statements as per customer requirement.

Read the [Posting](../../../../Payments/PP/Payments_Hub_(PP)/Posting/Introduction.htm) user guide for more details on booking related features and configurations.

## Charge Processing

The system supports the following charge code processing:

- CRED: All transaction charges are to be borne by the creditor (similar to charge code BEN)
- DEBT: All transaction charges are to be borne by the debtor (similar to charge code OUR)
- SHAR: Charges are shared. In a credit transfer context, SHAR means that transaction charges on the sender side are to be borne by the debtor, and the transaction charges on the receiver side are to be borne by the creditor. (similar to charge code SHA)

The system does not support the SLEV charge code (following service level). Hence, this option is not provided in Payment Order and Order Entry screens. If SLEV is received in an incoming message, it is saved and treated as shared (SHAR).

The system does not support fees calculation in case of a Bank Transfer.

Read the [Fees and Billing](../../../../Payments/PP/Payments_Hub_(PP)/Fees_and_Billing/Introduction.htm) user guide for more details on charge related features and configurations.

## FATF Regulation

The FATF regulations are the internationally endorsed global standards against money laundering and terrorist financing. They increase transparency and enable countries to successfully take action against illicit use of their financial system. FATF governs the ordering party details that are sent as part of SWIFT customer transfers. There are separate regulations for Europe and non-European regions.

The system supports this regulatory requirement by configuration.

Read the [FATF](../../../../Payments/PP/Payments_Hub_(PP)/FATF/Introduction.htm) user guide for more details on FATF related features and configurations.

## Relationship Management (RMA)

RMA is a bilateral agreement between banks to exchange specific SWIFT message types between themselves. The objective of RMA is to stop unwanted messages. With RMA, bank can decide:

- the banks who can send message to them
- the message types that the bank can send
- the dates within which they can send these messages

The system provides the option to capture and maintain RMA for SWIFT messages.

The system checks the RMA while sending SWIFT payments to another bank as part of R& S. This check decides whether the payment message can be sent or not. If RMA check fails for a bank, it implies that routing is not possible using SWIFT.

## Unstructured Address Mapping

Support for unstructured address format ends with go-live of SWIFT SR2026. TPH has been enhanced to restrict unstructured address format as SWIFT does not accept CBPR+ payments with unstructured address elements only.

## Direct and Cover Processing

This section explains the cover processing of both outgoing and incoming Customer and bank transfers. pacs.008 and pacs.009 COV are the messages used for the cover processing of customer transfer. pacs.009 Pre-advice and pacs.009 are the message used for the cover processing of bank transfers.

SWIFT International customer or bank payments can be settled using serial or cover method. The system supports generation of outward cover as well as processing of inward cover.

Following are the differences between a customer transfer settled using cover and a bank transfer settled using pre-advice method:

- For a bank transfer, the direct or announcement message sent to creditor agent is pacs.009 ADV (for customer transfer, it is pacs.008).
- For a bank transfer, the funds are moved using a normal pacs.009 message as cover (for customer transfer, it is pacs.009 COV).
- There is no separate tag in the pacs.009 message to indicate if it is a normal serial bank transfer or a cover against a pre-advice. The end-to-end identification in the pacs.009 core should be same as instruction identification of the pacs.009 ADV (in case of customer transfer pas.009 COV is a distinct message).
- The pacs.009 core can be routed through Instructing and Instructed reimbursement agents. Third reimbursement agent is not allowed (customer transfer allows Third reimbursement agent).

[Outgoing Direct and Cover Payments](#)

The system can send outgoing CBPR+ customer or bank payments through the SERIAL or COVER method based on the routing configuration.

If the creditor agent bank (Account servicing institution of creditor) has a direct correspondent relationship with the processing company, then the system can route the payment through LORO or NOSTRO. However, if the creditor agent bank is not reachable by a direct correspondent relationship, then a new credit bank is inserted into the payment. This new credit bank can be a country correspondent, currency correspondent, and so on. It is expected that the new credit bank(s) should route the payment to the creditor agent. Such payments can be routed using a SERIAL or COVER method.

- SERIAL - The payment message (pacs.008 or pacs.009) is sent to a correspondent bank (intermediary). The correspondent bank, in turn, is expected to route the payment message to the beneficiary bank. There can be multiple intermediary agents (up to three) in a CBPR+ payment.
- COVER - The announcement message (pacs.008 or Pacs.009 ADV) is sent directly to the creditor agent bank even if the company does not share an account relationship with it but maintains RMA. A separate cover payment message (pacs.009 COV or Pacs.009) is sent to clear and settle the payment at an inter-bank level through one or more reimbursement agents. In the cover scenario, the system first sends the announcement message and waits for a technical acknowledgment from the SWIFT gateway. After receiving a positive technical acknowledgment, the cover payment is released. The system provides a configurable option to set up the routing rules to define whether a customer payment should be sent through the SERIAL or COVER method.

There are two ways a cover can be generated while capturing outgoing CBPR+ customer or bank transfer payment.

- While capturing an outgoing transfer, the user can manually enter the Instructing and Instructed reimbursement agent details (in the routing tab of the ISO Bank Transfer screen). If all validations are successful, then the system would treat this like a create scenario and generate a CBPR+ announcement message sent to the creditor agent (pacs.008 in case of customer transfer, pacs.009 ADV in case of bank transfer) followed by a cover message sent through a reimbursement agent (pacs.009 COV in case of customer transfer cover, pacs.009 in case of bank transfer cover).
- Users can configure cover contract for the customer or bank transfer. If the cover contract is selected while processing the transfer, then the system generates an announcement and cover message.

[Debtor Details for Bank Transfer Cover Method](#)

When TPH generates an outgoing pacs.009 for an underlying pacs.009 ADV, debtor details of the pacs.009 ADV message is mapped as the debtor details (BIC/NCC/LEI or name & address) in the outgoing pacs.009 as per CBPR Q4 2021 UHB.

Similarly, when TPH receives a redirected pacs.009 message for which the creditor agent is reachable by direct and cover message, then pacs.009 ADV and pacs.009 (cover) are generated. The debtor details of the pacs.009 ADV message should not be mapped as the debtor details (BIC/NCC/LEI or name & address) in the outgoing pacs.009.

SWIFT has confirmed that the pacs.009 ADV model does not support the redirection use case. The model is fixed to the debtor agent sending the pacs.009 ADV to the creditor agent. The reason behind the message used is to settle the pacs.009 message is limited in providing transparency without changes to the ISO 20022 base pacs.009 message. However TPH does not restrict users from generating pacs.009 ADV and pacs.009 for the redirected pacs.009 if there is a necessary configuration in R&S.

[Creditor Details for Bank Transfer Cover Method](#)

When TPH generates an outgoing pacs.009 for an underlying pacs.009 ADV, the creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) InstInstruction for creditor agent, instruction information element preceded by /UDLC/ (Underlying Creditor) to provide party transparency in the settlement message as per CBPR Q4 2021 UHB.

- If a creditor is identified with a BIC, then BIC gets mapped.
- If the creditor is identified with a clearing system member ID or LEI, then it is not mapped.
- If the creditor is identified with a clearing system member ID or LEI along with Name and Address, then the following details are mapped:
  - In case of Name (140 chars) and Structured Address (Town Name (35 chars) and Country Code (2 chars))
    - /UDLC/<Name 134 chars>
    - /UDLC/<Name remaining 6 chars><Town 35 chars><Country Code 2 chars>

- If there are less than three address lines in the outgoing pacs.009 adv then (Name and two address lines)

- /UDLC/<Name 134 chars>
- /UDLC/<Name remaining 6 chars ><address line1 35 chars> <address line2 35 chars>

- If there are three address lines in the outgoing pacs.009 adv then (Name and three address lines)

- /UDLC/<Name 134 chars>
- /UDLC/<Name remaining 6 chars><address line1 35 chars><address line2 35 chars><Address line3 35 chars>

[Incoming Direct and Cover Payments](#)

The system provides a hold for cover option to park incoming announcement messages (containing reimbursement agent details through which cover is received) until funds are received through cover or a credit confirmation message.

- The last reimbursement agent may send a credit confirmation message (for example, camt.054 / MT910) to indicate the arrival of funds. This is the most used mechanism as the last reimbursement agent usually holds the Vostro account. It credits the Vostro and sends a credit confirmation. The announcement message parked for cover payment can be released on receipt of credit notification.
- The last reimbursement agent may forward pacs.009 COV or pacs.009 to the creditor agent. This is not a regular practice but may happen if the reimbursement agent holds Nostro of the creditor agent or if there is an agreement between them to always forward the covering message.
  - Once funds arrive through cover (pacs.009 COV) for the customer transfer the announcement message (pacs.008), the system automatically matches the cover against the previously received announcement message and completes the processing.
  - Once funds arrive through cover (pacs.009) for the bank transfer the pre-advice (pacs.009 ADV), then the process is either manual or automatic. This is because the received pacs.009 could be a normal bank transfer or a cover against the bank transfer pre-advice, and no separate indications in pacs.009, which identifies this to be a cover (in case of a customer transfer settled through cover, pacs.009 COV is a distinct message type based on which cover matching is triggered). Please read the below sections for more details.

The announcement message, for which funds are expected to arrive through cover can be configured to be processed

- STP without waiting for cover (Configuration in company properties as BLANK).
- STP without waiting for cover if the transaction amount is less than a configurable threshold (Configuration in company properties as LIMIT).
- once cover is received and matched (Configuration in company properties as COVER).

For a bank transfer cover pre-advice announcement message, the system does not refer the hold for cover configuration, and neither supports processing based on the limit. So, the hold for cover option is always implicitly considered as COVER when TPH bank receives a bank transfer pre-advice message. However, the existing cover suspense account category configurations are referred when required for posting.

If the pre-advice or announcement is incoming (TPH bank is the creditor agent), then the payment flow would end thereby crediting the creditor bank or the customer account. However, if TPH bank is just the receiver and credit agent is another bank, then the system credits the Nostro account of the next agent in the payment chain and forwards a new pacs.009 or pacs.008 serial payment to the next agent mentioned in the announcement message.

[When Announcement Message is Received (settled through cover)](#)

When an incoming announcement message (pacs.008 or pacs.009 ADV) is received, the system checks the following conditions to decide whether to hold the payment or continue processing without waiting for a cover.

- If the incoming payment contains BIC for the following reimbursement agents in the payment instruction:
  - Instructing Reimbursement Agent
  - Instructed Reimbursement Agent
  - Third Reimbursement Agent (not allowed in bank transfer.

If the incoming payment contains BIC, then the system understands that the funds are received via cover through these reimbursement agents through SWIFT or clearing. The system tries to determine the Loro or Nostro account for the latest reimbursement agent whose account has to be debited. If the debit account is not determined, then the payment is routed to the repair queue.

- If the beneficiary account of the payment message is a P&L account, the system does not wait for a cover message, and no record is created in the ER module for matching.
- If the determined debit account is of type LORO, the system checks if there is a debit authority to debit the account. If debit authority exists, then the system does not wait for the cover message even if the configuration is ‘Cover’ or ‘Limit’ and processes the payment message as STP. The following accounting entries are posted in the transaction:
  - Dr Reimbursement agent Vostro account
  - Cr Customer or Creditor account.

    If there is no debit authority, then the system waits for the cover message and sends the details to ER module for matching.
- If the determined debit account is of type NOSTRO, then

- For the bank transfer pre-advice message (pacs.009 ADV), the hold for cover configuration is never looked up, and is always considered as 'Cover'. So, the message is always parked in the Hold for Cover queue for matching.
- For the customer announcement message (pacs.008), the system checks whether the settlement method configured to process such payments is ‘Cover’ or ’Limit’. If the configuration is BLANK, the system does not send the details to ER module for matching and processes the received payment message as STP without waiting for Cover.

- For COVER configuration – The system sends payment details to the expected receipt module (ER) to find and match against a cover payment if already received and implies the debit account as cover suspense account. The record is created in the AC.EXPECTED.RECS(ER) application as ’Expected Cover’ for the payment message, and the message is parked in the Hold for Cover (130 status) queue. While sending the details of the payment message, the ER module validates the configuration of the determined debit account in the ER.PARAMETER table.
- For LIMIT configuration – The system sends the payment details to ER module, and ER checks if a limit is available for sender to cover the payment amount in the ER.COVER.LIMIT application. If the limit is available, the payment is released for further processing and processed to completed status. The accounting entries for such transactions are :
  - Dr Nostro of Reimbursement agent
  - Cr Customer account

If payment amount is not within the sender limit, then the system implies the debit account as cover suspense account and sends payment details to expected receipt module (ER) to find and match against a cover payment. The payment is parked on Hold for cover status (130). The payment is released later once cover payment is received or can be force released by the operator. Read [Manual Queues for cover processing for both customer and bank transfer cover](#Manual_Queue) for more information.

Once the announcement message (pacs.008 or pacs.009 ADV) is parked in the Hold for Cover queue, the creditor agent can receive either the credit confirmation message or the cover message from the last reimbursement agent, as explained above.

[When Credit Notification is Received](#)

When incoming credit notification (MT910 or camt.054) is received, it is stored in the Expected Receipts (ER) module as Received Cover. The ER checks if it is a duplicate, and if yes, the credit notification is ignored.

ER tries to match the received credit notification against already received payments (expected cover records) that are not yet matched.

If matching is successful, then forward entries raised earlier are deleted and the payment is released from the Hold for Cover status. If the payment is already released, then the audit trail is updated.

Below accounting entries are raised if the matching is successful for an announcement message :

- Dr Nostro of Reimbursement Agent (from whom the credit confirmation is received).
- Cr Customer or Creditor Account.

If matching is not successful, then a Received Cover record is created in ER for matching with payments received later.

The system does not support matching of payment based on other format of notifications such as MT 940/950, camt.053 and so on.

[When Cover Payment is Received for Pre-advice](#)

The normal bank transfer Pacs.009 core message is used as a cover for bank transfer pre-advice. There is no indication in this message to consider it as a cover and this message does not hold underlying customer credit transfer tag element as well. So, this can be processed as a normal bank transfer message or a cover message which is customisable by the bank.

If this message is treated as normal bank transfer message, then the matching between bank transfer pre-advice Pacs.009 ADV and the Pacs.009 message is always manual. If the pacs.009 core message is treated as a cover message (customised by the bank) for bank transfer pre-advice, then the matching is automatic. Both the processes are explained in the below sections.

[Manual Matching](#)

On receipt of pacs.009 message (Cover for Pacs.009 Pre-Advice) from the last reimbursement agent, TPH treats the message as a normal bank transfer and no matching is performed with the available pacs.009 pre-advice message.

Normally in this covering pacs.009, the creditor agent or beneficiary bank and creditor or beneficiary would be the TPH bank BIC (own company BIC). The system moves such incoming bank transfer (pacs.009) payments to repair queue (since the BENINS in pacs.009 is same as company BIC). The user manually verifies the Hold for Cover queue to check if there is a pre-advice already received and waiting for cover. The automatic matching is not performed to release the pre-advice from hold for cover. If a pre-advice is already available, then the user releases it manually from hold for cover queue. The pre-advice is processed with the following accounting entries:

- Dr Nostro account of Reimbursement Agent (From whom the funds will be received through Cover)
- Cr Creditor account

In order to complete the processing of the pas009 cover, the user can perform one of the following actions by opening the payment manually from the repair queue.

- Impose the credit account same as the determined debit account (Nostro account of reimbursement agent) and then commit and authorize the payment. The payment would get processed, and the accounting entries would be posted as below
  - Dr Nostro Account of Reimbursement Agent
  - Cr Nostro account of Reimbursement Agent (Same as debit account)
- Instead of processing the payment with same debit and credit account, the user can also cancel this transaction so that no accounting entry happens for the covering pacs.009 message. Transaction goes to Cancelled status.

If the Pre-Advice is incoming (means TPH bank is the creditor agent), then the payment flow would end there by crediting the creditor bank account. However, if TPH bank is just the receiver and credit agent is another bank, then the system credits the Nostro account of the next agent in the payment chain and forwards a new pacs.009 serial bank transfer payment to next agent mentioned in the pre-advice message.

[Manual Matching of Record in EC Application](#)

Since user manually force releases the pre-advice (pacs.009 ADV) from Hold for cover queue on receipt of covering pacs.009 message, the user can create a RC record manually in the AC.EXPECTED.RECS application and manually match the ER record and RC record.

[Automatic Matching](#)

The automatic matching of the Core Pacs.009 message with the bank transfer pre-advice message is customisable based on the bank requirements. The validation logic is not attached to the Pacs.009 core message from SWIFT or clearing as a product feature. It is attached at the client’s environment.

The validation criteria for a bank transfer to be identified as a cover for bank transfer pre-advice (Pacs.009 ADV) is as follow:

- Beneficiary or Creditor (BIC) is a TPH Bank processing BIC
- Beneficiary Account number is not present OR if beneficiary account is present (IBAN/BBAN) then it is not an account in the books of the TPH bank
- Instruction Information in 'Instruction for Creditor agent' tag is present with Codeword /UDLC/

Once all the above conditions are satisfied, the Pacs.009 message gets marked as cover and credit account of the cover payment is the configured cover suspense account. For the processing of Pacs.009 ADV and Pacs.009 core message, which is considered as cover, the configuration in company properties 'Hold for Cover' is not looked up. Read When cover payment is received for announcement message section for more information on the processing of cover message.

[When Cover Payment is Received for Announcement Message](#)

When incoming cover payment (pacs.009 COV or Pacs.009 (identified as cover)) is received through SWIFT or clearing, the system checks for the following:

- End to End identification in the cover payment is available and is not equal to NOTPROVIDED or empty.
- Beneficiary institution for the payment is same as receiving bank.

If the payment is identified as cover payment and if it satisfies the above two condition, then the system implies the credit account as Cover Suspense Account (Configurable in company properties) and sends the payment details to expected receipts module (ER) to find and match against the payment message, if already received. The details of the cover message are sent to ER module if the configuration in company properties is defined as COVER or LIMIT.

The system saves the entire content of the Underlying Credit Transfer *UndrlygCstmrCdtTrf*
tag as a **BLOB** in PRF.BLOB
. It does not store individual fields separately.

The following are the possible scenarios when the cover payment is received into the system:

[Announcement Message Not Waiting for Cover – Force released from Hold for cover queue or underlying message is processed based on LIMIT](#)

TPH checks if the payment message for the received cover is already processed when the cover message is received in the following scenarios:

- There could be a possibility that cover has already been received through another message, so the announcement message is forcefully released by the user from the Hold for Cover queue (130 status).
- Announcement message is processed already based on LIMIT configuration.

In all of these scenarios, if the payment message is already processed, then the received cover is parked in repair queue by raising a functional error for the operator to cancel the transaction.

Once cancelled, the received cover message is moved to the cancelled status (997). The accounting entries for the payment message are:

- Dr Nostro of Reimbursement agent
- Cr Customer or Creditor account

[Announcement Message Waiting for Cover](#)

On receiving the cover message, once it is identified as cover, TPH sends the details of the cover message to ER module for matching. ER checks if the payment message is already received based on payment characteristics (that is, Sender, Amount, Currency, Value Date, Transaction Reference and so on). The matching criteria to match between payment message and the cover message is configurable in ER module in ER.MATCHING.CONDITION. If the payment message is already received, the received cover record is matched against the expected cover record and forward entries are deleted on the credit account. The payment is released from the awaiting cover status.

The accounting entries for the cover message once it is matched with an announcement message are:

- Dr Nostro
- Cr Cover Suspense Account

The accounting entries for the announcement message are:

- Dr Cover Suspense Account
- Cr Customer or Creditor Account

[Announcement Message not Waiting for Cover – Payment in Repair or Warehouse](#)

If the payment message is in repair status due to some business validation error or if it’s a future dated transaction, then the details are not sent to ER module for matching. In the meantime, if the cover message is received, it gets routed to 'Cover Payments Unmatched' enquiry (120) for matching. The details of the cover message are sent to ER module and Received Cover RC record gets created.

Once the error is rectified for the payment message or released from warehouse, the details are sent to ER module for the payment message and the expected cover EC record gets created. Once the EC record is created, the matching happens for both payment and cover message. Both the messages are automatically released from enquiry and processed to complete.

The accounting entries for the cover message once it is matched with an announcement message are:

- Dr Nostro
- Cr Cover Suspense Account

The accounting entries for the announcement message are:

- Dr Cover Suspense Account
- Cr Customer or Creditor Account

[Announcement Message not yet Received](#)

If the payment message is not received, the cover payment is moved to Cover Payment Unmatched (120) queue. Once the payment message is received into the system, both the messages are automatically matched and released from manual queue for further processing. Once all the validations are successfully performed, the payments are moved to completed status (999).

The accounting entries for the cover message once it is matched with an announcement message are:

- Dr Nostro
- Cr Cover Suspense Account

The accounting entries for the announcement message are:

- Dr Cover Suspense Account
- Cr Customer or Creditor Account

[](#)[Manual Queues for Cover Processing of both Customer Transfer and Bank Transfer Cover](#)

Announcement message that is yet to be matched with the cover payment is parked in Hold for cover queue (130) status. The cover payment which is received before the announcement message or which is not automatically matched with payment messages is parked in the cover payments unmatched queue (120) status.

The matching criteria for automatic matching of these two messages are as below :

- Instruction Identification tag of announcement – End to End identification tag of cover message.
- Transaction Currency of announcement – currency of cover.
- Interbank Settlement date of announcement and cover.
- Reimbursement agent of the announcement – Sender or Instructing agent of the cover.

The above details are customizable in ER module. The AC.Expected.Recs (ACER) record gets created for these two messages as Ec (Expected Cover) and Rc (Received Cover) in the ER module.

The user can manually match these two ACER records. Once manually matched, the payment message held in Hold for cover queue (130) and the cover message held in cover payment unmatched queue (120) are released for further processing and moved to completed status on successful validation and processing.

Accounting entries of announcement and cover message while manually matched is same as that for automatic matching.

[Hold for Cover Queue](#)

Incoming payments that are yet to be matched with the cover payments are parked in 'Pending payments for cover queue' (Status – 130). This enquiry is accessible through

**User Menu** > **Payments** > **Payment Hub** > **Payment Inquiries** > **Pending and Processed Payments** > **Pending Payments for Cover**.

The possible user actions from this enquiry are as below :

| Icon | Name | Description |
| --- | --- | --- |
|  | Release | Force releases the payment message from manual queue. Once force released, the payment is released for further processing and moved to complete if there are no further errors. The accounting entries given below are raised for the transaction once completed.  - Dr   Nostro of Reimbursement agent - Cr   Customer or Creditor account   The corresponding ACER record is deleted. |
|  | Cancel | Moves the payment to the cancelled status (997). The corresponding ACER record is also reversed. |
|  | Reject | Allows user to take an action by entering the reason code. Once committed and authorized, Pacs.002 RJCT gets created and sent to the Instructing agent of the announcement message if the bank is MX enabled. Once reject is sent, the corresponding ACER record gets reversed. |
|  | View | Gives a high level view of the transaction. |
|  | View in Detail | Gives the detailed view of the transaction. |

[Cover Payments Unmatched Queue](#)

Cover payment can be received before a payment message is parked in 'Cover Payment Unmatched' (Status -120) queue for manual action. This enquiry is accessible through:

**User Menu** > **Payments** > **Payment Hub** > **Payment Inquiries** > **Pending and Processed Payments** > **Cover Payments Unmatched**.

The possible user actions from this enquiry are as below :

| Icon | Name | Description |
| --- | --- | --- |
|  | Cancel | Moves the payment to cancelled status (997). The corresponding ACER record is also reversed. |
|  | Reject or Return | Allows user to Reject or Return by entering the reason code.   - If the payment is already settled by the instructing   agent (settlement method is INGA), then the user can return the transaction. The Pacs.004 return message gets created   and sent to the Instructing agent of the cover message. - If the payment is yet to be settled by the   instructed agent (Settlement method is INDA), then the user can reject the   transaction. The Pacs.002 RJCT message gets created and sent to the instructing   agent of the cover message.   For both reject and return action, the corresponding ACER entry in ER module gets reversed. |
|  | View | Gives a high level view of the transaction. |
|  | View in Detail | Gives the detailed view of the transaction. |

[](#)[Cover Processing for Customer Transfer](#)

An announcement message which is yet to be matched with the cover payment is parked in the “Hold for Cover Queue” (status – 130). The cover payment which is received before the announcement message or which is not automatically matched with the payment messages, is parked in the “Cover Payments Unmatched Queue” (status - 120) status.

These two messages are automatically matched based on the following matching criteria,

- Instruction Identification tag of announcement – End to end identification tag of cover message
- Transaction Currency of announcement – Currency of cover
- Interbank Settlement date of announcement and cover
- Reimbursement agent of the announcement – Sender or instructing agent of the cover

User can customize the above details in ER module, where AC.Expected.Recs (ACER) record gets created for these two messages as Ec (Expected Cover) and Rc (Received Cover).

User can manually match these two ACER records. Once manually matched, the payment message held in the “Hold for Cover Queue” (status - 130) and the cover message held in the “Cover Payment Unmatched Queue” (status - 120), are released for further processing and moved to completed status on successful validation and processing.

Accounting entries of announcement and cover message are same for manually and automatic matching.

[Hold for Cover Queue](#)

Incoming payments that are yet to be matched with the cover payments are parked in the “Pending Payments for Cover Queue” (status – 130). To access this enquiry, navigate to

**User Menu** > **Payments** > **Payment Hub** > **Payment Inquiries** > **Pending and Processed Payments** > **Pending Payments for Cover**

Following are the possible user actions from this enquiry:

| Icon | Name | Description |
| --- | --- | --- |
|  | Release | Force releases the payment message from manual queue. Once force released, the payment is released for further processing and moved to complete if there are no further errors. The accounting entries given below are raised for the transaction once completed.  - Dr   Nostro of Reimbursement agent - Cr   Customer or Creditor account   The corresponding ACER record is deleted. |
|  | Cancel | Moves the payment to the cancelled status (997). The corresponding ACER record is also reversed. |
|  | Reject | Allows user to take an action by entering the reason code. Once committed and authorized, Pacs.002 RJCT gets created and sent to the Instructing agent of the announcement message if the bank is MX enabled. Once reject is sent, the corresponding ACER record gets reversed. |
|  | View | Gives a high level view of the transaction. |
|  | View in Detail | Gives the detailed view of the transaction. |

[Cover Payments Unmatched Queue](#)

Cover payments received before a payment message are parked in the “Cover Payment Unmatched Queue” (status -120) for manual action. To access this enquiry, navigate to

**User Menu** > **Payments** > **Payment Hub** > **Payment Inquiries** > **Pending and Processed Payments** > **Cover Payments Unmatched**

Following are the possible user actions from this enquiry:

| Icon | Name | Description |
| --- | --- | --- |
|  | Cancel | Moves the payment to cancelled status (997). The corresponding ACER record is also reversed. |
|  | Reject or Return | Allows user to Reject or Return by entering the reason code.   - If the payment is already settled by the instructing   agent (settlement method is INGA), then the user can return the transaction. The Pacs.004 return message gets created   and sent to the Instructing agent of the cover message. - While manually initiating a return for the unmatched cover payments, user can select and capture the return originator details using the *Return Originated By* field. Allowed values are,    - Customer – Customer or beneficiary of the original transaction is the originator for the return transaction.   - Bank – Processing company is originator for the return transaction.   - Blank (default value) – Maps the company BIC in the outgoing message. - If the payment is yet to be settled by the   instructed agent (Settlement method is INDA), then the user can reject the   transaction. The Pacs.002 RJCT message gets created and sent to the instructing   agent of the cover message.   For both reject and return action, the corresponding ACER entry in ER module gets reversed. |
|  | View | Gives a high level view of the transaction. |
|  | View in Detail | Gives the detailed view of the transaction. |

## Routing SWIFT International Payments

The system provides multiple options to route outgoing and redirected cross border payments using contract definition. The system allows to configure the following types of contracts:

| Contract | Description |
| --- | --- |
| Party Contract | The party contract is checked for the credit party in the payment. In a party contract, the bank specifies on how the payment should be routed and settled with the credit party. |
| Country Contract | The country contract is checked for the destination country of the payment. In a country contract, the bank specifies on how it wants to route and settle payments to be sent to a specific country. |
| Bank Level Contract | The default bank level contract is applied if a corresponding country and party contract is not found. |

While processing an outgoing or redirected payment, if a relevant contract is not found then it is a set up issue and the payment is routed to repair. The system provides the following options using which banks can define the contract. If routing cannot be determined, then the system checks if Alternative for Routing and Settlement failure is configured otherwise the payment is moved to repair.

[LORO or NOSTRO Relationship](#)

The system has the ability to route an outgoing SWIFT payment to the credit party by using their LORO or NOSTRO accounts. The system provides an option to store these LORO or NOSTO accounts within the payment engine. If there are more than one LORO accounts for a particular BIC or if there are more than one NOSTRO accounts for a particular BIC, then a default LORO or NOSTRO account is used.

For routing ChequePresentmentNotification (camt.107) message, drawer bank must maintain a Nostro account with drawee bank.

[Support of Configuration of Message Interface](#)

If the Temenos Payments Hub bank acts as a clearing participant for Cross Border Payments and Reporting Plus (CBPR+) or direct participant for any other ISO based Real Time Gross Settlement (RTGS) clearing (like TARGET2 (TGT2), Clearing House Automated Payments System (CHAPS), Swiss Interbank *Clearing (*SIC) and so on), Temenos Payments Hub has the ability to forward the message in CBPR+ format to the creditor agent or Indirect participant. For such payments, the correspondent bank (with the output channel as LORO or Nostro) is the routing channel or agreement configured in the Temenos Payments Hub.

The correspondent banks of the Temenos Payments Hub processing bank can receive CBPR+ format messages on different network or interface (for example, SWIFT interact, Managed File Transfer (MFT)). Temenos Payment enables to configure  the network to route CBPR+ messages in the system if the network is not SWIFT interact (for example, MFT)

[Country Correspondent](#)

The system has the ability to store a Preferred Correspondent per country (also known as country correspondent). The bank can define more than one country correspondent per country. The user can configure the routing rules to send a payment using the preferred correspondent.

[Currency Correspondent](#)

The system has the ability to store a Currency Correspondent per country. The bank can define more than one currency correspondent per country. The user can configure the routing rules to send a payment using the currency correspondent. Read [SSI Upload](../../../PPSSIU/International_PaymentsCBPR/PPSSIU/Introduction.htm#) for more information.

[Relationship between Head Office and Branch](#)

The system has the ability to store a relationship between the head office and branch (on BIC code level) within the payment engine. The user can configure the routing rules such that a payment can refer to these relationships and route a payment.

[Account for Settlement](#)

The system has the ability to define an account through which the settlement can be carried out. This account can be different from the LORO or NOSTRO account of the credit bank.

Read the [Routing and Settlement](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Routing_and_Settlement/Introduction.htm) user for more information on booking related features and configurations.

## Acknowledgements for ISO20022 Messages

SWIFT InterAct is a messaging service used to send or receive ISO20022 format XML messages. When the system processes a payment, generated ISO20022 format messages are sent through the Temenos Transact delivery module. The system can receive one or more acknowledgements against these outward message. Within system these acknowledgements are categorised as technical and business acknowledgement.

The following diagram shows various acknowledgements corresponding to a customer payment sent as pacs.008 through SWIFT.

/Introduction_10.png)

| Message Type | Description |
| --- | --- |
| pacs.008 | Outward customer payment message is generated in the system and sent to SWIFT through SWIFT Alliance using InterAct service (using xmlV2 envelop). It could be other messages also such as Bank Transfer (pacs.009 Core and Cover), return Payment (pacs.004) and so on. |
| Network ACK | This is an acknowledgement sent by SWIFT indicating if the message has been accepted or rejected (similar to the F21 technical acknowledgement response for SWIFT FIN against MT messages). |
| pacs.008 | If the pacs.008 is accepted by SWIFT, then it forwards the message to the receiver, which could be as follows:  SWIFT gateway in another bank (for correspondent banking scenario)  Clearing (for SWIFT based RTGS clearing scenario) or Clearing Gateway (ESMIG for TARGET2) |
| DLN | The receiver gateway can send a positive delivery notification (if requested or configured to send) on receipt of the incoming message. |
| DLN | SWIFT forwards the positive delivery notification to the sender of the underlying message (pacs.008). Based on positive DLN, the sender understands that the receiver has received the outgoing message.  If SWIFT is unable to deliver the message to the receiver, it sends a negative delivery notification indicating delivery failure. |
| pacs.002 | Once the receiver processes the payment, the system may send an optional pacs.002 payment status report indicating that the payment is settled or rejected. Sending pacs.002 is optional and depends on various conditions for correspondent banking and clearing scenarios. |
| Network ACK | This is a technical acknowledgement sent by SWIFT indicating if the pacs.002 message has been accepted or rejected (similar to the F21 technical acknowledgement response for SWIFT FIN against MT messages) |
| pacs.002 | If pacs.002 is accepted by SWIFT, then it forwards the pacs.002 to the receiver (sender of the underlying payment message). Based on the pacs.002 bank understand the status of settlement and takes appropriate action in case of rejection. |
| DLN | On successful receipt of the pacs.002, the SWIFT gateway in the bank sends back delivery notification (if requested/configured to send) |
| DLN | SWIFT forwards the positive delivery notification to the sender of the underlying message (pacs.002). Based on positive DLN, the sender understands that the outgoing message has been received by the receiver.  If SWIFT is unable to deliver the message to receiver, it sends a negative delivery notification indicating delivery failure. |

These Network ACK and DLN are considered as SWIFT technical acknowledgements and the Payment Status Report (pacs.002) is considered as business acknowledgement in the system.

## Technical Acknowledgement Processing

SWIFT CBPR+ messages processed in the system are sent using the Delivery module. The Delivery layer updates the business application header, technical header and sends the message through SWIFT Interact Service. A specific carrier (CBPRPLUS) is defined in the Delivery module for SWIFT CBPR+ messages.

The delivery module supports sending MX messages through SWIFT Alliance standard interface using XMLv2 DataPDU format. The following technical acknowledgements from SWIFT should also be received in the XMLv2 DataPDU format –

- Transmission report for Network Ack/Nack
- SWIFT Alliance standard delivery report format for delivery notifications
  - xsys.010 for overdue warning
  - xsys.011 for positive delivery notification (when message is delivered)
  - xsys.012 for failed delivery notification (when message is not delivered)

The Delivery module also provides an option to send the outward messages through an intermediate interface layer (for example, ESBs, other SWIFT gateways, and so on), instead of the Delivery module sending the outward messages to SWIFT. In such cases, the intermediate interface layer sends the messages to SWIFT alliance and sends back technical acknowledgements.

[Outward](#)

The Delivery module provides the configurations at carrier level to define the technical acknowledgements applicable. Therefore the bank users can configure if Network Acknowledgement is applicable and if delivery notification is applicable. Failed delivery notification is not configurable, as SWIFT always sends this if network could not deliver the message (maximum timeline is 14 days).

When an outward payment is processed, Temenos Payments Hub checks against the delivery configuration to identify which technical acknowledgements are expected against the outward message and the status of the outward message is updated accordingly. This functionality is applicable only for single messages (not for bulk). The status change is applicable only for payment messages (pacs.008, pacs.009, and pacs.004) and non-payment message (camt.107).

The following table shows the status change based on technical acknowledgement configured in the Delivery module for the carrier (applicable for payment messages).

| Payment Status When Message is Emitted | Network Ack Req | DLN Req | Status |
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
| No | No | Cover sent and status =  Complete (999). |

Read the Delivery Framework user guide for details on features and configurations.

For the cover message sent through a non-SWIFT clearing (not through the Delivery module), Temenos Payments Hub checks against the clearing configuration to identify whether the acknowledgements are expected against the outward message.

If the configuration is enabled at the clearing level (ACKReqforRTGS is set as YES), then the system parks the message in intermediate status for the confirmation from clearing.

Once the clearing sends the positive confirmation, the system parks the message status to completed (999). On receiving the negative confirmation from clearing, the system parks the message in RTGS ISO technical exception enquiry from which user is allowed to take the manual actions.

If the configuration is not enabled (*ACKReqforRTGS* is set to NO or blank), the message directly moves to completed status (If *DLN* is already received for announcement or *DLNRequired* is set as No). If DLN is not received for the announcement message, then system waits at 'Waiting for DLN status' until the DLN is received from SWIFT network for the announcement.

[Inward](#)

The Delivery module receives the technical acknowledgements against outward messages. The Delivery module uses a proprietary technical acknowledgement XML response format to send the details of these acknowledgements to Temenos Payments Hub for further processing through a configured queue (the acknowledgement messages are not forwarded). The following are some of the important information sent in the proprietary acknowledgement response message:

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

On receipt of the technical acknowledgment details in the proprietary XML format, the system identifies the underlying outward message (from the PSM.BLOB table), for which this technical acknowledgement is received, using the Original Bulk Reference. The received acknowledgement response is saved in PSM.BLOB.

- The *AckNackMsgType* field is updated with Response Class
- The *AcknowledgementCode* field is updated with Response Type
- The *AckNackReason* field is updated with Error Codes
- The *AcknowledgementMessage* field is updated with the received proprietary XML response
- The *AcknowledgementAction* field is updated as PNDG (for negative ack) for non-payment messages

Based on the message type, the system identifies if the acknowledgement is for a payment message (such as pacs.008, pacs.009, pacs.004, pacs.009ADV) or a non-payment message (such as camt.056, camt.029, camt.107 and so on).

The system updates the audit trail in the related payment for which the acknowledgment is received (positive or negative).

When negative technical acknowledgment is received, the system does not perform any automatic action. The user can view all such outgoing messages using the **SWIFT ISO Technical Exception** enquiry. This enquiry displays:

- Payment messages (such as pacs.008, pacs.009, pacs.009 cover, pacs.009 ADV, pacs.004) and non-payment message (camt.107)
  - payments / cover that are waiting for acknowledgement
  - payment / cover for which NACK has been received
  - payments / cover message waiting for DLN
  - payments / cover for which negative DLN has been received
- Non-payment messages (such as pacs.002, camt.057, camt.056, and camt.029) for which NACK has been received

The enquiry output displays records with the following columns:

- Company
- FTNumber
- Amount
- Currency
- MessageType
- Date (Date on which message was sent)
- Status Code (Status of original transaction - applicable only for payment messages)
- Status Code Description (Status code description of original transaction - applicable only for payment messages)
- Cover flag (Indicates if payment is sent through cover method which is applicable only for pacs.008 payment message)
- Cover Sent (Indicates if cover is sent already which is applicable only for payment message pacs.008)

The enquiry provides the following options against each record displayed in the output screen:

| Option | Description |
| --- | --- |
|  | Allows to display the underlying message in read-only mode. |
|  | Allows to display the audit trail of the underlying message. |
|  | Allows to display the following attributes of the technical acknowledgement message:   - Company - FTNumber - Sender’s Reference - SendDateTime - Message Type - Message Content (outward formatted xml message) - AcknowledgementCode (0 for ACK/1 for NACK/ 2 for WARNING) - AckNackReason (Reason code received in NACK/Negative DLN response) - AckNackDescription - AcknowledgementMessage (xml Format Ack/Nack message as received from DE) |
|  | Allows to perform manual action on the underlying message. It opens a new screen with available actions. |

The user can perform one of the following actions against a record in the enquiry:

| Option | Description |
| --- | --- |
| Cancel | When the user performs this action, accounting entries are reversed and the status of outward payment is updated as Reversed (993). Audit trail is updated.  The posting entries are directly reversed (separate reversal transaction is not created). Hence credit notification from Temenos Payments Hub is not generated for the customer.  In case the underlying is a return payment (pacs.004), once the return transaction is reversed, the related original transaction (can be traced using POR.Supplementary.Info > OriginalOrReturnId) is moved back to its original status (Completed).  If the outgoing pacs.008 sent to SWIFT, is a part of pain.001 bulk payment file with the *Batch Booking Indicator* as TRUE, and after successful reversal of accounting entries, a new RJ transaction is created for the outgoing transaction amount to debit the Batch Suspense account and to credit the Debtor of the bulk payment as the money should be returned to the debtor who initiated the bulk payment. The user can also view the remittance information of the original transaction in the reversal message, to identify which payment has been reversed. If Temenos Payments Hub debits the debtor of the bulk payment for any processing charges, the charged amount is not credited back to the debtor as the Temenos Payments Hub processed the payment.  If the outgoing payment is a part of the pain.001 bulk file with *Batch Booking Indicator* field as TRUE, and settled through the cover method, where the cover is sent to the correspondent bank through SWIFT, Temenos Payments Hub releases the cover message to the SWIFT network once a positive ACK is received for the announcement message (pacs.008) from the SWIFT network.   - On receiving the ACK for the announcement and releasing the cover, it is possible to receive a negative DLN for the announcement message. In that case, the user cannot initiate a cancellation request for an already released cover message, since the status of the transaction is updated as NACKED. In such cases, the instructing bank has to wait for the return payment for the cover from the correspondent bank. The received return message gets routed to the repair queue with the ‘Original transaction is not fully processed’ warning message. The user should accept this warning and enter the credit account number as the Original Debtor account of the batch parent transaction and submit it from the repair queue. On successful submission and authorization of the return transaction, the status of the return is updated as Completed and the status of the original transaction is updated as ‘Completed with Return’. - On receiving the ACK for the announcement message and once the cover is released to the network, it is possible to receive NAK or negative DLN for the cover message from the network. On receiving NAK or DLN for the cover message, the status of the message is updated as NACKED and the message gets routed to the SWIFT ISO Technical Exception enquiry. For such payments, the user cannot initiate a cancellation request for an announcement message to the instructed agent since the payment status is changed to NACKED. In such cases, the instructing bank can wait for pacs.002 RJCT for the announcement message from the creditor agent through SWIFT. When a functional reject (pacs.002) is received from the creditor agent for the announcement message, the acknowledgment message is always parked in the SWIFT ISO Business Exception enquiry for user action. In this scenario, the user cannot perform the reverse action for the pacs.002 RJCT message as the status of the payment is not complete. The system throws an ‘Underlying payment for the pacs.002 was settled via a cover and it is not in completed status, so the Reverse option is not applicable’ error. Temenos Payments Hub user can then reverse the payment from the SWIFT ISO Technical Exception enquiry for the NAK message for the cover and the status of the transaction gets updated as Reversed. Once the original payment is marked as reversed, the payment is not displayed in the SWIFT ISO Exception queue. A new RJ transaction is created for the outgoing transaction amount to debit the Batch Suspense account and to credit the Debtor of the bulk payment as the money should be returned to the debtor who initiated the bulk payment. The user can also view the remittance information of the original transaction in the reversal message to identify which payment has been reversed.   If the debtor of the bulk payment was debited for any processing charges by the Temenos Payments Hub, the charged amount is not credited back to the debtor as the TPH bank processed the payment.   - For redirected payments (pacs.008, pacs.009, and pacs.004), when the system receives a NACK and the user selects the ‘Cancel’ action from the SWIFT ISO Technical Exception queue, the system triggers the following overrides:   1. ‘The payment will be cancelled, and all posting entries, including charges, will be reversed. Do you wish to continue?’   2. ‘The return message should be manually sent to the original sender’. Upon accepting these overrides, the user must manually initiate the return transaction to the sending bank using ‘Outgoing ISO Bank Transfer Return’ or ‘Outgoing ISO Customer Transfer Return’ screen. |
| Complete | When user performs this action, payment status is updated as Complete (999). Accounting entries are not reversed (actions taken outside Temenos Payments Hub/Temenos Transact –directly on SWIFT alliance). Audit trail is updated.  - Complete action can be performed for following scenarios. - When the payment is sent out again from external interface - Bank user creates a new payment using the OE screen by entering same details from the original transaction, imposing the ordering customer details, imposing same debit and credit accounts (to nullify accounting entries). - Once complete action is performed for the camt.107 message, Current State in Payment Order moves to ‘AwaitingPrinting’, that is, the system is ready for printing the draft. |
| ProcessAsAckReceived | This action is applicable when the underlying payment is in one of the following status:   - Payment Sent and waiting for ACK/NACK (Status Code 677) - Cover sent and waiting for ACK/NACK (688) - NACK received for cover (691) - NACK received for payment (680)   This action moves the payment to the next status assuming that the system has received ACK and continues processing. Audit trail is updated. |
| ProcessAsDLNReceived | This action is applicable when the underlying payment is in one of the following status:   - Payment sent and waiting for DLN - Cover sent and waiting for DLN - Negative DLN received for payment/underlying message - In case of cover, Negative DLN received for cover   This action moves the payment to the next status assuming that the system has received positive DLN and continues processing. Audit trail is updated. |
| Ignore | This action updates the value of the *Acknowledgment Action* as Ignore (in the PSM.BLOB table), so that this record is not showed in this exception enquiry again. Audit trail is updated. For non-payment messages except camt.107, the ‘Ignore’ action is applicable. Other actions are applicable for payment messages and for camt.107. |
| Accept | This action updates the value of the *Acknowledgment Action* field as Accept (in PSM.BLOB), so that this record is not shown in this exception enquiry again. Refer to the [Processing of Non-Payment Messages based on Technical Acknowledgements](#ProcessNonPayment) section for more details. |

[Confirmations and Pre-Advice Generation](#)

- The system generates confirmations such as SMS or Email and Debit or Credit notification (camt.054) once the payment is successfully processed and reaches complete status (999). This means that positive network acknowledgement and positive delivery notification are received (if configured)
- Notice to receive (camt.057) is generated when network acknowledgement is received and need not wait for DLN even though bank is configured to receive positive DLN. Currency Correspondent

[Accepting and Ignoring Technical Response for pacs.004 Message](#)

For pacs.004 return message, if Temenos Payments Hub receives a negative DLN or ACK from SWIFT network, instead of resending the same message again to the network, the user can decide to accept the response. If the user selects the Accept option from the Technical Exception queue, then the status of return transaction is updated as Reversed and also the posting gets reversed.

When the original transaction was in any of the interim status and the return transaction is triggered, and once the return is reversed, the system should also reverse the accounting of the original transaction and park the original payment in repair status so that user can take action on the payment.

When the original transaction is in the Completed status and the return transaction is triggered, and once the return is reversed, the system updates the status of the original transaction to Completed.

If the outgoing pacs.004 was initiated in response to an incoming camt.056, then the system updates the status of the corresponding EBQA record as INWORK and value of the *Process Indicator* field as MANUAL. The system also updates the error reason as ‘Return rejected by the network’ in the EBQA table. So, the cancellation request is available for the user to take manual action from the **Inward Cancellation req – Require Manual action** enquiry. Refer to the [Processing Payment Cancellation](../../../PPSWCR/International_PaymentsCBPR/PPSWCR/Introduction.htm#Payment_Cancellation_Processing) section.

If the user does not want to take any action in Temenos Payments Hub, then the user can select Ignore option from the Technical Exception queue.

[](#)[Resubmission of Payment Messages based on Technical Acknowledgements](#)

When an outward SWIFT CBPR+ message is sent, it may receive negative technical acknowledgements from SWIFT, based on the delivery configurations. Payments awaiting technical acknowledgements and those that have received negative technical acknowledgement are displayed using the **SWIFT ISO Technical Exception** enquiry. Under certain circumstances such as, DLN is not received, the users can decide to resend the payment again.

For payment messages, the user can perform actions using the **User Menu** > **Payments** > **Payment Hub** > **Payment Exceptions** > **SWIFT ISO Exception Queue** > **SWIFT ISO Technical Exception** enquiry.

From the **SWIFT ISO Technical Exception** enquiry, the user can select a payment and use the resubmit option to resend it. Any action taken by the user for the payment messages must be authorised by another user from the **User Menu** > **Payments** > **Payment Hub** > **Authorise SWIFTOut Exceptions** > **Authorise SWIFTOUT Exceptions** enquiry. Resubmission of payment (Customer Transfer - pacs.008, Bank Transfer - pacs.009 and pacs.009COV, pacs.009 pre-advice, Return - pacs.004 and ChequePresentmentNotification-camt.107) is allowed when it is in one of the following statuses.

- Payment Sent and waiting for Ack (677)
- Payment Sent and waiting for DLN (673)
- Cover Sent and waiting for Ack (688)
- Cover Sent and waiting for DLN (683)
- Nack or Negative DLN received for payment (680)
- Nack or Negative DLN received for Cover (691)

On invoking the resubmit option, the system opens the delivery (DE) version from where the user can actually resubmit the message. The Delivery (DE) module resends the message with same Technical Header, Business Application Header (BAH), and underlying payment payload. In case the underlying payment(which is being resent) is in Awaiting Ack or Awaiting DLN status, a possible duplicate indicator is added in the BAH.

When the message is resent successfully, the following updates are also performed on the underlying payment:

- The payment status is updated (refer to the table below).
- If some acknowledgements were received already (Ack/DLN responses) for the direct payment or cover, then those are deleted.
- Audit trail is updated as: “<MessageType> is resubmitted by <CurrentUserName> at <CurrentDateTime>”

| Payment Status Before Resubmit | Payment Status After Resubmit | Other Updates |
| --- | --- | --- |
| Payment sent and waiting for ACK (677) | Payment sent and waiting for ACK (677) | Any responses received for the payment (direct message) is deleted from Response status list |
| Cover sent and waiting for ACK (688) | Cover sent and waiting for ACK (688) | Any responses received for the cover is deleted from Response status list |
| Payment sent and waiting for DLN | Payment sent and waiting for ACK (677) | Any responses received for the payment (direct message) is deleted from Response status list |
| Cover sent and waiting for DLN | Cover sent and waiting for ACK (688) | Any responses received for the cover is deleted from Response status list |
| NACK received for Payment (680) | Payment sent and waiting for ACK (677) | Any responses received for the payment (direct message) is deleted from Response status list |
| NACK received for Cover (691) | Cover sent and waiting for ACK (688) | Any responses received for the cover is deleted from Response status list |

When the response is received for the underlying payment, the system checks if a cover is sent already. If yes, the system proceeds to send a cover again.

- A cover is sent again only when the cover sent earlier receives any negative response.
- If the resubmit functionality does not work, set the TAFJ property as 'temn.tafj.xml.enable.cdata.replacement=false'.

The above check is done to ensure that the cover is not sent twice because of underlying payment resubmission in scenarios like:

- Cover already has positive responses received (both ACK/DLN)
- Cover has received no responses yet

[](#)[Processing of Non-payment Messages based on Technical Acknowledgements](#)

When the outward CBPR+ payment status report (pacs.002) or Notice to Receive (camt.057) message or Resolution of Investigation message (camt.029) or Customer Status Report (pain.002) is sent through SWIFT, it is possible to receive negative technical acknowledgements against such non-payment messages. In case of negative technical acknowledgements, these non-payment messages are displayed in the **SWIFT ISO Technical Exception** enquiry for the user to understand that these have been negatively acknowledged. From the exception enquiry, the system provide options to Ignore, Accept, or Resubmit based on the message types (payment or non-payment).

For non-payment messages, the user can perform actions from the **User Menu** > **Payments** > **Payment Hub** > **Payment Exceptions** > **SWIFT ISO Exception Queue** > **SWIFT ISO Technical Exception** enquiry.

Any action taken by the user for the non-payment messages must be authorized by another user from the **User Menu** > **Payments** > **Payment Hub** > **Payments Approvals** > **Authorize SWIFTISO Exceptions** > **Authorize SWIFTISO Exceptions** enquiry.

When the user performs the Ignore action, no action is taken on the message in Temenos Payments Hub and the user has to take any further action separately outside the system.

- In case a negative acknowledgment is received against the outward payment status report (pacs.002), the system does not perform any accounting entry, but the operational users need to handle required postings manually. The following are the applicable user actions for pacs.002 message:

| Action | Description |
| --- | --- |
| Ignore | The system does not perform any status change for the transaction. |
| Resubmit | For pacs.002 message that are waiting Ack/DLN or have received Nack/Negative DLN, the same message gets resubmitted to the SWIFT network. |

- In case a negative acknowledgement is received against the outward Notice to Receive message (camt.057), the possible user actions from the **SWIFT ISO Technical Exception** enquiry is Ignore. Temenos Payments Hub bank does not provide resubmit option for camt.057 that are waiting Ack/DLN or have received Nack/Negative DLN, this resubmission must be done from the delivery (DE) module directly.
- In case a negative acknowledgement is received against outward customer status report (pain.002), the system provides the following options in the **SWIFT ISO Technical Exception** enquiry for the user to take action. The possible user actions are as follows.

| Action | Description |
| --- | --- |
| Ignore | This option only ensures that pain.002 record does not show in **SWIFT ISO Technical Exception** enquiry anymore. The system updates the audit trail as Nack ignored from Technical Exception Queue by <User\_Id> on <DateTime>. |
| Resubmit | The system sends the pain.002 message again from the Delivery Module layer. |

[](#)[Action on Payments Failing XSD Validation in Temenos Payments Hub Transformation Layer](#)

When an outward SWIFT CBPR+ payment is captured and processed, the XML-format message is generated finally and sent through the DE module. The message generation happens after all processing is done (such as channel determination, validations, posting and so on). When the message is generated, it is also validated against the respective schema (XSD). Under exceptional scenarios such as when the XSD validation fails, this message cannot be sent out.

Therefore, if the payment message (pacs.008, pacs.009, pacs.009cov, pacs.009 pre-advice, and pacs.004) and non-Payment message (camt.107) fail the payload validation in the Camel Transformation Layer, the system updates the payment status as Payment Failed XSD Validation and displays such payments in the **SWIFT ISO Technical Exception** enquiry. The users can take one of the following actions on these payments:

| Action | Description |
| --- | --- |
| Complete | Updates payment status to Completed (999). Any further action need to be done manually outside the system  Once complete action is performed for the camt.107 message, Current State in Payment Order moves to 'AwaitingPrinting', that is, the system is ready for printing the draft. |
| Cancel | Reverses the accounting entries and the payment status is moved to Cancel |

The message is still passed to Delivery Camel, but the disposition (status) of the outward messages in the DE module is marked as Repair.

[](#)[Action on Non – Payments Failing XSD Validation in Temenos Payments Hub Transformation Layer](#)

If non-payment messages like the customer status report (pain.002) fails the payload validation in the Camel Transformation Layer, the system updates the audit trail as Payment Failed XSD Validation and displays such payments in the **SWIFT ISO Technical Exception** enquiry. The users can perform one of the following actions on these payments:

| Action | Description |
| --- | --- |
| Ignore | No action is taken in Temenos Payments Hub. Any further action needs to be done manually outside the system |
| Resubmit | The system displays that the resubmit option is not allowed |

The file status gets updated as Failed along with the error description.

The message with XSD error is still passed to Delivery Camel, but the disposition (status) of the outward messages in DE module is marked as Repair.

## Payment Status Report (Business Acknowledgement) Processing

For SWIFT cross border payments between financial institutions, the instructed agent sends the Payment Status Report message (CBPR+ pacs.002) to the previous agent in the payment chain.

/Introduction_15.png)

Payment status report is used to inform the previous agent about:

- Positive status – When the received instruction has been processed successfully by the instructed agent. Positive status is optional and depends on agreement between banks.
- Pending status – When the payment is in intermediate status and neither completed nor rejected. Pending status is optional and depends on agreement between banks.
- Negative status – When the received instruction has been rejected by the instructed agent. Negative status for rejection is mandatory and does not require any agreement.

CBPR+ has restricted usage of pacs.002 to a single transaction (one message contains status of a single transaction).

It is possible to receive more than one payment status report against across border payment (for example – first report is generated for pending status and second for positive or negative status).

The system supports processing of both incoming and outgoing payment status report (pacs.002).

[Inward pacs.002 Processing](#)

When an outgoing or redirected payment is sent through SWIFT, the user can receive inward payment status report (pacs.002) from the instructed agent (receiver) in the following cross border payment scenarios.

The processing bank is configured to send cross border SWIFT payments in MX format.

- Outgoing customer transfer captured and sent through SWIFT in CBPR+ MX format (pacs.008 or pacs.008 STP), where the debit customer has an account in the processing bank
- Outgoing bank transfer captured and sent through SWIFT in CBPR+ MX format (pacs.009 or pacs.009COV or pacs.009 pre-advice), where the debit account is in the books of the processing bank
- Inward customer transfer redirected to SWIFT in CBPR+ MX format (pacs.008 or pacs.008 STP) for a payment received from another bank (correspondent banking) or from RTGS clearing
- Inward bank transfer redirected to SWIFT in CBPR+ MX format (pacs.009 or pacs.009COV or pacs.009 pre-advice) for a payment received from other bank (correspondent banking) or from RTGS clearing
- Outgoing return payment sent through SWIFT in MX format (pacs.004)
- Inward return payment redirected through SWIFT in MX format (pacs.004)

The processing bank is configured to send cross border SWIFT payments in MT format.

- Outgoing customer transfer captured and sent through SWIFT in MT format (MT103 or MT103+), where the debit customer has an account in the processing bank
- Outgoing bank transfer captured and sent through SWIFT in CBPR+ MX format (MT202 or MT202 COV), where the debit account is in the books of the processing bank
- Inward customer transfer redirected to SWIFT in MT format (MT103 or MT103+) for a payment received from another bank (correspondent banking) or from RTGS clearing
- Inward bank transfer redirected to SWIFT in MT format (MT202 or MT202 COV) for a payment received from other bank (correspondent banking) or from RTGS clearing.

The incoming pacs.002 could be a positive/interim status report or a rejection. The system identifies the underlying payment (for which pacs.002 is received) using the value received in Original Instruction ID (which is the FTNumber of the underlying outgoing or redirected payment). However, if original instruction ID is not received in the incoming pacs.002 (as this is an optional field), the system identifies the underlying transaction based on the original message identification received in pacs.002,which is the message ID of the underlying outgoing or redirected payment.

If the pacs.002 is a positive or interim status, then the audit trail of the underlying payment is updated. No status change is done for the underlying payment.

If the pacs.002 is for a rejection (reject code = RJCT) against an outgoing or redirected payment, then the system can be configured to process the negative pacs.002 either manually or in STP mode. The reject reason code received in pacs.002 is checked (the *RoutetoException* field in the PP.CLEARING.RETURNCODE application, for SWIFTMX ID and clearing transaction type RJ) to decide if manual or STP processing is configured.

[Manual Processing of pacs.002 Rejection](#)

When manual processing is configured for the reject reason code, the system does not perform any automatic action on the received pacs.002 rejection. The user can view the underlying outgoing and redirected cross border payments for which rejection has been received (through pacs.002) and awaiting manual action using the **SWIFT ISO Business Exception** enquiry.

To access this enquiry, go to **User Menu** > **Payments** > **Payment Hub** > **Payment Exceptions** > **SWIFT ISO Exception Queue** > **SWIFT ISO Business Exception**.

Any action taken by the user from the SWIFT ISO Business Exception enquiry must be authorised by another user from the **User Menu** > **Payments** > **Payment Hub** > **Payments Approvals** > **Authorise SWIFT ISO Exceptions** > **Authorise SWIFT ISO Exceptions** enquiry.

The enquiry provides the following options against each record displayed in the output screen:

| Option | Description |
| --- | --- |
| View | Allows to display the underlying payment in read-only mode. |
| View History Log | Allows to display the audit trail of the underlying payment. |
| View PSR | Allows to display the payment status report message. |
| Action | Click on this option to perform a manual action on the underlying payment. It opens a new screen with available actions.  The user can perform one of the following actions against a record in the enquiry. Once user completes the action, the payment no longer appears in this enquiry again.   - Ignore – The user can choose to ignore the error, the status of the payment is not changed and no accounting entries are performed. The underlying message is not displayed again in the enquiry.  - Reverse – The user can select the payment and choose reverse action.   If the underlying payment direction is outgoing, then the system reverses the accounting entries and update the status of the original transaction as 998 (Completed - Payment reversed (rejected). A new reversal transaction is created to post the reversal entries.  If the underlying payment direction is redirected, then the system creates a new return payment (pacs.004) and sends to the sender of the underling redirected payment.  If the processing bank is configured to send cross border payments in MT format, then reverse action is not allowed for redirected underling payment. If the user clicks on reverse option, an error message ‘Reverse action cannot be initiated as Temenos Payments Hub does not support return of MT messages’ is displayed. |

After performing the user action from the business exception enquiry, the transactions are sent for authorisation. On authorization, the reversal or ignore action takes effect.

The system does not support resubmission or resending of the underlying payment from the Exception enquiry when payment status report - rejection is received against an outgoing or redirected payment.

[STP Processing of pacs.002 Rejection](#)

When STP processing is configured for the reject reason code, the system automatically reverses the accounting entries by creating a new reversal transaction (as mentioned above for Manual Reversal action) if the underlying payment direction is outgoing. In this scenario, the underlying payment is not displayed in the **SWIFT ISO Business Exception** enquiry.

If the underlying payment direction is redirected and processing bank is configured to send cross border payments in MX format, then the system automatically generates a return payment (pacs.004) and routes to the sender of the underlying redirected payment.

If the underlying payment direction is redirected and processing bank is configured to send cross border payments in MT format, then the system does not create a return payment (pacs.004) automatically. Instead the rejection message is displayed in the **SWIFT ISO Exception** enquiry and reversal is not allowed. If the user clicks on reverse option, an error message, ‘Reverse action cannot be initiated as Temenos Payments Hub does not support return of MT messages’ is displayed.

[Receiving pacs.002 Reject against Outgoing Payment Settled Serially](#)

/Introduction_16.png)

In this scenario, the system captures an outgoing payment (Customer / Bank Transfer / Bank Transfer Cover) in Temenos Payments Hub bank and sends it to correspondent bank through SWIFT. The outgoing payment is in MX format or MT format based on how the processing company is configured for cross border payments.

When a reject (pacs.002 with reason code RJCT) is received for the outgoing payment, the system creates a new reversal transaction which is processed as a book transfer. The transaction amount in the reversal transaction is same as the amount which was sent in the underlying outgoing payment, irrespective of the charge option (SHAR/CRED/DEBT) in the underlying payment.

The following accounting entries are posted:

| Accounting Entry | Description |
| --- | --- |
| Debit | Loro/Nostro account of the instructed agent (that was credited while sending the outgoing payment) |
| Credit | Customer or Loro/Nostro account (that was debited while sending the outgoing payment) |

The status of the underlying payment is moved to 998 (Completed - Payment reversed (rejected).

The reversal process mentioned above is not applicable if the pacs.002 reject is received for an underlying payment (customer transfer) settled using cover method (system generated a cover). Since the underlying message (which was sent directly to creditor agent) does not carry the money, there is no need to create a reversal transaction for it. The bank should get back the money through the reimbursement agents through whom the cover was sent. In such scenario, only the audit trail of the underlying payment is updated to indicate it was rejected by the instructed agent without any accounting entries.

[Receiving pacs.002 Reject against a Redirected Payment from Correspondent Bank Settled Serially](#)

/Introduction_17.png)

In this scenario, the original payment is received from a correspondent bank through SWIFT and the Temenos Payments Hub bank redirected it through SWIFT to a correspondent bank. The correspondent bank rejects the payment and sends pacs.002. The redirected payment could be in MX format or MT format based on how the processing company has been configured for cross border payments.

If the bank is configured to send cross border SWIFT payments in MX format, and when pacs.002 reject is received against a redirected payment, the system generates a new outgoing return payment (based on STP processing or manual action) and routes the return to the correspondent bank through SWIFT that sent the original message.  The system sends the return payment using CBPR+ pacs.004 message. This applies for redirected customer transfer and bank transfer (including cover). The charge option is always set as SHAR in return payment (irrespective of the charge option used in the underlying payment). Temenos Payments Hub bank can deduct the charges from the transaction amount of the return payment for processing the return payment if redirect return charges are configured with the instructed agent of the return payment (receiver of the return payment).

After the return is sent, the status of the original transaction is moved to Complete with Return (996).

The following accounting entries are posted:

| Accounting Entry | Description |
| --- | --- |
| Debit | Loro/Nostro account of the instructed agent (that was credited while sending the redirected payment) |
| Credit | Loro/Nostro account of the receiver of the return payment (to which the return is sent) |
| Credit | Profit and Loss (P&L) account for charges |

If the processing bank is configured to send cross border SWIFT payments in MT format, and when pacs.002 reject is received against a redirected payment, the system performs the following functions:

- Updates the audit trail of the underlying transaction indicating rejection received
- Does not generate return payment automatically
- The received pacs.002 message is parked and the user can view using the **SWIFT ISO Business Exception** enquiry (Read the [Working with SWIFT MX](Workingwith.htm)  for more information).

Reverse action is not allowed for such scenarios.

The user should manually create a new transaction (in MT103 or MT202 format as required for return with appropriate code words in tag 72) and send it to the correspondent bank from whom underlying payment was received.

This flow is same when the Temenos Payments Hub bank receives pacs.002s2 RJCT from Clearing (such as STEP2), original payment from a correspondent bank through SWIFT, and redirects it through Clearing (such as STEP2). For manual intervention, the user can go to the Clearing Status Report Exception screen using the navigation below:

**User Menu** > **Payments** > **Payment Hub** > **Payment Exceptions** > **Clearing Status Report**.

The system posts the following accounting entries:

- Settlement Transaction: Debit – Clearing Nostro | Credit – Clearing Suspense
- Individual Transaction: Debit – Clearing Suspense | Credit – Loro/Nostro of receiver of return payment

[Receiving pacs.002 Reject against Redirected Payment from Clearing](#)

/Introduction_18.png)

In this scenario, the system receives the original payment from a RTGS clearing (for example, TARGET2) and Temenos Payments Hub bank redirects it through SWIFT to a correspondent bank. The correspondent bank rejects the payment and sends CBPR+ pacs.002.

If the processing bank is configured to send cross border SWIFT payments in MX format, and when pacs.002 reject is received against a redirected payment, the system generates a new outgoing return payment (based on STP processing or manual action) and routes the return to the clearing that sent the original message. The return should be sent in the format accepted by the clearing (for example, pacs.004 for TARGET2), which is handled as part of individual clearing solution. If return is not supported for the clearing, the new return payment moves to repair. This applies for redirected customer transfer and bank transfer (including cover).

After the system sends the return to the clearing, the status of the original transaction is moved to Complete with Return (996).

The following accounting entries are posted:

| Accounting Entry | Description |
| --- | --- |
| Debit | Loro/Nostro account of the instructed agent (that was credited while sending the redirected payment) |
| Credit | Clearing Nostro/Loro account (to which the return is sent) |
| Credit | Profit and Loss (P&L) account for charges |

[Receiving pacs.002 Reject against Outgoing Payment Settled through Cover Method](#)

/Introduction_19.png)

In this scenario, the system captures an outgoing cross border payment in Temenos Payments Hub bank and sends it to correspondent bank using cover method through SWIFT. Two messages are generated – one is sent directly to the creditor agent (direct message) and second is the cover message, which is sent through the reimbursement agents. The outgoing payments could be in MX format or MT format based on how the processing company is configured for cross border payments.

If the negative status report is received for the outgoing direct message, then pacs.002 message is processed as non-STP by default. This pacs.002 is displayed in the **SWIFT ISO Business Exception** enquiry, from where the user can perform either Reverse or Ignore action.

- If the Reverse action is performed, the system checks the status of the original transaction
  - If the status of the original transaction is in completed status, the system displays an override, ‘Pacs.002 received for underlying transaction which was settled through Cover, Are you sure you want to reverse’.
    - On accepting the override, a new Reverse transaction is created by debiting instructed agent account (which was credited as part of original transaction) and crediting the Customer/Loro/Nostro account (which was debited as part of original transaction)
    - Audit trail of the original transaction is updated
    - The status of the original transaction is updated as reversed (993).
    - If the customer has agreed for any customer status report (pain.002) then Temenos Payments Hub sends the status report to the customer informing them about the reject.
    - If the status of the original transaction is not in completed status, the system displays a functional error, ‘Underlying payment for the pacs.002 was settled via a cover and it is not in completed status, so the Reverse option is not applicable’ on the screen,. In this case the only possible action for the user is to ignore.
- If the Ignore action is performed, status of the underlying transaction remains unchanged. Audit trail is updated with pacs.002 message transaction status and timestamp. pacs.002 message is not displayed in the enquiry after ignore action.

| Customer Transfer Settled Using Cover | Bank Transfer Settled Using Pre-advice |
| --- | --- |
| The direct or announcement message is pacs.008 and a cover message is pacs.009 COV | The direct or announcement message is pacs.009 ADV and the cover message is pacs.009 |

[Receiving pacs.002 Reject against Redirected Message Settled through Cover Method](#)

/Introduction_20.png)

In this scenario, the system as an intermediary receives an incoming serial transfer and then redirects to correspondent bank using cover method through SWIFT. So as an intermediary, two messages are generated to redirect the received payment – one is sent directly to the creditor agent (direct message) and second is the cover message which is sent through the reimbursement agents.

If negative status report is received for the redirected direct message settled through cover, then pacs.002 message is processed as non STP by default. This Pacs.002 is displayed in the **SWIFT ISO Business Exception** enquiry, from where user can perform either Reverse or Ignore action.

- If the Reverse action is performed, the system displays a functional error, ‘Underlying redirected payment for the pacs.002 was settled via a cover, so return not applicable (Wait for the cover return)’ on the screen. Audit trail of the payment is updated to indicate underlying payment (not cover) is rejected by the instructed agent. In this case the only possible action for the user is to ignore.

Since the underlying message does not carry the money, return transaction is not created. The receiving bank returns the money using the different route that was used by the cover payment

- If the Ignore action is performed, status of the underlying transaction remains unchanged. Audit trail is updated with pacs.002 message transaction status and timestamp. The message is not displayed in the enquiry any more.

If negative status report is received for the cover message which is generated by Temenos Payments Hub for the redirected transfer settled through cover method, then pacs.002 message is processed as non STP by default. This pacs.002 is displayed in the **SWIFT ISO Business Exception** enquiry – from where user can take Reverse or Ignore action.

- If the Reverse action is performed, a new return transaction pacs.004 is created and sent out to the correspondent bank or to the clearing (Sender of the original message) if the bank is configured to send cross border payments in MX mode. If the bank is in MT mode, the system displays an error message, ‘Reverse action cannot be initiated as Temenos Payments Hub does not support return of MT messages’.
- If the Ignore action is performed, audit trail is updated without changing the status of the original transaction. The message is not displayed in the enquiry any more.

| Customer Transfer Settled Using Cover | Bank Transfer Settled Using Pre-advice |
| --- | --- |
| The direct or announcement message is pacs.008 and a cover message is pacs.009 COV | The direct or announcement message is pacs.009 ADV and the cover message is pacs.009 |

[Receiving pacs.002 Reject Against Redirected Payment Received through Cover Method](#)

/Introduction_21.png)

In this scenario, the system as an intermediary receives direct customer transfer or bank transfer payment message from debtor agent which is using cover through reimbursement agents. After the cover is received, the intermediary bank redirects the customer transfer to creditor agent bank.

If negative status report is received for the redirected payment, then pacs.002 message is processed as non-STP by default. This pacs.002 is displayed in the **SWIFT ISO Business Exception** enquiry – from where user can take Reverse or ignore action.

- If Reverse action is performed, system displays a functional error, ‘Underlying redirected payment for the pacs.002 was received via a cover, so return not applicable’ on the screen. Audit trail of the payment is updated to indicate underlying payment is rejected by the instructed agent. The only possible action for the user is to ignore.
- If Ignore action is performed, status of the underlying transaction remains unchanged. Audit trail is updated with pacs.002 message transaction status and timestamp. The message is not displayed in the enquiry any more.

The user has to manually create a new return transaction and send it to the Instructing agent of the cover message. This return transaction can be manually initiated from the enquiry if pacs.009 COV message is received from correspondent or user can use the ISO bank transfer return OE to initiate a pacs.004.

| Customer Transfer Settled Using Cover | Bank Transfer Settled Using Pre-advice |
| --- | --- |
| The direct or announcement message is pacs.008 and a cover message is pacs.009 COV | The direct or announcement message is pacs.009 ADV and the cover message is pacs.009 |

[Viewing Received Incoming pacs.002 for the Transaction](#)

The Pending and Processed enquiry enables the user to view the outgoing transaction and its corresponding received incoming pacs.002 message for the outward transaction.

[Outward pacs.002 Generation](#)

When the system receives an inward cross border payment through SWIFT, outward payment status report (pacs.002) can be generated and sent to the instructing agent (sender) of the inward payment for the following scenarios.

The processing bank is configured to send cross border SWIFT payments in MX format.

- Incoming customer transfer received through SWIFT in CBPR+ MX format (pacs.008 or pacs.008 STP) or MT format (MT103 or MT103+), where the credit customer has an account in the processing bank
- Incoming bank transfer received through SWIFT in CBPR+ MX format (pacs.009 or pacs.009COV or pacs.009 ADV) or MT format (MT202 or MT202 COV), where the credit account is in the books of the processing bank
- Inward customer transfer redirected to SWIFT in CBPR+ MX format (pacs.008 or pacs.008 STP) for a payment received from another bank (correspondent banking)
- Inward bank transfer redirected to SWIFT in CBPR+ MX format (pacs.009 or pacs.009COV or pacs.009 ADV) for a payment received from other bank (correspondent banking)
- Incoming return payment received through SWIFT in MX format (pacs.004)
- Inward return payment redirected through SWIFT in MX format (pacs.004)

The processing bank is configured to send cross border SWIFT payments in MT format.

If the processing bank is configured to send cross border payments in MT format, then the system does not generate payment status report for incoming or redirected messages.

To send payment status report for payments received through SWIFT, the user need to maintain the Relationship Management Application (RMA) for pacs.002 (with the bank to whom it is sent). If RMA is not available, then the system does not generate outward payment status report even if other conditions are met, and adds an audit trail indicating the same.

The system supports sending the following status codes in pacs.002 message.

| Code | Name | Definition |
| --- | --- | --- |
| ACCC | AcceptedSettlementCompleted | Settlement on the creditor's account is completed. |
| ACSP | AcceptedSettlementInProcess | All preceding checks such as technical validation and customer profile are successful and therefore the payment initiation is accepted for execution. |
| ACSC | AcceptedSettlementCompleted | Settlement is completed. |
| PDNG | Pending | Payment initiation or individual transaction included in the payment initiation is pending. Further checks and status update are performed. |
| RJCT | Rejected | Payment initiation or individual transaction included in the payment initiation is rejected. |

The system does not support other status codes (such as RCVD, ACCP, ACTC, ACWC, ACSC, ACWP) while sending a pacs.002 to the instructing agent.

[Sending Positive Payment Status Report](#)

Sending positive payment status report is optional. Hence, the system provides configuration in bank conditions, which can be configured to decide if it needs to be sent to the instructing agent / sender of the inward payment. The user can maintain this for individual correspondent bank or at a default bank condition level.

This configuration is for a correspondent bank and is not for any specific message type. Therefore if configured, the system sends pacs.002 irrespective of the underlying payment (which is customer transfer, bank transfer, return).

The system can send positive payment status report for the following scenarios (if bank condition is configured for Sender and RMA is maintained):

- Incoming payment is successfully processed and beneficiary account is credited (incoming on us payment). Status code ACCC () is sent in the pacs.002 message.
- Inward payment successfully processed and redirected through SWIFT or through a local clearing. In case of redirected payment, the reason code is decided as mentioned below:
  - If the payment is redirected through a clearing (Output Channel is clearing), then the ACSP status code is sent in the pacs.002 message
  - If the payment is redirected through SWIFT (Output Channel is LORO or NOSTRO or ACCOUNT)
    - If credit account is of type LORO/VOSTRO (that is, if the processing bank services the account of the receiving bank), ACSC status code is sent in the pacs.002 message
    - If credit account is of type NOSTRO (that is, if the processing bank’s account is serviced by the receiving bank), ACSP status code is sent in the pacs.002 message

[Sending Pending Payment Status Report](#)

Sending pending (interim) payment status report is optional. Hence, the system provides configuration in bank conditions that can be configured to decide if it needs to be sent to the instructing agent or sender of the inward payment. The user can maintain this for individual correspondent bank or at a default bank condition level.

This configuration is for a correspondent bank and is not for any specific message type. Therefore if configured, the system sends pacs.002 irrespective of the underlying payment (which could be customer transfer, bank transfer, return).

The system can send pending payment status report with PNDG status code if,

- The bank condition is configured for Sender to send interim status report
- RMA is maintained to send pacs.002
- Payment is still under processing and not moved to completed status (999).

The following are functional scenarios in the system when interim payment status report with PNDG status code can be sent.

| Functional scenario | Temenos Payments Hub Business States |
| --- | --- |
| Payment is held up due to fraud or other regulatory requirements. | Payment waiting for response from Sanction screening system (status code 602)  Payment waiting in Manual HIT/Seize Filter queue in Temenos Payments Hub for manual intervention (status code : 215) |
| Payment is held up as awaiting for funds from the cover institution | Payment waiting for cover  (status code : 130) |
| Payment has been held up for any other reason | Payment routed to repair (status code :235)  Payment  routed to warehouse queue (status code 19 ) because the payment is received after cut off and it is configured as ALAP (As late as possible)  Payment sent to Treasury for FX rate request (status code : 645)  Payment routes to Risk filter queue ( 621)  If the DDA or general ledger is external, payment cannot be processed completely as the system is waiting for response from external system  (account validation and so on) |

While the system processes the payment, the payment can move through multiple intermediate statuses before reaching completion state. The system ensures only one interim status report to be generated and sent. It is not generated every time the payment moves from one interim status to another interim status.

[Sending Payment Rejection](#)

The system supports rejecting an inward cross border payment.

If the inward payment is not yet settled (that is, instructed agent is responsible for settlement) and the payment is rejected, then the system generates pacs.002 rejection with RJCT status code. The reason for rejection is also populated in the message.

The system can send pacs.002 rejection if the processing bank is configured to send cross border payments in MX format and RMA is maintained. If the processing bank is configured to send cross border payments in MT format, then the system does not send pacs.002 rejection.

In case the payment is already settled, then the system does not allow rejection. In this scenario, the payment must be returned using a pacs.004 message.

## Customer Payment Status Report Processing

Interbank customer payment status report message is sent by the debtor agent to the previous agent in the payment chain (Forwarding agent or Initiating Party). It provides notification of the status (positive, negative or pending) of the payment initiation message. Refer to the below image for details.

For CBPR+, Temenos Payments Hub currently supports pain.002.001.10 version, /Picture1.png)

As per CBPR+ rules, providing a rejected status is mandatory whereas the provision of a positive and interim status is governed by a bilateral agreement between the agents. There are two scenarios as shown below,

- The pain.002 message is sent by the initiating party (the debtor agent) to the forwarding agent which acts as a concentrating financial institution. It forwards the pain.002 message to the initiating party (relay scenario).
- The pain.002 message is sent by the debtor agent to the financial institution initiating liquidity sweeps on behalf of a corporate customer who may receive the sweep status separately.

Temenos Payments Hub does not support relay of pain.002 as Temenos Payments Hub bank acts as a forwarding agent for a pain.001 which is not supported in the system.

Customer payment status report is used to inform the previous agent about the following statuses as described below.

- Positive – When the received instruction processes successfully by the instructed agent. This status is optional and depends on agreement between banks.
- Pending – When the payment is in intermediate status and neither completed nor rejected. This status is optional and depends on agreement between banks.
- Negative – When the received instruction is rejected by the instructed agent. This status for rejection is mandatory and does not require any agreement.

CBPR+ has restricted usage of pain.002 to a single transaction (one message contains status of a single transaction).

It is possible to send more than one customer payment status report against cross border payment.

First report generates for pending status and second for positive or negative status.

When the system determines to send a customer status report (pain.002), it checks if the payment is initiated through SWIFT channel and if processing bank is configured to send cross border SWIFT payments in MX format. If so, pain.002 in CBPR+ format is sent through SWIFT through delivery module. If sending the cross border SWIFT payments in MX format is not configured in the processing bank, then CBPR+ pain.002 is not sent to the sending bank.

- Temenos Payments Hub does not perform any Relationship Management Application (RMA) check while sending a pain.002.
- Incoming Payment Instruction from SWIFT can be in MX format (pain.001).
- pain.002 is not generated for MT format (101).

System validates the outward pain.002 against corresponding XML Schema Definition (XSD) applicable for the channel (SWIFT) through which the message is sent. If XSD validation fails, the message must not be sent out and displayed in SWIFT ISO Technical Exception queue. Refer to [Action on Non – Payments failing XSD validation](#) in Temenos Payments Hub Transformation Layer section to know more details.

Bank can receive acknowledgment and delivery notification from SWIFT network when the pain.002 is sent through SWIFT network. Refer to [Technical Acknowledgment Processing and Processing of Non-Payment Messages](#) based on Technical Acknowledgment section for more details.

[CBPR+ pain.002 Message Structure](#)

The pain.002 message is composed of four building blocks as follows,

- Group Header - Contains a set of characteristics shared by all individual transactions in the message.
- Original Group Information and Status – Captures the message identifier and message name of the underlying payment that the payment status report relates to.
- Original Payment Information and Status – Contains information about the original payment information which refers to the status report message.
- Transaction Information and Status – Provides information on the original transactions which refers to the status report message. It is used to inform the previous party in the payment chain about the positive or negative status of an instruction. Additionally, it is used to report about a pending instruction.

/Picture2.png)

[Bilateral Agreement for Customer Status Report](#)

Despite the rejected status being mandatory for CBPR+pain.002, system sends it only if an agreement is defined in the system for reject status (file and transaction level). So, any status (negative, positive or interim) depends upon the bilateral agreement between the agents.

Bilateral agreement for customer status report can be defined at the following levels in the system.

- Netting Agreement: Used for file and transaction level acknowledgment. User can define agreement for a particular sending agent. There are separate indicators for file and transaction level acknowledgments.
- Message Acceptance: Used for the file level acknowledgment. User can define the agreement for payment initiation message received from all agents through SWIFT.
- Source Setting: Used for the transaction level acknowledgment. User can define the agreement for payment initiation message received from all agents through SWIFT.

Precedence is given to netting agreement. If the related customer status report indicator is not defined in the netting agreement, then system refers to the indicators defined in message acceptance (file acknowledgment) or source setting (transaction acknowledgment) to determine if a pain.002 must be generated.

The table below describes the recommended configurations for the generation of customer status table.

| Scenario | Originating Source | CSR On Settlement | CustomerStatusReportRejects | CustomerStatusReportReturns | InterimStatusind | Status code in PP.STATUS.CODE for CSR | Status code |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Payment is processed successfully and pain.002 must be sent immediately on completion | SWIFT/SWIFTMX | ACKImmediate | NA | NA | NA | NA | ACSP/ACCC |
| Payment is processed successfully and pain.002 and pain.002 must be sent on credit value date | SWIFT/SWIFTMX | ACK | NA | NA | NA | NA | ACSP/ACCC |
| Payment in Interim Status | SWIFT/SWIFTMX | NA | NA | NA | Immediate | 19,235,215,49,602,645,642,600 | PDNG |
| Payment is cancelled in system (status code -997) | SWIFT/SWIFTMX | NA | Immediate | NA | NA | NA | RJCT |
| Payment is rejected (998) based on pacs.002 from clearing or correspondent bank | SWIFT/SWIFTMX | NA | Immediate | NA | NA | NA | RJCT |
| Payment is returned (System should not send pain.002) | SWIFT/SWIFTMX | NA | NA | Blank | NA | NA | NA |
| Payment is reversed (993) (System should not send pain.002) | SWIFT/SWIFTMX | NA | NA | Blank | NA | NA | NA |

Refer to [Status Reporting](../../../../Payments/PP/Payments_Hub_(PP)/Status_Reporting/Introduction.htm#) for more details on the various customer status report indicators available in the system to support pain.002.

[Message Elements Supported in CBPR+ pain.002](#)

The basic message elements supported in CBPR+ pain.002 are provided below.

[Initiating Party](#)

The initiating party in the context of interbank payment initiation report is always the debtor agent which initiates the pain.002 message. Bank Identifier Code (BIC) is mandatory to identify the initiating party in the pain.002 message. There are two use cases as described below.

- The debtor agent sends the pain.002 message to the forwarding agent which acts as a concentrating financial institution. It forwards the pain.002 message to the original initiating party who can be the debtor themselves or the authorized party. This is commonly known as a relay scenario.

Temenos Payments Hub does not support functionality of relay pain.002 as forwarding agent.

- The debtor agent sends the pain.002 to the financial institution which initiated multi-bank liquidity sweeps on behalf of a corporate customer.

Temenos Payments Hub maps processing bank BIC as initiation party in pain.002.

[Forwarding Agent](#)

The forwarding agent acts as a concentrating financial institution and forwards the pain.002 message to the debtor or the initiating party. It is mandatory in a relay scenario where the receiver of the pain.002 message is not the original debtor. In such cases, the initiating party (the debtor agent) provides the Bank Identifier Code (BIC) of the forwarding agent in the pain.002 message.

- Other options include Legal Entity Identifier (LEI) or clearing system member ID.
- Temenos Payments Hub maps the forwarding agent in pain.002 as received in pain.001 message.

[Original Message Identification](#)

The original message identification contains the point-to-point reference of the underlying payment that is reported. Temenos Payments Hub maps this information as message identification as received in pain.001. It is a mandatory message element.

[Original Message Name Identification](#)

The original message name identification contains the message name of the underlying payment that is reported. Temenos Payments Hub maps this information as pain.001 message format (pain.001.001.09). It is a mandatory message element.

[Original Creation Date Time](#)

The original creation date time contains creation date time of the underlying payment that is reported and Temenos Payments Hub maps this information as creation date time as received in pain.001. It is an optional information.

[Original Payment Information Identification](#)

This 35-character identifier is a point-to-point reference used to unambiguously identify the payment information group or batch reference, if the message contains multiple transactions. Temenos Payments Hub maps this information with the original message identification as the interbank pain.001 and pain.002 usage guidelines are restricted to one single transaction.

[Original Instruction Identification](#)

This original element enables the initiating party to associate the payment status with the payment they originally sent. Temenos Payments Hub maps this information as Instruction Identification as received in pain.001. It is an optional element.

[Original End to End Identification](#)

This original element enables the initiating party to associate the payment status with the payment they originally sent. Temenos Payments Hub maps this information as End to End Identification as received in pain.001. It is a mandatory element.

[Original UETR](#)

This original element enables the initiating party to associate the payment status with the payment they originally sent. Temenos Payments Hub maps this information as UETR as received in pain.001. It is a mandatory element.

[Transaction Status](#)

The element specifies the status of a transaction in a coded form.

[File Level Acknowledgment](#)

The CBPR+ statuses applicable at file acceptance level are as below.

| Status code | Status Code Description | ISO Definition | Temenos Payments Hub Adherence | Comments |
| --- | --- | --- | --- | --- |
| RCVD | Received | Payment initiation has been received by the receiving agent. | Not Supported | Defines the status code which Temenos Payments Hub does not support as the payment initiation file does not parse and converts to neutral format at this stage (on receipt). Hence, payment instruction details do not retrieve from the file which is sent in the pain.002. |
| ACTC | AcceptedTechnicalValidation | Authentication and syntactical and semantical validation are successful | Supported | It indicates that the file validation is successful but the transaction inside the bulk does not map successfully because of missing configuration in the system. The status of the bulk is marked as Repair. User can resubmit the file from the Received File Details - Repair queue after fixing the missing configurations. |
| ACCP | AcceptedCustomerProfile | Preceding check of technical validation was successful. Customer profile check was also successful. | Supported | It specifies that the file is successfully accepted and the individual transaction (single for CBPR+) inside the bulk maps successfully to a payment transaction in the system. |
| RJCT | Reject | File has been rejected | Supported | It specifies the file fails technical validations and that it is not accepted |

pain.002 cannot be sent for XSD validation failure because of technical constraints.

[Transaction Processing Acknowledgment](#)

The CBPR+ statuses applicable at transaction level as are below.

Sending Interim Status - Temenos Payments Hub supports sending interim status in customer payment status report to indicate the progress of the payment.

The CBPR+ interim statuses are as below.

| Code | Status Code Description | ISO Definition | Temenos Payments Hub Adherence | Comments |
| --- | --- | --- | --- | --- |
| ACFC | AcceptedFundsChecked | Preceding check of technical validation and customer profile was successful, and an automatic funds check was positive. | Supported | It indicates that the interim status is sent when the balance check (with and without charges) performs successfully by the system.  Status code 642 must configure in status code table |
| ACWC | AcceptedWithChange | Instruction is accepted but a change will be made, such as date or remittance not sent. | Supported | It indicates that the system sends this status code if the payment routes to repair queue. System cannot track if changes are actually made or not in the payment instruction.  Status code 600 must configure in status code table |
| ACIS | AcceptedandChequeIssued | Payment instruction to issue a cheque has been accepted, and the cheque has been issued but not yet been deposited or cleared. | Not Supported | It defines that it is not a valid case for payments as Temenos Payments Hub does not support issuing of cheque |
| CPUC | CashPickedUpByCreditor | Cash has been picked up by the Creditor. | Not Supported | It specifies that it is sent by creditor agent and does not support in the system |
| ACWP | AcceptedWithoutPosting | Payment instruction included in the credit transfer is accepted without being posted to the creditor customer’s account. | Not Supported | It specifies that it is sent by creditor agent and does not support in the system |
| PDNG | Pending | Payment initiation or individual transaction included in the payment  initiation is pending. Further checks and status update will be  performed. | Supported | It indicates that the interim status code is sent for the status codes that configures in the system. As a result, interim status configured for the following statuses are as follows,   |  |  | | --- | --- | | 19 | Payment waiting in warehouse queue | | 215 | Screening requires manual intervention | | 235 | Payment moved to General repair queue | | 49 | Waiting for Balance Check DDA approval | | 602 | Payment waiting for response from screening system | | 645 | Waiting in Rate Request Queue |   Any status code other than the above must configure by the local implementation team in the system. |

Sending Final Status - Temenos Payments Hub supports sending final payment status in customer payment status report.

The CBPR+ final statuses are as below.

| Code | Name | ISO Definition | TPH Adherence | Comments |
| --- | --- | --- | --- | --- |
| ACSP | AcceptedSettlementInProcess | All preceding checks such as technical validation and customer profile were successful and therefore the payment initiation has been accepted for execution. | Not Supported | Temenos Payments Hub does not support. |
| ACSC | AcceptedSettlementCompleted | Settlement has been completed. | Supported | This status code is sent when the payment is sent to the clearing or correspondent bank and is completed in the system  - To generate  the pain.002 immediately after the payment is sent out successfully ‘AckImmediate’ option must define the  for ‘CSR on settlement  field For payments that is sent to correspondent bank, this status code is sent after the positive acknowledgment and delivery notification is received.  - To generate the pain.002 on credit value then ‘Ack’ option must be defined for ‘CSR on Settlement’  field . In certain cases, credit value date is different from the payment completion where cut off shift and settlement currency involves |
| RJCT | Rejected | Payment initiation or individual transaction included in the payment initiation has been rejected. | Supported | This final status code is sent in the following scenarios,  Cancelled (997) : When the payment is cancelled by the system automatically or by the bank user from repair screen (exceptions - payment cannot be processed ) or when the payment is cancelled in the system based on customer request (camt.055)  Rejected (998) : When the system receives a pacs.002 RJCT from clearing or correspondent bank (in this case, system creates new reversal transaction and mark the original transaction as 998 once the reversal transaction is processes successfully). |
| ACCC | AcceptedSettlementCompleted | Settlement on the creditor's account has been completed. | Supported | This final status code is sent by creditor agent For a book transaction (creditor has an account in the Temenos Payments Hub).  - To generate the pain.002 immediately after the payment is processed successfully then AckImmediate option must be defined for *CSR on Settlement* field.  - To generate  the pain.002 on credit value then Ack option must be defined for *CSR on Settlement* field . In certain cases, credit value date is different from the payment completion where cut off shift and settlement currency shift is involved. |

As per SWIFT, there is no need to send pain.002 when the debtor agent receives a return message (pacs.004) for an original outgoing customer transfer, as pacs.004 should re-credit the original debtor with a reversal indicator in the camt statement. There should be no further pain.002 notification as pain.002 does not have a return status. Bank must ensure not to configure in the netting agreement level or SWIFTMX source level (*CustomerStatusReportReturns* field) to send pain.002 when returns receives for the payment. The system does not send RJCT status when the payment reverses manually from the reversal screen or when the user clicks on reverse from the SWIFT ISO technical exception screen.

[Originator](#)

This indicates the party that issues the status. Ideally, this is the pain.002 initiating party and therefore originator is not necessary. Temenos Payments Hub maps originator BIC as processing bank BIC. All other optional elements such as name and address, Legal Entity Identifier (LEI), other identification does not map.

[Reason Code](#)

This utilizes ISO external status reason code. It must provide for RJCT (Reject) transaction status.

- CBPR+ User Handbook Manual (UHB) does not document a list of reject reason codes that is used in CBPR+pain.002. The rationale is that a pain.001 can instruct more than just CBPR+ payment meaning it includes domestic transaction outside of the SWIFT network.

- When the system receives a negative pacs.002 (RJCT status) from clearing, the reject reason code in clearing pacs.002 passes as the reject reason code in the CBPR+ pain.002. System does not check if the reason code is SWIFT MX complaint or not.

- When the outgoing payment cancels manually by the system, there is no provision for the user to select the cancel reason code. In such scenario, system follows framework used for non CBPR+ customer status report. System checks if there is any active error code and maps the ISO reason code defined for it. If the system is unable to retrieve the ISO reason code, default code of MS03 is used.

[Additional Information](#)

This indicates text element to provide further status reason information for reason codes like NARR.

Temenos Payments Hub does not map this information when the payment cancels or reverses manually. System allows to manually reverse the payment from Reversal of Payments enquiry or SWIFT/ISO Technical Exception enquiry. However, when the payment reverses because of pacs.002 RJCT from clearing or correspondent bank, Temenos Payments Hub maps this information as received in pacs.002 RJCT.

[Enquires to View the Customer Status Report](#)

The section describes the enquires used to view the customer status report,

- The user can view the CBPR+ pain.002 that is sent to corporates or financial institution as part of file level acknowledgment (positive or negative) using the below enquiry against the received payment initiation message. The user can view pain.002 message (in formatted xml) along with the details such as file name, creation date time and so on.

**Payments** > **Payments Hub** > **Payments Inquiries** > **Received and SentFile Details** > **Received Files Details** > **Received Message/File Details List**.

In the enquiry list under Received File Details tab, the user can choose the **View Sent CSR** option to view the file level customer status report details.

- The user can view the CBPR+ pain.002 as part of transaction level acknowledgment (interim, final positive or negative) using the below enquiry against the payment transaction.

**Payment Hub** > **Payment Enquiries** > **Pending and Processed Payments** > **View In Details option** /Picture3.png)**from the enquiry list** > **View Customer Payment Status Report Drill Down option**.

In case multiple pain.002 messages are sent for the transaction, user can view all pain.002 messages (in formatted xml) along with the details like reason code (in case of reject status), reason description (in case of reject status), acknowledgment and the DLN received from SWIFT network.

## Returning or Rejecting a Received International Payment

As per SWIFT CBPR+ rules, if the instructed bank is not able to process a received cross border payment (pacs.008 Customer Transfer, pacs.009 Bank Transfer – core and cover), then it must either reject the payment or return the payment and send a corresponding message to the instructing agent. For SWIFT CBPR+ cross border payments, Reject is sent as pacs.002 and Return is sent as pacs.004 message. If the payment is already settled, then the user must only return the payment (rejection not allowed for settled payments). Sending a rejection or return does not require any bilateral agreement.

The system provides option to reject or return a received payment manually. Automatic return is not supported for cross border payments.

Returns payments should not be settled using cover method.

The system can send pacs.002 rejection or pacs.004 return, if the processing bank is configured to send cross border payments in MX format and RMA is maintained. If the processing bank is configured to send cross border payments in MT format, then reject and return is not supported.

For SWIFT cross border payments, whether to reject or return the received payment, is decided based on which agent is doing the settlement – Instructing Agent or Instructed Agent. In correspondent banking, the bank holding the actual account (LORO/NOSTRO) is responsible for settlement.

[Reject or Return CBPR+ Payment based on Settlement Method](#)

Settlement Method is a mandatory element in a CBPR+ pacs.008 and pacs.009 message. This is populated by the instructing agent while sending the payment to the instructed agent. The system decides whether to reject or return an incoming payment based on the value in the Settlement Method tag in the message.

/Introduction_22.png)

[Settlement Method is INGA - Return](#)

This is the scenario where a cross border customer or bank transfer (core or cover) is sent serially through one or more intermediary agents. INGA means the instructing agent is responsible for the settlement. If settlement method is mentioned as INGA and the system is unable to process the pacs.008 or pacs.009 received from SWIFT, then only return is allowed as the payment is already settled by the instructing agent. Reject is not allowed.

The user can manually open the payment and return by providing the appropriate return reason code. Once the final authoriser approves the return action, the received payment is processed by crediting the funds to a return suspense account. The system derives the return suspense account based on the currency of the payment and configure suspense account category in company properties.

A new return payment transaction is created automatically and,

- the received party and agent roles are swapped and mapped into the return transaction
- charge option is set as shared (SHAR/SHA)
- the amount of the return transaction is calculated based on the charge option in the received payment being returned
  - If the charge option of the original payment, which is returned, is CRED (BEN) or SHAR (SHA), then the transaction amount of the return payment is same as the transaction amount of the received payment.
  - If the charge option of the original payment, which is returned, is DEBT (OUR) then the transaction amount of the return payment is transaction amount of the original transaction minus the receivers’ charges.

The processing bank can deduct return charges as part of the return interbank settlement amount for processing the return payment. Return charges are based on the bilateral agreement between the correspondent banks and can be configured accordingly in the system.

The following accounting entries are raised for the original received payment that is returned:

| Accounting Entry | Description |
| --- | --- |
| Debit | Nostro account of the Instructing Agent for transaction amount |
| Credit | Return Suspense Account for transaction amount minus receivers charges |
| Credit | Profit and Loss (P&L) account for receivers charges |

The following accounting entries are raised for the return payment:

| Accounting Entry | Description |
| --- | --- |
| Debit | Return Suspense account for return transaction amount |
| Credit | Nostro account of the Instructed agent of the return payment for return transaction amount minus return charges |
| Credit | Profit and Loss (P&L) account for return charges |

On processing the return transaction, the system generates the CBPR+ pacs.004 message and sends through SWIFT. The return reason code as entered by the user is sent in the generated pacs.004 message. After processing the return payment successfully, the system updates the status of the original received transaction as Completed with Return.

[Settlement Method is INDA - Reject](#)

This is the scenario where a cross border customer or bank transfer (core or cover) is sent serially through one or more intermediary agents. INDA means the instructed agent is responsible for the settlement. If settlement method is mentioned as INDA and the system is unable to process the pacs.008 or pacs.009 received from SWIFT, then only reject is allowed as the payment is not yet settled by the instructed agent. Return is not allowed.

The user can manually open the payment and reject the payment by providing reject reason code. When the payment is rejected, accounting entries are not posted. The system generates a CBPR+ pacs.002 message with RJCT status code and sends it through SWIFT to the instructing agent of the payment being rejected. The reject reason code as entered by user is sent in the generated pacs.002 message. After completing the reject successfully, the status of the original received transaction is updated as Rejected (998).

If an expected receipt record is already created for the payment being rejected, then the ER module is updated so that the record can be reversed.

[Settlement Method is COVE - Reject](#)

This is the scenario when the creditor agent receives the customer payment (pacs.008) or bank transfer payment (pacs.009 pre-advice) directly from debtor agent with information on the reimbursements agents through which funds are received. This payment message contains the settlement method as COVE. Debtor agent sends a separate cover (pacs.009 COV in case of customer transfer cover, pacs.009 in case of bank transfer cover) through the reimbursement agents to credit the funds in the account of creditor agent. The cover is settled between the reimbursements agents serially using INDA or INGA mechanism.

If settlement method is mentioned as COVE (means payment is being settled through a cover) and system is unable to process the pacs.008 or pacs.009 pre-advice received from SWIFT, then only reject is allowed as the payment is not yet settled by the instructed agent. Return is not allowed.

[Settlement Method is CLRG](#)

This is the scenario when the payment is sent through a clearing (such as, TARGET2) and the clearing is responsible for settlement. In this scenario, the return mechanism of the respective clearing is followed.

[Reject or Return MT Payment based on Debit Account Type](#)

Since there is a coexistence of SWIFT MT and MX format, it is always possible for a bank to receive customer or bank transfer in MT message. If the processing bank is configured to send cross border payments in MX format, then the system can send a reject or return against a cross border MT payment (MT103 or MT202 or MT202 COV) received from SWIFT. If the processing bank is configured to send cross border payment in MT format, then return or reject is not supported.

SWIFT MT 103/202 message does not have the *Settlement Method* field to explicitly mention which agent is responsible for settlement. Therefore, if the incoming message is MT, then decision on whether to reject or return the payment is taken based on the debit account which is determined while processing the inward MT payment.

- If the determined debit account is of type NOSTRO (that is, instructing agent has the actual VOSTRO account), then the system allows return only.
- If the determined debit account is of type VOSTRO (that is, instructed agent has the actual VOSTRO account), then the system allows reject only.
- If debit account is not determined (for example, debit account determination failure, incoming message is MT103 announcement which is being settled through a separate cover and so on), then the system allows reject only.

The user can open the payment from the repair queue and manually select the reject or return option. The remaining processing for reject or return is same as mentioned above for MX messages.

The system does not allow reject or return if the received MT103/MT202 message has RETN or REJT code word (which means these are incoming return/reject and therefore these cannot be returned/rejected).

[](#)[Manual Return or Reject Scenarios](#)

Manual reject or return of a received payment is supported for the following scenarios.

[Payment in Repair Status](#)

When the system receives a cross border SWIFT payment (in MT or MX format) from SWIFT, the system processes the payment in STP mode. If the system encounters any error during the processing, the payment is moved to repair status. Also system provides multiple configurations based on which a payment can be moved to repair (for example, Inbound code word rule to move payment to repair).

The user can open a payment parked in repair status using the **Pending Repair Payments** enquiry and manually reject or return the payment.

- To reject, select the Reject option and select appropriate rejection reason code.
- To return, select the Return option and select appropriate return reason code.

The system displays the reason codes as published in ISO External Code List ([External code sets | ISO20022](https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets)).

The system validates if the payment can be rejected or returned based on the settlement method or credit account type.

While manually initiating a return for a payment from the Repair screen, user can select and capture the return originator details using the *Return/Request Originated By* field. Allowed values are,

- Customer - Customer or beneficiary of the original transaction is the originator for the return transaction.
- Bank - Processing company is originator for the return transaction.
- Blank (default option) – System maps the company BIC in the outgoing message.

/Return1.png)

[HIT or Time out Response from Sanction Screening](#)

When the system sends a cross border payment received from SWIFT to the sanction screening system and if the response received is HIT or TIME OUT (no response received), the user can configure the following options as actions:

- Cancel or return
- Route to HIT Filter Queue

For the Cancel or Return option, the system automatically reject or return transactions that have received HIT responses based on the transaction's settlement type.

| Transaction's Settlement Method | System Action |
| --- | --- |
| INDA | The system automatically sends a pacs.002 message with the MS03 reason code (Reason not specified) to the original transaction's sender. |
| INGA | The system automatically sends the original transaction's sender a pacs.004 return message with the MS03 reason code (Reason not specified). The original transaction is credited to the Return Suspense account while transferring pacs.004, and the customer is not credited. |

The accounting entries are as follows:

- For Original Transaction: Dr Loro/Nostro | Cr Return Suspense Account
- For Return Transaction: Dr Return Suspense Account | Dr Loro/Nostro

For both the options, the system always routes the payment to HIT filter queue for manual action. The user can manually reject or return the payment from this queue.

[Payment in Manual Filter Queue](#)

When a payment is parked in manual filter queue, the user can select the following options:

- Seize – The transaction gets seized and the credit happens to the FCM suspense account instead of customer account.
- Continue – Transaction is released from manual queue and the processing continues.
- Cancel Return – Transaction gets opened in repair mode. The possible actions from this screen are Cancel, Reject or Return.

While initiating a return, user can select and capture the return originator details using the *Return Originated By* field. Allowed values are,

- Customer – Customer or beneficiary of the original transaction is the originator for the return transaction.
- Bank – Processing company is originator for the return transaction.
- Blank (default option) – System maps the company BIC in the outgoing message.

/Return2.png)
/Return3.png)

[Payment Waiting for Cover](#)

If a customer transfer or bank transfer pre-advice is received with reimbursement bank details to indicate that the payment is settled through a cover, the system can be configured to wait for the cover payment before crediting the customer or creditor. If hold for cover is configured in company properties, then the received customer payment is parked in the Hold for Cover queue. For bank transfer, irrespective of the configuration, the bank transfer pre-advice is always parked in hold for cover queue.

From the Hold for Cover queue, the user can manually reject the received payment by providing the reject reason code. Return is not allowed from this queue.

If the cover message or advice notification has not received and if the creditor agent wants to reject the payment, then the bank user can send pacs.002 message to the debtor bank.

If the system receives the cover message or advice notification and if the creditor agent wants to reject the payment, then the bank user need not send pacs.002 RJCT to the debtor bank.

[Cover Waiting for Match](#)

If the system receives a cover payment before the underlying customer transfer, then the cover payment is parked in cover payments unmatched queue when hold for cover feature is configured. The user can manually return or reject the cover payment from this queue by providing the reason code based on the settlement code of the transaction.

When the creditor agent returns the payment without crediting the customer or any intermediary agent returns the payment without crediting the next agent from any of the above queues, the system updates the marker in the original and return transaction that the payment is a return of an incomplete return (for STP or automatic and non-STP return). Based on this incomplete return indicator,

- Temenos Payments Hub bank is mapped as debtor (Return chain or Debtor agent ) and not the original creditor
- The original instructing agent is mapped as debtor agent in the return chain
- The original intermediary agent(s) present in the underlying payment are not mapped in the return chain (in case redirected)

The above mapping is different from pacs.004, which is returned after the customer is credited.

[Returning Processed Payment](#)

When the system receives an incoming CBPR+ payment (Customer or Bank Transfer), the payment is processed in STP and if there are no errors, the beneficiary is credited and received payment is moved to completed status. There might be scenarios where a processed payment needs to be returned.

To facilitate manual return of a processed incoming payment, go to **User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Return/Reject Payment** > **Return of SWIFT Completed Credit Txn**.

This enquiry displays all the SWIFT incoming payments (customer transfer, bank transfer, cover transfers) that are successfully processed and moved to completed status (amount is credited in the creditor’s account). The user can return a processed transaction by selecting a valid return reason code.

If the bank configured to process cross border payments is in MT format, then the system displays an error and manual return initiation is not allowed. This is allowed only if bank is configured for MX.

After submitting the transaction without any error and with valid return reason code, the return transaction is routed for authorisation. The user can authorise the return using the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Payment Approvals** > **Authorise Pmt Investigation and Cancellation** > **Return/Reject of SWIFT Transfers** > **Return of SWIFT completed credit txn**

After authorising and processing the return transaction successfully, pacs.004 return message is generated and sent to original sender of the incoming transaction. The status of the original transaction is updated as Complete with Return.

If the user tries to return a direct customer payment (which was received directly from debtor agent and settled through cover), then the system displays an error message on the screen to indicate that it is received through cover method and cannot be returned. The user should initiate a return for the cover using the enquiry.

If the user returns a cover that is processed successfully, the status of the incoming cover payment is updated as Completed with return. In addition, the status of the customer payment that was received directly is also updated as Completed with return.

Once the cover is returned, the cover suspense is debited and the loro or nostro account of the reimbursement agent is credited. In the announcement message, the cover suspense was debited, and the corresponding customer or creditor was credited. Now, this transaction must be manually reversed as part of the operational procedure.

While manually initiating a return for completed SWIFT transactions from the Return Enquiry, user can select and capture the return originator details using the *Return Originated By* field. Allowed values are,

- Customer – Customer or beneficiary of the original transaction is the originator for the return transaction.
- Bank – Processing company is originator for the return transaction.
- Blank (default option) – System maps the company BIC in the outgoing message.

In the Return of SWIFT completed credit txn OE screen, the Payment Processing Information section displays the details of the original transaction. Debit Side Info and Credit Side Info section displays the details of the return transaction (Swapped account details of the original transaction). Debtor Info and Creditor Info sections display the details of the original transaction. Authorization screen of this enquiry displays the same details as mentioned above.

[Partial Return](#)

Temenos Payments Hub supports partial return of customer transfer (pacs.008) and bank transfers including cover (pacs.009,pacs.009 COV), in which case the creditor is already credited and need to return a part of the transaction amount because the creditor was excess paid or it is a partial refund based on the request from the creditor.

In the Return of SWIFT Completed Credit Txn screen, the user can select the partial return and enter the partial return amount. In the original transaction, there is an indicator for partial return.

If the authorizer rejects the return transaction or when the user cancels the outgoing return payment from the repair screen, the system deletes the partial return indicator in the original transaction.

The **User Menu** > **Payments** > **Payment Hub** > **Payment Inquiries** > **Pending and Processed Payments** enquiry displays the high-level view of the payment for the original transaction and return payment, and the partial return indicator.

[Return Instructed Amount and Currency](#)

The transaction currency of the return payment is always in the currency of the original transaction but the creditor can instruct a return amount in a different currency.

In the Return of SWIFT Completed Credit Txn screen, the user can enter the return instructed amount and instructed amount currency applicable for both full and partial returns. On submission, the system populates the return amount after performing the currency conversion based on the exchange rate.

When the user validates the transaction, the system performs the following validations related to the instructed scenario:

- Return instructed currency cannot be same as the transaction currency of the original transaction
- Return instructed currency must be same as the debtor currency of the return payment (that is, creditor of the original transaction)
- If the user enters the return instructed currency, then the return instructed amount is mandatory and vice-versa
- If the user enters the return instructed amount, then the user cannot enter the return amount as the system automatically calculates it. This validation applies for partial return as well
- Return instructed currency must be valid
- Return instructed amount must be greater than 0
- The maximum amount and number of digits allowed for the return instructed amount is based on the existing *Instructed Amount* field in the ISO OE screen.

[Payment Return of Complete Financial Institution to Financial Institution Credit Transfer (pacs.009) based on camt.053 or camt.054](#)



|  |  |
| --- | --- |
| Debtor | Impose Name and Address details of Bank D  Enter Debtor Account number as either a suspense or Bank D’s nostro with Bank C |
| Debtor Agent | Bank C |
| Creditor | Bank A |
| Creditor Agent | Bank B |

In the above scenario, Temenos Payments Hub bank (Bank D) has to initiate a bank transfer return (pacs.004) using the **Outgoing ISO Bank Transfer Return** enquiry mentioned below. The user has to enter the details based on the details received in the camt.053.

**User Menu** > **Payments** > **Payment Hub** > **Initiate Payment Transaction** > **Initiate ISO Bank Transfer** > **Outgoing ISO Bank Transfer Return**.

In the Outgoing ISO Bank Transfer Return screen, the user must enter the nostro account of Bank C as the debtor account and impose the debtor details with Temenos Payments Hub bank BIC, so that the details are sent out in the outgoing pacs.004.

[Charge Options for Return Payment](#)

Charge option for a return payment in CBPR+ can be either CRED or SHAR. Charge options DEBT and SLEV are not allowed for return payment.

In pacs.004, charge information is mandatory if charge bearer is CRED. If no charges are taken, the user uses zero in Amount (any agent in the payment chain) in case of CRED. In case of SHAR option, if deduct is taken then charge information is mandatory. Charge information is optional for initiator if no charges are taken.

When return is generated in Temenos Payments Hub, based on a pacs.002 reject or when a payment is returned through GUI, the charge option is always set as shared (SHAR). Return charge processing is supported if the underlying payment being returned is a customer transfer.

For an outgoing return payment for customer transfer with SHAR/SHA charge option, the system can debit the customer for any charges for processing the return (based on the agreement for the charges) and also determine if the receiving bank (instructed agent) must be charged for processing the return (charges to be deducted from the return amount). The system provides a conditional fee, Outgoing Return Fee that can be configured to charge banks for returns.

For an outgoing return payment for bank transfer with SHAR/SHA charge option, the system can determine if the receiving bank (instructed agent) must be charged for processing the return (charges to be deducted from the return amount). The system provides a conditional fee, Outgoing Return Fee that can be configured to charge banks for returns.

For a redirected return payment for customer and bank transfer with SHAR/SHA charge option, the system determines if if the sending bank or the receiving bank (instructed agent) should be charged for processing the return (charges to be deducted from the return amount). The system provides a conditional fee, Redirected Return Fee that can be configured to charge banks for redirected returns.

Read [Fees and Billing](../../Payments_Hub_(PP)/Fees_and_Billing/Introduction.htm) to know more information on charges for return payment.

[Return Chain Population in Generated pacs.004 Return Message](#)

The Return Chain element captures all the parties and agents involved in the return transaction, nearly in the same way the underlying payment message captures all the parties and agents involved in a payment.

In this element, the role of various parties and agents change. The following image and table depicts how the party and agents roles from the incoming payment are mapped into return chain component of pacs.004 when the payment is returned.

/Introduction_23.png)

| Incoming Transaction | | | Return Transaction | | |
| --- | --- | --- | --- | --- | --- |
| Ultimate Debtor | ULTDBT | Debit | Ultimate Creditor | ULTCDT | Credit |
| Debtor | ORDPTY | Debit | Creditor | BENFCY | Credit |
| Debtor Agent | ORDINS | Debit | Creditor Agent | ACWINS | Credit |
| Previous Instructing Agent 1 | PRVINS | Debit | Intermediary Agent 3 | INTIN3 | Credit |
| Previous Instructing Agent 2 | PRVIN2 | Debit | Intermediary Agent 2 | INTIN2 | Credit |
| Previous Instructing Agent 3 | PRVIN3 | Debit | Intermediary Agent 1 | INTINS | Credit |
| Initiating Party | INIPTY | Debit | Not mapped in return |  |  |
| Intermediary Agent 1 | INTINS | Credit | Previous Instructing Agent 3 | PRVIN3 | Debit |
| Intermediary Agent 2 | INTIN2 | Credit | Previous Instructing Agent 2 | PRVIN2 | Debit |
| Intermediary Agent 3 | INTIN3 | Credit | Previous Instructing Agent 1 | PRVINS | Debit |
| Creditor Agent | ACWINS | Credit | Debtor Agent | ORDINS | Debit |
| Creditor | BENFCY | Credit | Debtor | ORDPTY | Debit |
| Ultimate Creditor | ULTCDT | Credit | Ultimate Debtor | ULTDBT | Debit |

Account-related information (such as debtor account, creditor account and so on) is not present in the pacs.004 message in return chain. Hence, when an incoming return payment is received, the system identifies the original payments and fetches the account information to process the incoming return. The party or agent roles should be properly populated by any bank initiating the return because the subsequent agents refers this information while redirecting the return payment. Ideally, the return payment should flow through the same banks through which the incoming payment was received.

If the return is an incomplete return (Read the [Manual Return or Reject Scenarios](#Manual) section for more details), the mapping of return chain in pacs.004 is different from pacs.004 when the customer is credited. The system performs the following:

- Maps Temenos Payments Hub bank as debtor (Return chain or Debtor agent ) and not the original creditor
- Maps the original instructing agent as debtor agent in the return chain
- Does not map the original intermediary agent(s) present in the underlying payment in the return chain (in case redirected).

## Processing Received Return Payment

CBPR+ allows SWIFT International payments to be returned using pacs.004 message format. Banks can return following types of payments:

- Customer Payment (pacs.008)
- Bank Transfer (pacs.009)
- Cover (pacs.009 COV)

When the system processes the outgoing and redirected payments and sends out through SWIFT, it is possible to receive return. The system supports processing of inward return payments received against original outgoing or redirected payment sent earlier. The received CBPR+ pacs.004 return payments are stored in system and identified with clearing transaction type as RT.

The following sections provide details on inward return payment processing functionality supported by the system.

[Return Processing for Serial Payment Scenarios](#)

The following sections explain about the receiving pacs.004 return against previous sent outgoing or redirected cross border transfers.

While processing the received pacs.004 return, the system can send positive or interim payment status report (pacs.002), if configured in bank conditions. Incoming pacs.004 return payments should not be rejected and therefore pacs.002 Reject is not sent.

The system does not allow incoming return payments (pacs.004) to be rejected or returned back to the instructing agent. If the bank is unable to process the received return payment, then it must communicate with the sender bank and handle the scenario manually.

When Temenos Payments Hub receives a partial return (return message pacs.004 from SWIFT with the value of ReturnReasonInformation/Additional information tag as PART), it marks the return transaction as partial return and updates the partial return indicator of the related original transaction.

When the user cancels the incoming return payment from the repair screen, the system deletes the partial return indicator in the original transaction.

The **User Menu** > **Payments** > **Payments Hub** > **Payment Inquiries** > **Pending and Processed Payments** enquiry displays the high-level view of the payment for the original transaction and return payment, and partial return indicator.

[Receive and Process pacs.004 Return Against Outgoing Transfers Settled Serially](#)

The system can receive a pacs.004 return message for an outgoing transfer processed and sent through SWIFT using serial method of settlement.

/Introduction_24.png)

The following are possible scenarios:

- Receive CBPR+ pacs.004 return against outgoing cross border customer transfer. The outgoing customer transfer could have been sent either as MT103 or pacs.008 based on configuration
- Receive CBPR+ pacs.004 return against outgoing cross border bank transfer. The outgoing bank transfer could have been sent either as MT202 or pacs.009 based on configuration

On receipt of the pacs.004 return payment against outgoing payments, the system performs the following processing.

- On receiving pacs.004 return, the system finds the original outgoing transaction in the system (live and archive) using Original instruction ID or original UETR (if original instruction id is not present) present in the incoming pacs.004. If the system does not identify the original transaction, then the received pacs.004 is routed to repair with 'Original transaction not found’ error message.

- Once the original transaction is identified, the system checks for the status of the original transaction. If the original transaction is not in the Completed status, then the return payment is routed to repair queue with the 'Original transaction is not in completed status' functional error. Also this Pacs.004 is displayed in unmatched enquiry.
- If the original transaction is not in the Completed status, then the return payment is routed to repair with functional error, ‘Original transaction is not in completed status’. Also, this pacs.004 is displayed in the **Unmatched Return Payment** enquiry.
- If the pacs.004 message is received for the outgoing bank transfers where beneficiary institution is Temenos Payments Hub bank, then the return payment is always routed to repair as the system is not able to determine the credit account of the return payment. The bank user has to manually enter the credit account number and complete the payment.
- The system enriches the credit account of the return transaction from the debit account of the original transaction.

[Receive and Process pacs.004 Return Against Redirected Transfers Settled Serially](#)

If the processing bank acts as an intermediary, then it can receive payments from other correspondent banks/clearing and redirect it through SWIFT. The system can receive a pacs.004 return message for such redirected payments sent through SWIFT using serial method of settlement.

/Introduction_25.png)

The following are possible scenarios:

- Receive CBPR+ pacs.004 return against redirected customer transfer received from correspondent bank or clearing. The redirected customer transfer could have been sent either as MT103 or pacs.008 based on configuration.
- Receive CBPR+ pacs.004 return against redirected cross border bank transfer received from correspondent bank or clearing. The redirected bank transfer could have been sent either as MT202 or pacs.009 based on configuration.
- Receive CBPR+ pacs.004 return against redirected cross border cover transfer received from correspondent bank or clearing. The redirected bank transfer could have been sent either as MT202 COV or pacs.009 COV based on configuration.
- Receive pacs.004 return from clearing (for example, TARGET2) against redirected customer transfer received from correspondent bank. The redirected customer transfer could have been sent either as MT103 or pacs.008 based on clearing configuration.

On receipt of the pacs.004 return payment against redirected payments, the system performs the following processing.

- On receiving pacs.004 message, the system finds the original transaction (in both live and archive) using Original instruction id or original UETR (if original instruction id is not present) present in the incoming pacs.004 message. If the original transaction is not identified, then the received pacs.004 is routed to repair with error message, 'Original transaction not found’.
- Once the original transaction is identified, the system checks for the status of the original transaction. If the original transaction is not in the Completed status, then the return payment is routed to repair queue with functional error, 'Original transaction is not in completed status'. Also, this pacs.004 is displayed in the **Unmatched** enquiry.
- If the status of the original transaction is in the Completed status, then the return payment is processed further.

- If the original transaction is received from a Clearing (for example, TARGET2), then the system imposes the output channel in the return transaction, so that the return message is generated as per the clearing format and sent to the same clearing from which original payment was received.
- If the original transaction is received from the correspondent bank over SWIFT, then the system imposes the output channel of the return transaction based on the debit account of the original transaction.

- If the Loro account is debited, then the system imposes the output channel as Loro
- If the Nostro account is debited, then the system imposes the output channel as NOSTRO

- System also does the following enrichment on return transaction,
  - The credit account of the return transaction is imposed from from the Debit account of the original transaction.
  - The creditor details of the return transaction is imposed from the debtor details of the original transaction when the account details are not present in the received return transaction as a part of Original Transaction Reference tag element.

- If any failure occurs while processing the return transaction, it is routed to repair.
- Till the time the return transaction is getting processed, status of the original transaction is moved to Payment being returned status.
- The system performs the following validations before forwarding the return payment through SWIFT
  - CBPR+ format validations for the return payment  (required fields are present as per CBPR+ rule)
  - RMA Check with the instructing agent of the return payment
  - Account validation (Nostro/Vostro) with the instructing agent of the return payment
  - Cut-off time check
- On processing the return transaction to be routed through SWIFT, CBPR+ pacs.004 message is generated only if the processing bank is configured to send cross border messages in MX format. Otherwise payment is routed to repair queue with error message.
- Once the pacs.004 message is generated and sent out to the instructing bank of the original transaction, then the status of the original transaction is updated as Completed with Return. Status of the return message is updated as Completed.
- If RMA is not there between TPH bank and the receiver bank for sending a pacs.004 message, then message lands in repair queue. The user has to manually impose the different receiver BIC with whom RMA is available for pacs.004, impose channel and credit account and commit the payment. Once the payment is authorized, the pacs.004 message gets generated and sent to swift network

The flow and processing is same even when redirecting pacs.004 return transaction from CBPR+ to Clearing (for example, STEP2). While redirecting the message to Clearing, Temenos Payments Hub performs all clearing validations for return message before sending it to the Clearing. The system updates the following accounting entries for the redirected return transaction and the settlement transaction for the Clearing.

- Dr - Loro/Nostro account ; Dr - Clearing Suspense Account
- Cr - Clearing Suspense Account ; Cr - Clearing Nostro Account

[Receive Return pacs.004 Against Redirected Transfer Settled Serially and Processing Bank in MT Mode](#)

As explained in the previous two sections, when redirected payments are sent through SWIFT, the bank may receive pacs.004 return. The system supports redirecting the return in pacs.004 format only if the processing bank is configured to send cross border payments in MX format. If the processing bank is still configured to process cross border payments in MT format, then the system does not redirect the received pacs.004.

The possible scenarios are:

- Receive pacs.004 return message from SWIFT for redirected customer or bank transfer sent as MT 103/MT202 (bank is in MT mode)
- Receive pacs.004 message from clearing (e.g. TARGET2) for redirected customer or bank transfer received as MT103 or MT202.

The system performs the following actions for such scenario.

- On receiving pacs.004 message, the system routes the return payment to repair queue with functional error, Bank is not MX enabled, so the return pacs.004 message cannot be routed to the correspondent bank.
- Bank user has to cancel the return payment from repair queue.
- Bank user has to create a new return payment MT103 / MT202 with REJT or RETN code word in the Tag 72 from order entry screen and send it to the original sender of the transaction.

[Return Processing for Cover Payment Scenarios](#)

[Receive and Process pacs.004 Return for Outgoing Transfer Settled through Cover Method](#)

/Introduction_19.png)

The system can receive a pacs.004 return message for an outgoing transfer processed and sent through SWIFT using cover method of settlement.

The following are possible scenarios:

- Receive CBPR+ pacs.004 return against outgoing MT 202 COV
- Receive CBPR+ pacs.004 return against outgoing pacs.009 COV
- Receive CBPR+ pacs.004 return against outgoing pacs.009 which case of bank transfer cover sent against a pre-advice

On receipt of the pacs.004 return payment against outgoing cover, the system performs the following process.

- On receiving pacs.004 message, the system finds the original transaction (live and archive) using the original instruction id present in the incoming pacs.004 message.

If the original transaction is not identified, then the received pacs.004 message is routed to repair queue with error message, ‘Original transaction not found’.

- Once the original transaction is identified, the system checks for the status of the original transaction.
- If the status of the original transaction is not in completed status (could have been already reversed on receipt of a pacs.002), then the return payment is routed to repair queue with a warning message stating that the original transaction is not completed (the user can configure this error as a warning or a hard stop error in PP.ERRORCODE table). In case of a hard stop error, the user cannot submit the payment from the repair queue.
- If the status of the original transaction is in completed status, then the return payment is routed to repair queue with an information error as ‘This is a return for an underlying payment that was settled through a cover’.
  - The bank user has to manually enter the credit account number of the customer and complete the payment processing.
  - Once the user enters the valid credit account number and process successfully, received return payment is moved to Completed status. Original transaction status is updated as Completed with return.

  It is also possible for the system or the bank to receive a pacs.002 RJCT for an announcement message from the creditor agent, when the return is received for the cover and parked in the repair queue. If the user has taken an action on the pacs.002 RJCT message from the SWIFT ISO Business Exception enquiry, then the message gets reversed, and the accounting entries are reversed, which eventually updates the payment status to 993. In this case, the received return for the cover message, which is waiting in the repair queue should be cancelled manually as an operational procedure since the amount is credited, which was initially debited from the debtor.

[Receive and Process pacs.004 Return for Redirected Transfer Settled through Cover Method](#)

/Introduction_20.png)

The system can receive pacs.004 return message for the originally redirected transaction settled through the cover method.

The following are possible scenarios:

- Receiving pacs.008 from the correspondent bank or from clearing and Temenos Payments Hub bank generates pacs.008 / MT103 to the receiver bank and pacs.009 COV / MT202 COV message to the correspondent bank – pacs.004 received for cover message.
- Receiving MT103 from correspondent bank or from clearing and Temenos Payments Hub bank generates pacs.008 / MT103 to the receiver bank and pacs.009 COV / MT202 COV message to the correspondent bank – pacs.004 received for cover message.
- Receiving pacs.009 from the correspondent bank or from clearing and Temenos Payments Hub bank generates pacs.009 ADV (pre-advice) to the receiver bank and pacs.009 message to the correspondent bank – pacs.004 received for the cover message.

On receipt of the pacs.004 return payment against the cover, the system performs the following processing.

- The system finds the original transaction (live and archive) using the original instruction id present in the incoming pacs.004 message.

If the original transaction is not identified, then the pacs.004 message is routed to repair queue with error message, ‘Original transaction not found’.

- Once the original transaction is identified, the system checks for the status of the original transaction.
- If the status of the original transaction is not in completed status, then the return payment is routed to repair queue with a functional error as ‘Original transaction is not in completed status’.
- If the status of the original transaction is in completed status, the return payment is routed to repair queue with an information error as ‘This is a return for an underlying payment that was settled through a cover’.
  - The user has to manually enter the suspense account number and complete the payment.
  - Once the user enters the valid credit account number, the return payment is moved to the ‘Completed’ status. Original transaction status is updated as ‘Completed with return’.

    The user has to manually initiate a new return payment using a Return GUI and send to the correspondent bank or to the clearing. The return GUI can be accessed using the following menu:

    **User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Return/Reject Payment** > **Initiate Rtn for txn setld with cov**.

The imposing of credit account number in return message from the original transaction does not happen for cover scenario.

[Receive and Process pacs.004 Return for Redirected Transfer Received through Cover Method](#)

The system receives pacs.004 return message for the originally redirected transaction received through the cover method.

The following are possible scenarios:

- Receiving pacs.008 or MT103 from debtor agent bank and MT202 COV or Pacs.009 COV from the correspondent bank and settling serially the pacs.008 or MT103 with the instructed agent - pacs.004 is received for the outgoing pacs.008 or MT103.
- Receiving pacs.008 or MT103 from debtor agent bank and camt.053 or camt.054 from the correspondent bank and settling serially the pacs.008 or MT103 with the instructed agent - pacs.004 is received for outgoing pacs.008 or MT103.
- Receiving pacs.009 ADV (pre-advice) from debtor agent bank and pacs.009 or camt.053 from the correspondent bank and settling serially the pacs.009 with the instructed agent – pacs.004 received for outgoing pacs.009.

/Introduction_26.png)

On receipt of the pacs.004, the system performs the following processing.

- The system finds the original transaction (live and archive) using the original instruction id present in the incoming pacs.004 message.

If the original transaction is not identified, then the pacs.004 message is routed to repair queue with error message, ‘Original transaction not found’.

- Once the original transaction is identified, the system checks for the status of the original transaction.
- If the status of the original transaction is not in completed status (could have been already reversed on receipt of a pacs.002), then the return payment is routed to repair queue with a functional error, Original transaction is not in completed status. The user cannot submit the payment from repair queue.

- If the status of the original transaction is in completed status, the return payment is routed to repair queue with a functional error, ‘This is a return for the redirected payment that was settled through cover on the debit side’. The status of the original transaction is updated to Return in progress.
- This return transaction is also displayed in the **Inwd Rtn of Rdrct Pymnt rcvd via COV** enquiry, from which the user can only cancel the transaction. This enquiry can be accessed through the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Cancellation** > **Swift Cancellation** > **Inwd Rtn of Rdrct Pymnt rcvd via COV**

- Once the user manually cancels the transaction from the enquiry, the status of the original transaction is updated as ‘Completed’ and audit trail of the underlying direct message and cover message is also updated.
- If Temenos Payments Hub bank has received pacs.009 COV message from the correspondent bank, then the user has to manually create a return transaction pacs.004 from the **Return of SWIFT completed credit txn** enquiry, which can be accessed through the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Return/Reject Payment** > **Return of SWIFT Completed Credit Txn**

- While manually initiating a return for completed SWIFT transactions from Return Enquiry, user can select and capture the return originator details using the *Return Originated By* field. Allowed values are,

  - Customer – Customer or beneficiary of the original transaction is the originator for the return transaction.
  - Bank – Processing company is originator for the return transaction.
  - Blank (default option) – System maps the company BIC in the outgoing message.

    /Return4.png)

- When the return is initiated from the above enquiry, the status of the underlying credit transfer is marked as ‘Completed with return’.

The following is the accounting entry of return transaction created from the **Return of SWIFT Completed Credit Txn** enquiry.

| Return Transaction | |
| --- | --- |
| Dr | Suspense account |
| Cr | Correspondent bank nostro or vostro (that sends pacs.009COV or MT202COV) |

The user has to manually initiate a new incoming customer transfer payment from ISO screen to park the funds that is coming from instructed bank of underlying MT103 or pacs.008.

| New incoming Customer Transfer | |
| --- | --- |
| Dr | Instructed bank of MT103 or pacs.003 Nostro |
| Cr | Suspense account |

- If Temenos Payments Hub bank receives camt.053 or camt.054 message from the correspondent bank, then the user has to manually create a return transaction pacs.004 from the **Outgoing ISO Bank Transfer Return** enquiry, which can be accessed through the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Initiate Payment Transaction** > **Initiate ISO Bank Transfer** > **Outgoing ISO Bank Transfer Return**.

- The user has to enter all the party details manually based on the details received in the incoming camt.053 or camt.054 message, select the return reason code and submit. After authorising the return payment, the status of the return transaction pacs.004 is updated as Completed 999 and the pacs.004 message is sent to the instructing bank of the original transaction.

The user can create the return from this enquiry only if the processing company is enabled with SWIFT MX. The same screen is used when Temenos Payments Hub receives pacs.002 from the creditor agent for the underlying redirected MT103 or to send pacs.008 and pacs.004 based on camt.053 or camt.054. The imposing of credit account number in return message from original transaction does not happen for cover scenario.



[Receive and Process MT103/MT202 REJT or RETN Message](#)

On receiving MT103 or MT202 with RETN or REJT code word (in Tag 72) from correspondent bank, the original transaction is identified based on the reference present in the MREF code word (in Tag 72). If the transaction reference is not present in the incoming message or if the transaction is not found, then the incoming return message is routed to repair queue.

Once the original transaction is identified in the system, same reference is updated in the *OriginalorReturnID* field in incoming return transaction for the cross reference.

The incoming MT message with RETN/REJT code word is routed to repair queue through inbound code word configuration, which is set to repair. The user can view the incoming MT reject/return messages using the, **Return/Reversal Inward SWIFT MT Rtn** enquiry, which can be accessed through the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Return/Reject Payment** > **Return/Reversal Inward SWIFT MT Rtn**

The user cannot return or reject this payment from the repair queue. If the user takes return or reject action for this payment from the repair queue, then the system displays an error message, ‘No Return/Reject allowed. Please take actions from the Return/Reversal Inward SWIFT MT Rtn enquiry’.

The enquiry provides following options:

- View the transaction details
- Cancel the transaction
- Return/Reject the transaction

[Process MT103/MT202 RETN/REJT Message from SWIFT (for original outgoing payment settled serially)](#)

/Introduction_27.png)

From the enquiry, the user can select either reject or return option for the incoming return transaction (corresponding underlying transaction is outgoing). On clicking the Return/Reject button, the system checks if the status of the underlying transaction is completed. If the transaction is in completed status, then the payment is sent to authorisation.

Authoriser can view and authorise the transaction using the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Payment Approvals** > **Authorise Pmt Investigation and Cancellation** > **Return/Reject of SWIFT Transfers** > **Return/Reversal Inward SWIFT MT Rtn**

Once the authoriser approves the transaction, a new reversal transaction is created by debiting the original credit account and by crediting the original debit account.

Status of the original transaction is updated as reversed (993) and the status of the incoming MT return transaction is updated as completed. Audit trail is updated to indicate underlying payment has been reversed or returned.

Transaction amount in reversal transaction is same as that of the transaction amount that was sent to the instructed agent of the original transaction irrespective of the charge option.

[Process MT103/MT202 RETN/REJT Message from SWIFT (for an original redirected payment settled serially)](#)

/Introduction_28.png)

From the enquiry, the user can select either Return or Reject option for the incoming MT return transaction (for which underlying transaction is redirected). On clicking the Return/Reject option from the enquiry, the system checks if the source of the underlying transaction is from clearing or from SWIFT.

- If the underlying transaction is from clearing, then the system checks the return message format in the Clearing table. If the return message format is not defined in the Clearing table, then the system displays an error message.
- If the underlying transaction is from SWIFT, then the system checks if the processing bank is configured to send cross border payments in MX format. If not, then an error message is displayed as ‘Payment cannot be returned as a pacs.004 as the Bank is not SWIFT ISO enabled’. The user can only cancel such transactions.
- If the company is MX enabled, then the transaction is submitted for authorisation.  These transactions can be authorized using following enquiry:

**User Menu** > **Payments** > **Payment Hub** > **Payment Approvals** > **Authorise Pmt Investigation and Cancellation** > **Return/Reject of SWIFT Transfers** > **Return/Reversal Inward SWIFT MT Rtn**

- While manually initiating a Return for completed SWIFT transactions from Return Enquiry, user can select and capture the return originator details using the *Return Originated By* field. Allowed values are,
  - Customer – Customer or beneficiary of the original transaction is the originator for the return transaction.
  - Bank – Processing company is originator for the return transaction.
  - Blank (default value) – Maps the company BIC in the outgoing message.

- Once the authoriser approves the transaction, then a new return transaction (RT) is created with an ISO return reason code, which is equivalent of FIN return reason code.
- The transaction amount of the return transaction is the amount that was sent to the instructed agent of the original transaction irrespective of the charge option (BEN,SHA or OUR)
- Temenos Payments Hub does not consider the charges mentioned in tag 72 if provided .They have to be claimed separately by the correspondent bank
- Following entries are raised as part of the return payment
  - Debit  :Instructed agent account ( that was credited as part of the original transaction )
  - Credit : Instructing agent/Sender of the original transaction
- On successful processing, pacs.004 message is generated and sent to the original sender of the underlying transaction. Once pacs.004 message is generated and sent out, then the status of the pacs.004 message is updated as ‘Completed’ and status of the underlying transaction is updated as ‘Completed with return’.
- The return payment generated by Temenos Payments Hub based on a MT 103/MT202 RETN/REJT is considered as outgoing (not redirected as Temenos Payments Hub has created the return) and the charge option of the return payment is set as ‘SHA’ irrespective of the charge option of the underlying transaction
- Temenos Payments Hub bank can deduct the charges from the transaction amount of the return payment for processing the return payment if redirect return charges have been configured with the instructed agent of the return payment (receiver of the return payment).

[Process MT103/MT202 RETN/REJT Message Received for Original Outgoing Payment Settled with Cover (credit side)](#)

/Introduction_29.png)

On selecting the Return or Reject option from the enquiry for the incoming MT return transaction (for which underlying transaction is outgoing and settled through cover method), the system displays an error ‘Underlying payment was settled through cover so cannot be reversed or returned’. The user can only cancel the transaction.

- If the underlying transaction is outgoing, the user has to cancel the incoming MT return transaction from the enquiry and create a new transaction (using Order Entry) to credit the customer once Temenos Payments Hub receives money through MT202.
- If the underlying transaction is redirected, the user has to cancel the incoming MT return transaction from the enquiry and create a return transaction using the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Return/Reject Payment** > **Initiate Rtn for txn setld with cov**

[Process MT103/MT202 RETN/REJT Message Received for Original Redirected Payment Settled with Cover (credit side)](#)

/Introduction_29.png)

On selecting the Return or Reject option from the enquiry for the incoming MT return transaction (for which underlying transaction is redirected and settled through cover method), the system displays an error ‘Underlying payment was settled through cover so cannot be reversed or returned’. The user can only cancel the transaction.

[Process MT103/MT202 RETN/REJT Message for Original Redirected Payment Settled through Cover (debit side)](#)

/Introduction_30.png)

On selecting either the Return or Reject option for the incoming MT return transaction (for which underlying transaction is received through cover method), the system displays an error ‘Underlying payment was settled through cover so cannot be reversed or returned’. The user can only cancel the transaction.

Once the MT return transaction is cancelled, the user has to create a new return transaction from GUI screen once funds are received through MT202. The user can create a new return transaction for the completed incoming transaction using the following menu:

**User Menu** > **Payments** > **Payment Hub** > **Initiate Payment Transaction** > **Initiate ISO Bank Transfer** > **Outgoing ISO Bank Transfer Return**.

| Customer Transfer | Bank Transfer |
| --- | --- |
| The direct or announcement message is pacs.008 and a cover message is pacs.009 COV | The direct or announcement message is pacs.009 ADV and the cover message is pacs.009 |

[Process MT202 RETN/REJT Message for Underlying Cover Generated by Temenos Payments Hub bank](#)

/Introduction_31.png)

On receiving MT202 return transaction for which underlying transaction is the cover message (pacs.009 or MT202 COV), the system cannot match the incoming return transaction with the original transaction, since the reference of the cover message is not stored in Temenos Payments Hub. So the system does not know if the received return message is for the direct message or for the cover message.

On clicking the Return/Reject option for such transaction, the system displays an error on screen, ‘Original transaction not found so cannot be reversed or returned’. The only option available for the user is to cancel the transaction.

| Customer Transfer | Bank Transfer |
| --- | --- |
| The direct or announcement message is pacs.008 and a cover message is pacs.009 COV | The direct or announcement message is pacs.009 ADV and the cover message is pacs.009 |

[GUI based Manual Initiation of Return (pacs.004) for Customer Transfer](#)

When the system receives pacs.004 message for an original outgoing or redirected customer transfer settled through cover method, the received pacs.004 message is routed to repair queue with an informational error. The user has to manually complete the pacs.004 message by entering the credit account number.

If the underlying transaction is redirected, the user has to manually create a pacs.004 message and send to the original sender of the transaction. This return transaction for the underlying customer transfer can be created using the following enquiry:

**User Menu** > **Payments** > **Payment Hub** > **Payment Investigations and Cancellations** > **Return/Reject Payment** > **Initiate Rtn for txn setld with cov**

From this enquiry, the user can do the following action,

- View the payment details
- Create a return transaction

On clicking the return action for the transaction for which return needs to be initiated, a new order entry GUI screen opens with necessary party and agent details auto populated from the underlying transaction. The user manually enters the remaining information. The charge option for the return payment is defaulted to SHA, which cannot be changed. The output channel of the return transaction is auto-populated based on the originating source of the underlying transaction.

While manually initiating a return for SWIFT transactions from ISO Return Enquiry, user can select and capture the return originator details using the *Return Originated By* field. Allowed values are,

- Customer – Customer or beneficiary of the original transaction is the originator for the return transaction.
- Bank – Processing company is originator for the return transaction.
- Blank (default option) – System maps the company BIC in the outgoing message.

The user must select the return reason code. The user has to manually enter the debit account number and submit the transaction. This is because on receiving pacs.004 message for the cover, the process is non-STP and the user has completed the transaction manually by entering the credit account number from repair queue. So now on generating the pacs.004 to the original sender of the transaction, the same credit account number should be entered and debited.

Once the transaction is submitted, it is forwarded for authorisation. The transaction can be authorized using the following menu:

**User menu** > **Payment** > **Payment hub** > **Payment approvals** > **Authorise Pending payments** > **Authorise order entry and repair payments** > **Pending Authorise payments**.

Once the authoriser approves the transaction, it is processed and pacs.004 message is generated and sent to the original sender of the underlying transaction only if the processing company is MX enabled for cross border payments.

If the processing company is not MX enabled, then an error message is displayed on screen as ‘Cannot return the payment to Swift’.

[Unmatched Return Transaction](#)

On receiving pacs.004 return message from SWIFT, if the original transaction is not identified, then the received pacs.004 is parked in Unmatched queue. Also, this pacs.004 is displayed in repair queue. These return payments can be viewed using the following enquiry:

**User menu** > **Payment** > **Payment hub** > **Payment Inquiries** > **Pending Payments** > **Pending Unmatched R-Payments**

From this unmatched queue, the user can edit or view the transaction. On editing the transaction, transaction opens in repair mode and the user can enter the Original FT number. If the original FT number is present in the system and it is in the ‘Completed’ status, then it gets linked with the return transaction and also gets enriched only for ISO enabled transaction as follows:

- If the original transaction is Outgoing and in the ‘Completed’ status, then the debit account number of the original transaction is imposed as the credit account number of the return transaction.
- If the original transaction is redirected and in the ‘Completed’ status, then the originating source of the underlying transaction gets imposed as the output channel of the return transaction.

The user can also submit the return transaction from unmatched queue without entering the original FT number. In that case, pacs.004 message gets routed based on the parties present in the return message (point to point details of the original transaction are not populated).

If the original FT number is not entered for the pacs.004, which has to be routed to clearing (for example, TARGET2), then the channel validation error is displayed to enter the original interbank settlement date and amount which are mandatory for outgoing pacs.004 message.

Temenos Payments Hub does not support the manual processing of MT103 and MT202 return messages from the unmatched queue.

[Order Entry Screen for Investigation Users to Initiate Return](#)

If the cancellation request has been received for a transaction that was processed in the legacy system and the bank would like to return the amount that was previously credited, then the investigation officer can use the OE screen to initiate such returns.

If the payment that needs to be returned is a customer transfer, then the bank user can use Outgoing ISO Customer Transfer Return screen to initiate the return. If the payment is a bank transfer, then the bank user can use Outgoing ISO Bank Transfer Return screen to initiate return. The user can use the *Related Reference* field in this order entry screen to mention the transaction details.

To initiate the BTR return, go to **User Menu** > **Payments** > **Payments Hub** > **Payment Investigation and Cancellations** > **Return/Reject Payments** > **Outgoing ISO Bank Transfer Return**.

To initiate the CTR return, go to **User Menu** > **Payments** > **Payments Hub** > **Payment Investigation and Cancellations** > **Return/Reject Payments** > **Outgoing ISO Customer Transfer Return**.

The bank requires the PPISOX license to access these menus. The user has to manually fill all the mandatory details to initiate the return transaction. Once validated and submitted, the record moves to the existing authorisation queue. Once it is authorised by the authoriser, the transaction gets created and sent out to the receiver bank.

## Notification to Receive

Notice to Receive message is an advance notice by account owner to their account servicing institution that it will receive funds to be credited to sender’s account.  It is sent to the Correspondent to pre-advice incoming funds in their accounts, to ensure good value is applied for the incoming funds. For cross border international payments, CBPR+ camt.057 message is used for this purpose. The equivalent message in SWIFT FIN is MT210.

Following sections explains the support for this message in system.

[Generation of Outgoing camt.057](#)

Notification to receive message is sent when bank wishes to transfer funds from one Nostro account to another Nostro account (Own Account Transfer). The system supports automatic generation of notification to receive message (camt.057) for the following scenarios:

- A CBPR+ own account transfer is initiated using the ISO Outgoing Own Account Transfer menu
- A CBPR+ bank transfer is initiated using the ISO Outgoing Bank Transfer menu
- A CBPR+ bank transfer is initiated from payment order using the CBPR+ Bank Transfer menu

When these Own Account Transfer or Bank Transfer payments are processed successfully, the system generates CBPR+ pacs.009 sends through one or more intermediary agents. If bank condition is configured, the system automatically generates the notification to receive (camt.057) message also and sends directly to the creditor agent. To generate camt.057, the following conditions must be satisfied:

- Direction must be outgoing (that is, initiated from system)
- Transaction should be a Bank Transfer
- Bank Condition (for the creditor agent) configured to generate camt.057 (either for the creditor agent BIC or at default level)
- Creditor / Beneficiary Institution BIC is same as processing company BIC (indicating its own account transfer)
- Instructed Agent / Receiver BIC of the bank transfer is not same as creditor agent BIC (means payment is not sent directly but through intermediaries)
- RMA is maintained to send camt.057 message (if RMA is not available, camt.057 is not generated, an audit trail entry is added indicating the same)

First the CBPR+ pacs.009 (Bank Transfer) message is generated and sent through SWIFT. Once a positive technical acknowledgement is received (indicating SWIFT has accepted the message), then camt.057 message is generates and sent through SWIFT. In case pacs.009 is receives negative technical acknowledgement, camt.057 is not generated.

[Receiving Incoming camt.057](#)

Since Notification to Receive message is a pre advice, when incoming CBPR+ camt.057 messages are received from SWIFT, an expected receipt record is created with funds type as Expected Receipts (ER). This expected receipt record can be used for manual matching or automatic matching with incoming customer and bank transfer.

On receiving incoming customer and bank transfer, which requires matching with notice to receive, TPH sends request to ER module to create a record with funds type as RECEIPTS. The Expected Receipts (ER) record gets matched with Receipts record and status is updated as Matched.

It is also possible to receive a cancellation message (camt.058) for a notice to receive message. On receiving camt.058 message, the ER module creates a record with funds type as ERCANCEL. The Expected Receipts (ER) record gets matched with this ERCancel record as well and the status gets updated as Matched. In this scenario, if TPH receives customer or bank transfer, which requires matching with camt.057, the expected receipt record created in ER module remains as Unmatched.

Read the [Expected Receipts (ER)](https://docs.temenos.com/docs/Solutions/T24_Transact/Reconciliation_Matching/ER/Expected_Recs/Misc/Introduction.htm) user guide for more information on expected receipt related features and configurations.

The system does not support generation of notice to receive (camt.057) when incoming payment is processed (received directly from debtor agent) which is settled through cover (funds will arrive through reimbursement agents). The system provides hold for cover feature using which the incoming payment can be parked until funds arrive through cover.

## Notification of Correspondence

Notification of Correspondence (admi.024) is sent by a SWIFT CBPR+ agent to notify the receiver agent of an event or information that impacts both parties. The sending agent does not expect a response from the receiving agent. TPH provides client PSPs the ability to handle Notification of Correspondence messages.

[Generation of Outgoing admi.024](#)

TPH supports creation of Notification of Correspondence in admi.024.001.01 format. The following EBQA enquiries are created to support outward admi.024 messages.

- Initiate Outward Notification of Correspondence
- View Notification of Correspondence (common enquiry for both inward & outward)

Enquiry allows user to select processed outward admi.024 based on the following selection criteria.

- Date (single) - Mandatory
- Direction (Inward / Outward) - Mandatory
- User Status - Optional
- Sending/ Receiving BIC (optional) - If it is incoming, Sending BIC will be checked and vice versa in case of outward messages.

[Notification Type](#)

Is used to identify the type of notification and the message content in admi.024. TPH allows users to select notification type in coded format. Relevant codewords has to be maintained in ISO External Codewords table. TPH allows user to maintain ISO External Codewords table either manually or through upload process (via upload 'ExternalNotificationType1Code' to the ISO External Codewords table). The uploaded codes should be visible in 'Maintenance of ISO External code'.

[Notification Narrative](#)

'Narrative' allows user to provide additional information about the notification in a narrative format. This is a mandatory element. Each occurrence should support a maximum length of each field should be 2000 characters. Allowed character set is as follows

0-9 a-z A-Z / - ? : ( ) . , ' +.

!#$%&\*=^\_`{|}~";<>@[\]

User can enter characters other than the Unicode Character Set by configuring non-SWIFT supported characters conversion table (Refer to Character Conversion to know more about special characters). Existing character support for messages sent to DELIVERY should be extended to handle admi.024 messages.

[RMA Check](#)

TPH will continue with the existing RMA check framework. TPH will check RMA check for admi.024 message if the message is listed as 'No RMA Check' required. If not configured (even in case of wildcard entry), TPH will perform RMA check before processing outward admi.024 message. In addition to RMA check, TPH will validate the receiver BIC if RD module is present. If RMA check/BIC validation fails, system will not allow user to commit the message (similar to camt.056).

[Handling ISO Technical Exceptions from SWIFT gateway](#)

TPH might receive technical acknowledgment from SAG for an outward admi.024.

- Positive Response - The message should remain in PROCESSED status.
- Negative Response - The message should remain in PROCESSED (should be same as camt.056/110) status and moved to SWIFT ISO technical exception for manual action.
- Allowed user Action from SWIFT ISO Technical Exception enquiry.
- XSD transformation failure in TPH should be handled in the same way as camt.056/110 messages.
  - **Ignore** - When the user clicks Ignore, no status change happens for the transaction. The message is not listed in exception enquiry on ignore. Status will remain as PROCESSED
  - **Resubmit** - When the user clicks Resubmit, the same message is resubmitted to the SWIFT network with possible duplicate indicator. Status will remain as PROCESSED
  - **Accept** - When the user clicks Accept, the system updates the status of the corresponding notification request as Network Rejected. Status is moved to NETWORK REJECTED

[Receiving Incoming admi.024](#)

TPH has a designated enquiry to support handling of inward admi.024 messages which is accessible from the Payments Cockpit (User Agent). User is allowed to mark an inward notification message as 'Acted Manually' from the enquiry. User should be able to change to status to CLOSED after verifying the inward message by amending the value in 'User Status' field.

[Provision for DW Export](#)

TPH allows client to download and retrieve notification messages received for a day. Refer to [Configuring Housekeeping Functions](../../Payment_Initiation_(PI)/Housekeeping_Functions/Configuration.htm) for further details on configuring DW Export for Notification of Correspondence.

## Matching with Expected Receipts

The system can be configured to match incoming payments with expected receipts (received notice to receive messages). This configuration can be maintained in bank conditions either for specific sender bank or at default level. When the system is configured for matching, then incoming (direction = ‘I’) customer transfer (pacs.008) and bank transfer (pacs.009) payments are checked against expected receipts to find a match.

When matching request for an incoming payment is sent to expected receipts module, it creates a record with funds type as ‘Receipt’ and finds if there exists a matching record with funds type as ‘Expected Receipt’. Matching criteria is configurable in ER.PARAMETER.

Read the [Expected Receipts (ER)](https://docs.temenos.com/docs/Solutions/T24_Transact/Reconciliation_Matching/ER/Expected_Recs/Misc/Introduction.htm) user guide for more information on matching.

Following are the different scenarios in matching.

[Not Matched](#)

If no match is found, then the receipt record is left as unmatched. Audit trail of the incoming payment is updated indicating no match found and the incoming payment is processed further. For unmatched records ER module returns only the id of the receipt type record.

One of the possible scenarios when this can happen is camt.057 is received after the payment is received. So the payment won’t be matched (remains in unmatched status). The expected receipt record is created later when camt.057 is received. In this scenario when camt.057 is received, the system tries to automatically match it with the previously created unmatched records. No further update is done to the incoming payment for such matching done later.

[Matched](#)

If match is found, the system checks if the notice to receive is received before or after cutoff. ER module refers the channel cutoff in Temenos Payments Hub. Cut off is checked to decide the value date to be applied for the incoming payment. For matched records, the ER module returns the id of the receipt type record as well as the expected receipt type record.

[Cutoff Breached](#)

When matched but cutoff is breached, then the system adds an audit trail entry against the incoming payment and moves the payment to repair. A warning message is also raised to indicate the same when the user opens the payment from repair. The user must manually impose the credit value date and process the payment.

[Cutoff Not Breached](#)

When matched but cutoff is not breached, then the system adds an audit trail entry against the incoming payment indicating the same. The system calculates the credit value as mentioned below and applies to the incoming payment.

Credit Value Date = Interbank Settlement Date as received in incoming payment (pacs.008 / pacs.009) + FX Shift (if applicable and defined) + Credit Float Shift (if defined)

Settlement shift is not considered while calculating the credit value date for this scenario.

[Manual Reversal of Matched Records](#)

Matching is performed only if there is no active error present during processing of the payment. In case of any active error the payment is moved to repair and matching is not performed. There can be scenarios where matching is performed and transaction moves to repair after that (such as posting error). When a payment is released from repair status, the payment is sent for matching only if it was not sent for matching earlier.

If the payment is cancelled/returned/rejected from repair queue and it was already sent for matching earlier, the system does not undo the matching status automatically. Operator needs to manually reverse the record.

The **Payments Matched with NoticeToReceive** enquiry shows the incoming payments (in cancelled, reversed, repair, returned, rejected status) that are already matched with expected receipts. It provides an option to manually initiate reversal to separate a matched record.

## Auto Repair

Payments Repair is an automated repair engine that repairs SWIFT payments without manual intervention and helps to increase STP processing. The system is pre-integrated with optional Auto Repair engine to inspect and repair SWIFT Customer and Bank Transfer payments. If repair is configured, then received SWIFT payments (received in MT or MX format) while being processed in STP, are sent to repair tool. Repair is not applicable when payment is initiated from system (for example, Order Entry).

Decision on whether the payment has to be sent to Auto Repair engine for enrichments is based on

- Weights (Programs per weight)
- Auto Repair Instance Static data setup

Payments sent to Auto Repair Engine are parked in status 15 (Transaction Sent to Auto Enrichment Engine) till a response is received from Auto Repair Engine.

When Auto Repair Engine has finished processing the request, it returns either the original information unchanged or returns updated details for some of the provided information along with one or more return codes.

Once the response from repair engine is received, the system performs the following:

- Updates the payment instruction with the new information
  - Through a change of fields for particular changed data fields in individual records
  - Through insertion of new records if created by the Auto Repair Engine
  - Through deletion of existing records if not retained by the Auto Repair Engine
- Updates the auto repair audit trail
- Updates the enrichment history log
  - If enrichment is not performed by repair engine, then log a message to indicate processed and message is not enriched
  - If enrichment is performed by repair engine, then log a message to capture the return codes and indicate message is enriched
- Updates status code of the payment to 20 so that STP sub flow picks it up for further processing

The user can view the enrichment performed on the payment using the **Auto Repair Enrichment** enquiry (accessed through View in Details option). The system provides option to configure conditional fees and deduct charges if a payment is repaired by the engine.

When no response is received within timeout period (configured in company properties), the system automatically updates the status to 20 (that is, sub flow completed) and proceed with payment processing (ignoring any response received later).

Read the [Payments Repair](https://docs.temenos.com/docs/Solutions/Payments/Payments/VS/Payments_Repair/Payments_Repair/Introduction.htm) user guide for more information on repair features.

[Request Response Format](#)

The system communicates with Repair Engine that is, send payment details for enrichments and receive the enriched payment details back.

- Request to Repair Engine: Payment details are sent to repair engine in an xml format using Integration Framework.
- Response from Repair Engine: Response from repair engine is received in a proprietary format over queue (Integration Framework is not used here).

The request XML contains the following five sections for different types of information from the payment:

- Transaction Details
- Debit Party/Agent details
- Credit Party/Agent details
- Information Code
- Additional Information

Similarly, there is a specific response format against each of the sections.

[Transaction Details (from POR.TRANSACTION)](#)

[Request Format](#)

The system sends the following details related to the received payment based on availability. The *FTNumber* and *Company* fields are mandatory and always sent, remaining details are optional and sent if available.

| SL No | Fields | XML tag in request |
| --- | --- | --- |
| 1 | FT Number | ns1:ftNumber |
| 2 | Company | ns1:companyID |
| 3 | Transaction Currency Code | ns1:transactionCurrencyCode |
| 4 | Transaction Amount | ns1:transactionAmount |
| 5 | Message Format | ns1:messageFormat |
| 6 | Sender Address | ns1:senderAddress |
| 7 | Receiver Address | ns1:receiverAddress |
| 8 | Originating Channel | ns1:originatingChannel |
| 9 | Originating Source | ns1:originatingSource |
| 10 | Message Identification  (GrpHdr\ MsgId) | ns1:messageId |
| 11 | Create Date Time  (GrpHdr\ CreDtTm) | ns1:createDateTime |
| 12 | Instruction Priority  (PmtTpInf\InstrPrty) | ns1:instructionPriority |
| 13 | Instruction Identification  (PmtId\ InstrId) | ns1:instructionIdentification |
| 14 | End To End Identification  (PmtId\ EndToEndId) | ns1:endToEndIdentification |
| 15 | Transaction Identification  (PmtId\ TxId) | ns1:transactionIdentification |
| 16 | Instructed Currency  (CdtTrfTxInf\ InstdAmt - currency) | ns1:instructedCurrency |
| 17 | Instructed Amount  (CdtTrfTxInf\ InstdAmt) | ns1:instructedAmount |
| 18 | Record ID | ns1:recordID |

[Response Format](#)

The following is the proprietary response structure for transaction Details section of the request.

```
POR.TRANSACTION{FTNumber||CompanyID||TransactionCurrencyCode||
									TransactionAmount||MessageFormat||SenderAddress||ReceiverAddress||
									OriginatingChannel||OriginatingSource||MessageId||CreateDateTime||
									InstructionPriority||InstructionIdentification||EndToEndIdentification||
									TransactionIdentification||InstructedCurrency||InstructedAmount||
								RecordIDCRLF
```

Copy

[Debit Party/Agent Details (from `POR.SUPPLEMENTARYINFO`)](#)

[Request Format](#)

The system sends the following details for each of the debit party or agent roles present in the received payment. If a debit party/agent role is present, then the *Debit Party Role* field is mandatory and always sent, remaining details are optional and sent if available.

| Fields | New/Existing |
| --- | --- |
| Debit Party Role | ns2:dpRole |
| Debit Party National ID | ns2:dpNationalID |
| Debit Party Identifier Code | ns2:dpIdentifierCode |
| Debit Party Account Line | ns2:dpAccountLine |
| Debit Party Free Line 1 | ns2:dpLine1 |
| Debit Party Free Line 2 | ns2:dpLine2 |
| Debit Party Free Line 3 | ns2:dpLine3 |
| Debit Party Free Line 4 | ns2:dpLine4 |
| Account Number | ns2:dpAccountNumber |
| Name | ns2:dpName |
| Department | ns2:dpDepartment |
| Sub Department | ns2:dpSubDepartment |
| Street Name | ns2:dpStreetName |
| Building Number | ns2:dpBuildingNumber |
| Building Name | ns2:dpBuildingName |
| Floor | ns2:dpFloor |
| Post Box | ns2:dpPostBox |
| Room | ns2:dpRoom |
| Post Code | ns2:dpPostCode |
| Town Name | ns2:dpTownName |
| Town Location Name | ns2:dpTownLocationName |
| District Name | ns2:dpDistrictName |
| Country Sub Division | ns2:dpCountrySubDivision |
| Country | ns2:dpCountry |
| Country Of Residence | ns2:dpCountryOfResidence |
| AddressLine1 | ns2:dpAddressLine1 |
| AddressLine2 | ns2:dpAddressLine2 |
| AddressLine3 | ns2:dpAddressLine3 |
| FinIdClrgSysIdCode | ns2:dpFinIdClrgSysIdCode |
| FinIdClrgSysIdProp | ns2:dpFinIdClrgSysIdProp |
| FinIdClrgSysMemberId | ns2:dpFinIdClrgSysMemberId |
| OrgFinIdLEI | ns2:dpOrgFinIdLEI |
| OrgFinIdOtherId1 | ns2:dpOrgFinIdOtherId1 |
| OrgFinIdOtherSchemeCode1 | ns2:dpOrgFinIdOtherSchemeCode1 |
| OrgFinIdOtherSchemeProp1 | ns2:dpOrgFinIdOtherSchemeProp1 |
| OrgFinIdOtherIssuer1 | ns2:dpOrgFinIdOtherIssuer1 |
| OrgFinIdOtherId2 | ns2:dpOrgFinIdOtherId2 |
| OrgFinIdOtherSchemeCode2 | ns2:dpOrgFinIdOtherSchemeCode2 |
| OrgFinIdOtherSchemeProp2 | ns2:dpOrgFinIdOtherSchemeProp2 |
| OrgFinIdOtherIssuer2 | ns2:dpOrgFinIdOtherIssuer2 |
| Record ID | ns2:recordID |

Following is the list of various debit party/agent roles:

| Debit Party/Agent | Description |
| --- | --- |
| SNDCBK | Sender’s Correspondent / Instructing Reimbursement Agent |
| RCVCBK | Receiver’s Correspondent / Instructed Reimbursement Agent |
| TRMINS | Third Reimbursement Agent |
| PRVINS / PRVIN2 / PRVIN3 | Previous Instructing Agent 1 / 2 / 3 |
| ORDPTY | Ordering Party / Debtor |
| ORDINS | Ordering Institution / Debtor Agent |
| ULTDBT | Ultimate Debtor |
| SENDER | Sender / Instructing Agent |
| INSPTY | Initiating Party |
| CHGPTY, CHGPT2, CHGPT3, CHGPT4, CHGPT5 | Charge Agents (in case of OUR charges) |

IMPDBT role (Implied Debit) is not created as part of initial mapping when payment is received, hence not sent in the request.

[Response Format](#)

Following is the proprietary response structure for Debit Party/Agent details section of the request.

```
POR.PARTYDEBIT{DebitPartyRole||DebitPartyNationalId
									||DebitPartyIdentifierCode
									||DebitPartyAccountLine||DebitPartyFreeLine1
									||DebitPartyFreeLine2||DebitPartyFreeLine3
									||DebitPartyFreeLine4
									||PartyAccountNumber
									||Name||Department||SubDepartment
									||StreetName||BuildingNumber
									||BuildingName||Floor||PostBox
									||Room||PostCode||TownName
									||TownLocationName||DistrictName
									||CountrySubDivision||Country
									||CountryOfResidence||AddressLine1
									||AddressLine2||AddressLine3
									||FinIdClrgSysIdCode||FinIdClrgSysIdProp
									||FinIdClrgSysMemberId||OrgFinIdLEI
									||OrgFinIdOtherId1||OrgFinIdOtherSchemeCode1
									||OrgFinIdOtherSchemeProp1||OrgFinIdOtherIssuer1
									||OrgFinIdOtherId2||OrgFinIdOtherSchemeCode2
									||OrgFinIdOtherSchemeProp2||OrgFinIdOtherIssuer2
								||RecordIDCRLF
```

Copy

[Credit Party and Agent Details (from POR.SUPPLEMENTARYINFO)](#)

[Request Format](#)

The system sends the following details for each of the credit party and agent roles present in the received payment. If a credit party or agent role is present, then the *Credit Party Role* field is mandatory and always sent, remaining details are optional and sent if available.

| Field | New/Existing |
| --- | --- |
| Credit Party Role | ns3:cpRole |
| Credit Party National ID | ns3:cpNationalID |
| Credit Party Identifier Code | ns3:cpIdentifierCode |
| Credit Party Account Line | ns3:cpAccountLine |
| Credit Party Free Line 1 | ns3:cpLine1 |
| Credit Party Free Line 2 | ns3:cpLine2 |
| Credit Party Free Line 3 | ns3:cpLine3 |
| Credit Party Free Line 4 | ns3:cpLine4 |
| Account Number | ns3:cpAccountNumber |
| Name | ns3:cpName |
| Department | ns3:cpDepartment |
| Sub Department | ns3:cpSubDepartment |
| Street Name | ns3:cpStreetName |
| Building Number | ns3:cpBuildingNumber |
| Building Name | ns3:cpBuildingName |
| Floor | ns3:cpFloor |
| Post Box | ns3:cpPostBox |
| Room | ns3:cpRoom |
| Post Code | ns3:cpPostCode |
| Town Name | ns3:cpTownName |
| Town Location Name | ns3:cpTownLocationName |
| District Name | ns3:cpDistrictName |
| Country Sub Division | ns3:cpCountrySubDivision |
| Country | ns3:cpCountry |
| Country Of Residence | ns3:cpCountryOfResidence |
| AddressLine1 | ns3:cpAddressLine1 |
| AddressLine2 | ns3:cpAddressLine2 |
| AddressLine3 | ns3:cpAddressLine3 |
| FinIdClrgSysIdCode | ns3:cpFinIdClrgSysIdCode |
| FinIdClrgSysIdProp | ns3:cpFinIdClrgSysIdProp |
| FinIdClrgSysMemberId | ns3:cpFinIdClrgSysMemberId |
| OrgFinIdLEI | ns3:cpOrgFinIdLEI |
| OrgFinIdOtherId1 | ns3:cpOrgFinIdOtherId1 |
| OrgFinIdOtherSchemeCode1 | ns3:cpOrgFinIdOtherSchemeCode1 |
| OrgFinIdOtherSchemeProp1 | ns3:cpOrgFinIdOtherSchemeProp1 |
| OrgFinIdOtherIssuer1 | ns3:cpOrgFinIdOtherIssuer1 |
| OrgFinIdOtherId2 | ns3:cpOrgFinIdOtherId2 |
| OrgFinIdOtherSchemeCode2 | ns3:cpOrgFinIdOtherSchemeCode2 |
| OrgFinIdOtherSchemeProp2 | ns3:cpOrgFinIdOtherSchemeProp2 |
| OrgFinIdOtherIssuer2 | ns3:cpOrgFinIdOtherIssuer2 |
| Record ID | ns3:recordID |

Following is the list of various credit party/agent roles:

- INDAGT : Instructed Agent
- INTINS / INTIN2 / INTIN3 : Intermediary Agent 1 /2 / 3
- ACWINS : Creditor Agent
- BENFCY or BENINS : Creditor (Customer / Bank Transfer)
- ULTCDT : Ultimate Creditor
- CHGPTY, CHGPT2, CHGPT3, CHGPT4, CHGPT5: Charge Agents (in case of SHA or BEN charges)

IMPCDT role (Implied Credit) is not created as part of initial mapping when payment is received, hence not sent in the request.

[Response Format](#)

Following is the proprietary response structure for Credit Party/Agent details section of the request.

```
POR.PARTYCREDIT{CreditPartyRole||CreditPartyNationalId
									||CreditPartyIdentifierCode||CreditPartyAccountLine||CreditPartyFreeLine1
									||CreditPartyFreeLine2||CreditPartyFreeLine3||CreditPartyFreeLine4
									||PartyAccountNumber||Name||Department||SubDepartment||StreetName
									||BuildingNumber||BuildingName||Floor||PostBox||Room||PostCode||TownName
									||TownLocationName||DistrictName||CountrySubDivision||Country
									||CountryOfResidence||AddressLine1||AddressLine2||AddressLine3
									||FinIdClrgSysIdCode||FinIdClrgSysIdProp||FinIdClrgSysMemberId
									||OrgFinIdLEI||OrgFinIdOtherId1||OrgFinIdOtherSchemeCode1
									||OrgFinIdOtherSchemeProp1||OrgFinIdOtherIssuer1||OrgFinIdOtherId2
									||OrgFinIdOtherSchemeCode2||OrgFinIdOtherSchemeProp2
								||OrgFinIdOtherIssuer2||RecordIDCRLF
```

Copy

[Information Codes (from POR.SUPPLEMENTARYINFO)](#)

[Request Format](#)

The system sends the following details for various information codes present in the received payment.

| Field | New/Existing |
| --- | --- |
| Information Code | ns4:infoCode |
| Information Line Sequence | ns4:infoTypeLineSeq |
| Information Tag | ns4:infoTag |
| Instruction Code | ns4:instrCode |
| Country Code | ns4:countryCode |
| Information Line | ns4:infoLine |
| Record ID | ns4:recordID |

For MT format messages, the information code words and details received in 13C, 23E, 72, 77B and 77T are included.

For MT format messages, the information code words and details received in Instruction for Creditor Agent, Instruction for Next Agent, Purpose, Clearing Chanel, Settlement Priority, Settlement Method, Service Level, Local Instrument, Category Purpose, Settlement Time Indication and Settlement Time are included.

Regulatory reporting information from MX message are not sent in the request. Regulatory reporting data in MX message is different in structure than MT message, hence not stored like information code.

[Response Format](#)

Following is the proprietary response structure for Credit Party/Agent details section of the request.

```
POR.INFORMATION{InformationCode||InformationTypeLineSequence
									||InformationTag||InstructionCode||CountryCode||InformationLine
									||RecordID{InformationCode||InformationTypeLineSequence
									||InformationTag||InstructionCode||CountryCode||InformationLine
								||RecordIDCRLF
```

Copy

[Additional Information Details (from POR.SUPPLEMENTARYINFO)](#)

[Request Format](#)

The system sends unstructured remittance information details present in the received payment.

| Field | New/Existing |
| --- | --- |
| Additional Information Code | ns5:additionalInfCode |
| Additional Information Line Sequence | ns5:additionalInfTypeLineSeq |
| Additional Information Tag | ns5:additionalInfTag |
| Additional Information Line | ns5:additionalInfLine |
| Record ID | ns5:recordID |

Related Remittance Information and Structured Remittance Information details, received in MX format payments, are not sent in the request as it is not used for enrichment.

[Response Format](#)

Following is the proprietary response structure for Credit Party/Agent details section of the request.

```
POR.ADDITIONALINF{AdditionalInformationCode
									||AdditionalInfTypeLineSequence
									||AdditionalInfTag||AdditionalInfLine
									||RecordID{AdditionalInformationCode
									||AdditionalInfTypeLineSequence
									||AdditionalInfTag||AdditionalInfLine
								||RecordIDCRLF
```

Copy

## Debit and Credit Confirmations

Debit and credit confirmation is used to notify the account owner of a debit or credit entry in their account. CBPR+ camt.054 message format is used to generate the debit and credit confirmations and send through SWIFT. The equivalent SWIFT FIN confirmation is MT900 (debit) and MT910 (credit).

The system provide options to configure the generation of debit or credit confirmation at client and bank conditions level. Separate options are available to configure notification message format. If the delivery method is configured as SWIFT, then confirmations are sent using MT900 or MT910 message. If the delivery method is configured as xmliso, then confirmations are sent using CBPR+ camt.054 message. The user can configure the format of the notification to be sent through SWIFT. The BIC address must be configured in order to send these confirmations through SWIFT.

- Confirmation is not generated for file-based clearings when Temenos Payments Hub is deployed in standalone mode.
- For the inward announcement message where the debit accounting is neither LORO nor NOSTRO, though the configuration generates confirmations, the system does not generate confirmations (MT900/camt.054) for the sending bank.
- For the bank transfers where the debit account type is NOSTRO, the system does not generate the MT900 or camt.054 even with confirmations configurations, since it is the mirror of accounts maintained at the other bank.
- When the system initiates the Book Transfer for LTA from RTGS/CLM, Debit/Credit confirmations (camt.054) are generated based on the accounts that have actually been debited or credited in posting lines (not based on the Account derived from settlement account in Account mapping table).

| Payment Direction | Transfer Type | Originating Channel | Clearing Txn Type | OutputChannel | Debit | Credit | Debit camt.054 | Credit camt.054 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Redirect | Customer/Bank | Clearing | NA | SWIFT | Bank | Bank | No | Yes |
| SWIFT | SWIFT | Bank | Bank | Yes | Yes |
| Redirect | Customer/Bank | SWIFT | NA | Clearing | Bank | Bank | Yes | No |
| Outgoing | Customer | NA | NA | SWIFT | Customer | Bank | Yes | Yes |
| Outgoing | Bank | NA | NA | SWIFT | Bank | Bank | Yes | Yes |
| Outgoing | Customer | NA | NA | Clearing | Customer | Bank | Yes | No |
| Outgoing | Bank | NA | NA | Clearing | Bank | Bank | Yes | No |
| Incoming | Customer | SWIFT | NA | LEDGER | Bank | Customer | Yes | Yes |
| Incoming | Bank | SWIFT | NA | LEDGER | Bank | Bank (Account Type ‘V’ is being checked for Credit Side) | Yes | Yes |
| Incoming | Customer | Clearing | NA | LEDGER | Bank | Customer | No | Yes |
| Incoming | Bank | Clearing | NA | LEDGER | Bank | Bank | No | Yes |
| Book | Customer | NA | NA | Book | Customer | Customer | Yes | Yes |
| Book | Customer | NA | NA | Book | Customer/Vostro | Suspense | Yes | No |
| Book | Customer | NA | NA | Book | Suspense | Customer/Vostro | No | Yes |
| Book | Bank | NA | NA | LEDGER | Customer/Vostro | Suspense | Yes | No |
| Book | Bank | NA | NA | LEDGER | Suspense | Customer/Vostro | No | Yes |
| Book | Bank | NA | NA | LEDGER | Customer/Vostro | Customer/Vostro | Yes | Yes |
| Book | Bank | NA | LTA | LEDGER | Customer/Vostro | Suspense | No | Yes |
| Book | Bank | NA | LTA | LEDGER | Suspense | Customer/Vostro | Yes | No |

## Customer Transfer STP (pacs.008 STP)

The system provides multiple options to capture CBPR+ customer transfer:

- Front office users can capture CBPR+ customer transfer using dedicated screen in the `PO` application
- Back office users can capture CBPR+ customer transfer using dedicated screen in Temenos Payments Hub
- Receive a pain.001 file that results in a CBPR+ customer transfer initiation

When the routing channel is decided as LORO or NOSTRO and the company properties is configured to send outward cross-border SWIFT payments in MX format, Temenos Payments Hub process and posts the order, and generates the CBPR+ pacs.008 message after the customer transfer order is captured.

SWIFT supports the following two CBPR+ formats for customer transfer:

- pacs.008.001.08
- pacs.008.001.08\_STP

The STP format (pacs.008.001.08\_STP) is a subset of the normal pacs.008.001.08 message type. The STP format supports less number of fields compared to normal pacs.008 message type in order to enable end-to-end STP processing without manual intervention.

Once customer transfer order is processed and outgoing channel is determined as LORO / NOSTRO (for routing through SWIFT) and format as MX, the system inspects the captured payment data and decides whether to generate a normal pacs.008 or pacs.008\_STP format message. This is applicable for redirect customer payments also.

The system checks the following conditions on the payment data in order to decide if pacs.008 STP message can be sent. If the conditions are not met, the system generates normal pacs.008 message.

| Condition | Description |
| --- | --- |
| Agent Related Condition | There are multiple agent roles in a CBPR+ customer transfer payment order:   - Instructing Reimbursement Agent - Instructed Reimbursement Agent - Third Reimbursement Agent - Charge Agent - Previous Instructing Agent 1 / 2 / 3 - Intermediary Agent 1 / 2 / 3 - Instructing Agent - Instructed Agent - Debtor Agent - Creditor Agent   The name and address related fields should not exist for all these agent roles.  Only the following details can be present for the agent roles:   - BIC - Clearing System Code and Member Identification - LEI   The BIC information is mandatory. |
| Service Level | If the Service Level tag is captured, only sub tag code is allowed. Sub tag proprietary field should not be present. |
| Local Instrument | If the Local Instrument tag is captured, only sub tag code is allowed. Sub tag proprietary field should not be present. |
| Category Purpose | If the Category Purpose tag is captured, only sub tag code is allowed. Sub tag proprietary field should not be present. |
| Purpose | If the Purpose tag is captured, only sub tag code is allowed. Sub tag proprietary field should not be present. |
| Instruction for Creditor Agent | Instruction for Creditor Agent details (such as code, instruction information) should not be present. |
| Instruction for Next Agent | Instruction for Next Agent details (such as instruction information) should not be present. |
| Remittance Information | Only unstructured remittance information can be sent in STP format. Structured remittance information should not be present. |

[Specific Rules for Country Code](#)

The debtor
agent and creditor agent BIC’s are inspected to check the following country
rules. If the debtor and creditor agent falls in these country codes, then Name and IBAN must be present
for Debtor and Creditor for the message to be sent in STP format.

[Rule "Debtor \_ Creditor \_EU\_ Rule"](#)

If Creditor Agent and Debtor Agent BICs are part of following countries:

AT, BE, BG, BV, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GF, GI, GP, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MQ (FR), MT, NL, NO, PL, PM (FR), PT, RE (FR), RO, SE, SI, SJ, SK

then Debtor and Creditor must be identified using a Name and the Account/IBAN.

[Rule "Debtor \_
Creditor \_E S/ AD\_ Rule"](#)

Transactions exchanged within these country couples are considered
as domestic ones. If Creditor Agent and Debtor Agent BICs are part of
following countries: ES, AD

then Debtor and Creditor must be identified using a Name and the
Account/IBAN.

[Rule "Debtor \_ Creditor \_F R/ MC\_ Rule"](#)

Transactions exchanged within these country couples are considered as domestic ones. If Creditor Agent and Debtor Agent BICs are part of following countries: FR, MC

then Debtor and Creditor must be identified using a Name and the
Account/IBAN.

[Rule "Debtor \_
Creditor \_I T/ SM\_ Rule"](#)

Transactions exchanged within these country couples are considered
as domestic ones. If Creditor Agent and Debtor Agent BICs are part of
following countries: IT, SM

then Debtor and Creditor must be identified using a Name and the
Account/IBAN.

[Rule "Debtor \_
Creditor \_I T/ VA\_ Rule"](#)

Transactions exchanged within these country couples are considered
as domestic ones. If Creditor Agent and Debtor Agent BICs are part of
following countries: IT, VA

then Debtor and Creditor must be identified using a Name and the
Account/IBAN.

## Payment Processing Workflow

This section describes the workflow of the outward and inward credit transfers.

[Outward Credit Transfer](#)

This section describes the outward processing flow of an International Credit Transfer Payment order initiated in the system. Credit Transfer can be of type Customer Transfer (CTR) or Bank Transfer (BTR).

/Introduction_32.png)

| Activity | Description |
| --- | --- |
| GUI based manual capture of SWIFT International Payment from front-office (POA) or back-office (Order Entry) | The user captures International payment from the `PO` application or Order Entry (OE) screen. The system provides menu and screens to capture CBPR+ payments.  Validation of mandatory and non-mandatory fields are performed on submission and errors indicated if any. |
| Payment instructions from correspondent bank | Correspondent bank sends payment instructions in electronic format to Temenos Payments Hub bank through SWIFT. The received payment instruction is validated against XSD and mapped into the system. |
| Submission and Supervisor approval | On submission of the payment from GUI, the payment waits for supervisor approval. Once approved, the payment is moved for further processing. If the supervisor rejects the payment, it can be modified and resubmitted for approval. Payment is then sent to Temenos Payments Hub Engine for further processing.  Payments received in Temenos Payments Hub from correspondent banks in STP mode do not wait for supervisor approval. |
| Code and SLA | Once the payment is mapped, weight is determined. SWIFT payments are considered as heavy weight. For STP payments, the system processes the inbound code words and determines SLA based on configurations. |
| Auto Repair | Communicates with auto repair engine to enrich the SWIFT messages received from correspondent banks if interfaced to repair engine. This is bank-specific requirement and is to be undertaken at site.  Temenos Payments Hub solution is pre-integrated with Temenos Auto Repair solution. |
| Direction Determination | The system determines the direction of the payment as Outgoing or Redirect based on where the debtor and creditor accounts are held. |
| Debit Account validations | For outgoing payments created from the `PO` application or OE screen, the system validates if the Ordering Account is valid Temenos Payments Hub Account, it has no posting restrictions and has sufficient balance to cover the transaction.  For redirected payments, the system validates LORO/NOSTRO of the correspondent bank. |
| Debit Client/Bank Condition | The system checks for configured client or bank condition applicable for the payment and applies. |
| Warehouse | Payments with future execution date is warehoused. Warehoused payments are then released on the SOD of the execution date. |
| Duplicate Check | Functional duplicate check is performed if configured. |
| FATF Check | The system performs FATF validations if configured. |
| Routing Determination, RMA Check, Serial/Cover Method, and Channel Validation | Based on the routing product configured, the system determines the routing channel. SWIFT International payments are routed through LORO/NOSTRO/ACCOUNT channel based on the configuration.  Based on the contract configuration, the system determines Serial or Cover method and validates the credit agents.  The system validates if RMA is available to send the message to determined receiver/instructed agent bank.  SWIFT specific format validations are performed on the payment to ensure that the payment meets the compliance requirements.  If RMA does not exist or channel validation fails, the payment is attempted to be routed through an alternate channel (if configured) otherwise payment is moved to repair.  Routing through an alternate channel is available only with ‘PH’ license. |
| Value Date Calculation | The system calculates the payment Value date and Booking date.  If date is in future, the payment is warehoused. |
| Credit Bank Condition | The system checks for configured credit bank condition applicable for the payment and applies. |
| Filtering | The system performs filtering of payments if interfaced to a screening engine. This is bank specific requirement and is to be undertaken at site.  Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Fee Calculation | The system calculates the applicable charges/fees for the payment.  Charge code can be CRED (BEN), SHAR (SHA) or DEBT (OUR) for SWIFT International payments. |
| FX Calculation | Applies when debit account currency and payment currency are different.  If any FX shifts are involved, Value date is adjusted accordingly forward and payment is warehoused. This feature is only supported with ‘PH’ license. |
| Balance Reservation | Reserves funds on the debit account. Balance reservation is done on Payment amount with charges.  If Account Management System (AMS) is T24, then Temenos Payments Hub performs funds reservation in embedded mode, whereas if the AMS is external, it generates fund reservation request in a standard XML format and accepts response from the external system. |
| Posting | Based on the posting product configured, accounting entries are posted.  If Account Management System (AMS) is T24, then Temenos Payments Hub performs debit posting in embedded mode, whereas if the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  Outward Credit Transfer: Entries made before sending customer / Bank transfer   - Debit   - Debtor Account for originating payment   - Correspondent bank Loro/Nostro Account for redirected payment - Credit Loro/Nostro Account of receiver/instructed agent bank - Credit P&L Account for fees/charges (applicable for customer transfer) |
| Outbound Code Word | The system determines the final list of code words to be sent in the outgoing/redirected message. |
| Payment Message Generation | At the end of processing and successful posting, the payment message (pacs.008 or pacs.009 or pacs.009AD or pacs.009 ADV) is generated and sent to delivery. |
| Serial Method | If serial method is identified, then pacs.008/pacs.009 is generated and sent to Receiver Bank through the Delivery module. Delivery layer generates the BAH and technical header to send the message through SWIFT.  Payment is parked in ‘Awaiting acknowledgement’ status.  The system receives SWIFT acknowledgement (through Delivery) and updates the outward payment status. In case of negative SWIFT acknowledgement the outward payment is parked for manual action. |
| Cover Method | If cover method is identified, then pacs.008 or pacs.009ADV is generated and sent to Creditor Agent bank directly through the Delivery module. Delivery layer generates the BAH and technical header to send the message through SWIFT.  Payment is parked in Awaiting acknowledgement status.  The system receives SWIFT acknowledgement and updates the outward payment status. In case of negative SWIFT acknowledgement the outward payment is parked for manual action.  If acknowledgement is positive, then the pacs.009 COV (for customer transfer) /pacs.009 (for pre-advice bank transfer) message is generated and sent to Sender’s Correspondent Bank through the Delivery module.  The system receives SWIFT acknowledgement against the cover and updates the status. |
| Error Queue | If any error is encountered when the international payment is being processed in STP, the transaction is moved to error queue from where the user can repair or cancel the payment. |

**Country Payment Conditions Check**

Temenos Payments Hub performs country-specific validations for a cross-border payment when the payment is classified as ‘I’ (international) and the PSINCV license is installed. Temenos Payments Hub sends the payment details as a request to the Country Payment Conditions module where the country rules are checked against the country code of the Creditor Agent.

If no condition is defined for a country, then the payment processing is continued.

Country payment conditions are validated only for outward credit transfers.

[Derivation of Account Numbers from BIC or NCC for Outward Payments](#)

The user performs the following for deriving the account numbers.

- While initiating the outward bank transfer from the ISO bank transfer initiation screen by entering the *Debit Account Number BIC* field, the system derives the debit account number from the Loro or Nostro table using the entered BIC and the transaction currency. The account number that matches BIC and currency is fetched and populated in the *Debit Account Number* field. When there is no relevant account in the table, an error message is displayed on the screen.
- The users can enter the *Debtor Clearing System ID Code* and *Debtor Clearing System member ID* fields under the Extended Debtor Info tab. The *Clearing System ID* dropdown list displays the values from the PI.ISO.EXTERNAL.CODE table. The user must enter both fields for the system to fetch the account number. If a user leaves one field blank, the system displays an error message on the screen.
- When the user enters the NCC for which BIC can be derived (using SWIFT reference files), the system derives the account number from the Loro or Nostro table as mentioned in the first point.
- When the user enters NCC for which BIC cannot be derived due to one of the following reasons:
  - Derivation of BIC from NCC is not enabled at the company level (PP.COMPANY.PROPERTIES – NoBICbkcdvaldiation is checked).
  - Derivation of BIC from NCC is enabled at the company level but no record is found in the RD.CENTRAL.BANK.DIR table to derive the BIC.
  - Derivation of BIC from NCC is enabled at the company level but no BIC is available for the NCC in the RD.CENTRAL.BANK.DIR table (banks that operate only on NCC and don’t have BIC).
- The system fetches the debit account number from PP.CLEARINGCORRESPONDENTS table and populates the same in the Debit account number field. Read the [Configuration](Configuration.htm#NCC) section to know more about configuring the account number in the PP.CLEARINGCORRESPONDENTS table.
- When the user enters both BIC and NCC, then the system gives preference to BIC and derives the account number as mentioned in the first bullet point.
- When the user enters the *Debit Account Number* and *NCC* fields, then no derivation happens, the system tries to process the payment with the user-entered debit account number, and the user-entered NCC gets stored as part of the transaction and emitted out as part of the outgoing message.
- When the outgoing payment is moved to the repair queue with Debtor NCC details, the user can modify these details from the repair screen but fetching of account number from NCC is not performed in the repair screen. The modified NCC details are stored as part of the transaction and emitted as part of the outgoing message.

[Inward Credit Transfer](#)

This section describes the inward processing flow of an International Credit Transfer Payment order received in the system, where the creditor account is held in processing bank’s book. Credit Transfer can be of Customer Transfer (CTR) or Bank Transfer (BTR) type.

/Introduction_33.png)

| Activity | Description |
| --- | --- |
| Validation and Mapping | Correspondent bank sends payment instructions to Temenos Payments Hub bank through SWIFT. Delivery layer receives the payment and forward to Temenos Payments Hub. Temenos Payments Hub receives the payment, validates format and maps for processing the payment in STP mode. |
| Code and SLA | Once the payment is mapped, weight is determined. SWIFT payments are considered as heavy weight. For STP payments, the system processes the inbound code words and determines SLA based on configurations. |
| Direction Determination | The system determines the direction of the payment as Incoming if the creditor account is in processing bank’s book. |
| Debit Account validations | The system determines the debit account (LORO/NOSTRO of instructing agent) and validates if the account is valid T24 Account. |
| Hold for Cover | If hold for cover feature is enabled, then the system tries to match the incoming payment or cover with the expected receipts module. If matching is not successful, payment is parked.  In case of bank transfer pre-advice (pacs.009 ADV), hold for cover configuration is always considered as cover. Payment will be parked in hold for cover queue always. |
| Debit Client/Bank Condition | The system checks for configured client or bank condition applicable for the payment and applies. |
| Warehouse | Payments with future execution date is warehoused. Warehoused payments are then released on the SOD of the execution date. |
| Duplicate Check | Functional duplicate check is performed if configured. |
| FATF Check | The system performs FATF validations if configured. |
| Credit Account Validation | The system determines the credit account and validates if the account is valid T24 Account, it has no posting restrictions. |
| Value Date Calculation | The system calculates the payment Value date and Booking date.  If date is in future, the payment is warehoused. |
| Credit Bank Condition | The system checks for configured credit bank condition applicable for the payment and applies. |
| Filtering | The system performs filtering of payments if interfaced to a screening engine. This is bank specific requirement and is to be undertaken at site.  Temenos Payments Hub solution is pre-integrated with Temenos FCM solution. |
| Fee Calculation | The system calculates the applicable charges/fees for the payment.  Charge code can be CRED (BEN), SHAR (SHA) or DEBT (OUR) International SWIFT payments. |
| FX Calculation | Applies when credit account currency and payment currency are different.  If any FX shifts are involved, Value date is adjusted accordingly forward and payment is warehoused. This feature is only supported with ‘PH’ license. |
| Posting | Based on the posting product configured, accounting entries are posted.  If Account Management System (AMS) is T24, then Temenos Payments Hub performs debit posting in embedded mode, whereas if the AMS is external, it generates posting request in a native XML format and accepts response from the external system.  Entries made after processing incoming customer / Bank transfer   - Debit Loro/Nostro Account of sender/instructing agent bank - Credit the creditor/beneficiary Account mentioned in payment - Credit P&L Account for fees/charges (applicable for customer transfer) |
| Error Queue | Errors when the international payment is being processed, the transaction is moved to error queue from where user can repair or cancel the payment. |

[Derivation of Account Numbers from BIC or NCC for Inward Payments](#)

When an Incoming bank transfer is received from any clearing or through the SWIFT network into TPH, the system checks the creditor tag.

- If the creditor tag is present with BIC, the system compares the BIC with its own processing company BIC.
  - If there is a match, the system updates the direction of the payment as Incoming and tries to credit the account that is received in the payment message. If no account is received in the payment message, then the payment is parked in the repair queue since the system is not aware of the account to credit for the transaction.
- If there is no match, the system tries to derive the account from the Loro or Nostro table and update.
  - If both the Loro and Nostro accounts are present, then the system updates the direction as Incoming and credits the Loro account.
  - If only the Nostro account is present in the Loro or Nostro table, then the system updates the direction as Redirected and redirects the message.
  - If only the Loro account is present, then the system updates the direction as Incoming and credits the Loro account.
  - If no account is present, then the system parks the payment in the repair queue.
- If the creditor tag is present with NCC for which BIC can be derived, then the same logic applies as mentioned above.
- If the creditor tag is present with NCC for which BIC cannot be derived, the system compares the received NCC with the own company NCC (PP.COMPANY.PROPERTIES).
  - If there is a match, the system updates the direction of the payment as Incoming and tries to credit the account that is received in the payment message. If there is no account received in the payment message, then the system parks the payment in the repair queue since the system is not aware of the account to credit for the transaction.
  - If there is no match, the system tries to derive the account for NCC from the PP.CLEARINGCORRESPONDENTS table and updates the direction of the payment as Incoming. The system processes the payment by crediting the derived account number. If there is no entry in this table, the system updates the direction of the payment as Redirected. Read the [Configuration](Configuration.htm#NCC) section to know more about configuring the account number in the PP.CLEARINGCORRESPONDENTS table.

When an incoming payment with creditor NCC or BIC moves to the repair queue, the system displays the received details on the screen and the user cannot edit the received details from the repair queue. Once the payment is submitted from the repair queue, the system stores the received NCC as part of the transaction and the user can view from the Pending and Processed enquiry.

[](#)[Channel Validation](#)

When the user captures and processes an outward payment in Temenos Payments Hub, as part of routing and settlement, the system tries to determine the routing channel. While determining a channel, the system performs channel validations to validate whether the underlying payment object conforms to the messaging requirements of the destination channel. The system performs the same channel validations even for redirected payments, payments initiated from the `PO` application and pain.001. If the channel validation fails, then based on routing configuration, the system either checks the next channel or moves the payment to the repair queue.

The following are the two channel validations performed for ISO20022 based payments (SWIFT CBPR+, MX based clearing such as TARGET2):

- Common Validations : These are standard validations that are applicable for all ISO20022 based messages.

  If Nobicbkcdvalidation in PP.CLEARING or PP.COMPANY.PROPERTIES is set as Y, then validating the BIC against RD.CENTRAL.BANK.DIR is skipped as part of common validations.
- Specific Validations : These are additional validations (on top of common validations) that are specific to the determined channel (CBPR+ or Clearings which are configured as MX such as TARGET2 and so on) and are not applicable for others.

The Channel validations are performed only for the following MX payment types:

- Customer Transfer (which results in pacs.008)
- Bank Transfer (which results in pacs.009)
- Return Payment (which results in pacs.004)

When a customer payment is captured which is settled through cover, the same payment object is first checked for customer transfer validations followed by the bank transfer validations. The system does not perform separate validations for the underlying credit transfer block of the pacs.008 announcement.

When a cover is received and redirected , the bank transfer part of the message is validated but no separate validation is performed for Underlying Credit Transfer section (as this information is saved as a BLOB and attached as it is in the redirected message).

The system does not perform any separate channel validation for the individual elements of structured remittance information. When structured remittance information is received in pain.001 or as an incoming message, it is saved as a BLOB and attached to the generated outgoing or redirected message.

[Customer Transfers (pacs.008)](#)

Given below are the Common Validations and CBPR+ Specific Validations for Customer Transfers (pacs.008).

[Common Validations](#)

The following table lists the common channel validations performed for all ISO20022 (MX) based on customer transfers (pacs.008) including CBPR+:

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
| If either of Structured or Hybrid Postal Address details are provided, name of the party role should be provided | Name and Structured Address (at least Town Name and Country) or Hybrid Address should be present for <<party role>>  Given below are the list of Party Roles:  SNDCBK, RCVCBK, TRMINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, CHGPTY, CHGPTY2, CHGPT3, CHGPT4, CHGPT5, RECVER,ULTDBT, INSPTY, ORDPTY |
| Maximum three occurrences of service level (code and/or proprietary) information can be provided | Maximum 3 entry of service level is allowed |
| If Local Instrument information is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Local Instrument |
| If Category Purpose information is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Category Purpose |
| If Transaction Purpose information is provided, both code and proprietary should not be provided at the together | Either Coded or Proprietary form can be present for Transaction Purpose |
| If Account Identification scheme related information is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Account Identification Scheme for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENFCY, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Account Type for the party role is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Account Type for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENFCY, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Account Proxy Type for the party role is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Account Proxy Type for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENFCY, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Organisation Identification Scheme for the party role is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Organisation Other Identification Scheme for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| If Private Identification Scheme for the party role is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Private Other Identification Scheme for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| Both Organisation Identification related information and Private Identification related details should not be provided together | Either Organisation identification or Private identification can be present for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| The PayCreditorByCheque (CHQB) and HoldCashForCreditor (HOLD) codes are not allowed together in the Instruction for Creditor Agent field | If Instruction for Creditor Agent is CHQB, HOLD is not allowed as another code |
| The Telecom (TELB) and PhoneBeneficiary (PHOB) codes are not allowed together in the Instruction for the Creditor Agent field | If Instruction for Creditor Agent is "PHOB", "TELB" is not allowed as another code |
| If Clearing System Member Id is provided, either Clearing System Code or Clearing System Proprietary should be provided | If Clearing Member Identification is present, then clearing system id or proprietary must be present for <<party role>>  Given below are the list of Party Roles:  ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, CHGPTY, CHGPTY2, CHGPTY3, CHGPTY4, CHGPTY5 |
| The same code  should not be repeated when the Instruction for Creditor Agent is provided | Same code word should not be repeated for Instruction for Creditor Agent. |
| If the Organisation Identification details are provided, either the scheme code or scheme proprietary information should be provided | When Organisation Other Identification is provided, Identification is mandatory for <<Party Role>>.  Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| Private Identification should be provided if any of private scheme code, scheme proprietary, or issuer details are provided | When Private Other Identification is provided, identification is mandatory for <<Party Role>>. Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| If any of the details of birth, such as Date, Province of birth, City of birth, Country of birth are provided, Birth date, City of Birth and Country of Birth should be provided | - BirthDate should be present when CityOfBirth and CountryOfBirth are present for <<Party role>> - CityOfBirth should be present when BirthDate and CountryOfBirth are present for <<Party role>> - CountryOfBirth should be present when BirthDate and CityOfBirth are present for <<Party role>>   Given below are the list of Party Roles:  ORDPTY, BENFCY, ULTDBT, ULTCDT, INSPTY |
| End-to-End Identification of the payment should not start or end with “/” and should not contain “//” | End-to-End Identification should not have "/" as 1st and 16th character and no "//" up to 16th character |
| Service level code should be valid as per the ISO External Code list | Invalid Service Level Code - <code> |
| Local instrument code should be valid as per the ISO External Code list | Invalid Local Instrument Code - <List the code> |
| Category purpose code should be valid as per the ISO External Code list | Invalid Category Purpose Code - <List the code> |
| Purpose code should be valid as per the ISO External Code list | Invalid Purpose Code - <List the code> |

[CBPR+ Specific Validations](#)

The following table lists the CBPR+ specific validations performed for customer transfers (pacs.008):

| Validation | Error Description |
| --- | --- |
| The following payment currencies are not allowed:   - XAU - XAG - XPD - XPT | The Interbank Settlement Currency must not contain the value XAU, XAG, XPD and XPT |
| For an ultimate debtor, Name and Structured Postal address details (at least country and town name) should be provided | Name and Postal Address,Town Name plus Country, or an Address Line must be present for ULTDBT |
| If debtor BIC is not provided, the name of the debtor should be provided. | Debtor Name must be present when BIC is absent for ORDPTY |
| If creditor BIC is not provided, the name of the creditor should be provided | Creditor Name must be present when BIC is absent for BENFCY |
| For an ultimate debtor, the Name, Postal Address, and Country details should be provided | Ultimate Creditor – Name and Postal Address (at least Country) must be present for ULTCDT |
| Debtor Organization scheme proprietary option is not allowed for identification | Scheme code proprietary is not allowed for Debtor Org Id or Other Id |
| Debtor Private scheme proprietary option is not allowed for identification | Scheme code proprietary is not allowed for Debtor Org Id or Other Id |
| If Debtor is identified as an organization, then the scheme code must be provided | If Organisation Other Identification is provided, scheme Code must be provided for ORDPTY |
| If Debtor is identified as a private, then the scheme code must be provided | If Private Other Identification is provided, scheme Code must be provided for ORDPTY |

[Bank Transfers (pacs.009)](#)

Given below are the Common Validations and CBPR+ Specific Validations for Bank Transfers (pacs.008).

[Common Validations](#)

The following table lists the common channel validations performed for all ISO20022 (MX) based bank transfer payments (pacs.009) including CBPR+:

| Validation | Error Description |
| --- | --- |
| The details of first Previous Instructing Agent Account are allowed only if first Previous Instructing Agent is present | Intermediary agent institution information must be present when Intermediary agent account is present |
| The details of second Previous Instructing Agent Account are allowed only if second Previous Instructing Agent is present | 2nd Intermediary agent institution information must be present when 2nd Intermediary agent account is present |
| The details of third Previous Instructing Agent Account are allowed only if third Previous Instructing Agent is present | 3rd Intermediary agent institution information must be present when 3rd Intermediary agent account is present |
| The second Intermediary Agent details are only allowed if first Intermediary Agent is present | If 2nd IntermediaryAgent is present, then 1st IntermediaryAgent must be present |
| The third Intermediary Agent details are only allowed if second Intermediary Agent is present | If 3rd IntermediaryAgent is present, then 2nd IntermediaryAgent must be present |
| The first Previous Instructing Agent Account details are allowed only if first Previous Instructing Agent is present | 1st Previous Instructing agent institution information must be present when 1st Previous Instructing agent account is present. |
| The second Previous Instructing Agent Account details are allowed only if second Previous Instructing Agent is present | 2nd Previous Instructing agent institution information must be present when 2nd Previous Instructing agent account is present |
| The third Previous Instructing agent details are allowed only if the third Previous Instructing agent account is present | 3rd Previous Instructing agent institution information must be present when 3rd Previous Instructing agent account is present |
| The second Previous Instructing Agent details is allowed only if the first Previous Instructing Agent details are present | If 2nd Previous Instructing Agent is present, then 1st Previous Instructing Agent must be present |
| The third Previous Instructing Agent details is allowed only if the second Previous Instructing Agent details are present | If 3rd Previous Instructing Agent is present, then 2nd Previous Instructing Agent must be present |
| If BIC is provided, it should be valid | Invalid Financial Institution BIC for <<party role>>  Given below are the list of Party Roles:  ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, ORDPTY, BENINS, RECVER |
| If Postal Address Country is provided, it should be a valid country code | Invalid Postal Address Country for <<party role>>  Given below are the list of Party Roles:  ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3, ORDPTY, BENINS |
| If Account Currency is provided, it should be a valid currency code | Invalid Agent Account Currency for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN1, PRVIN2 |
| Maximum of only three entries of service level code or proprietary information can be provided | Maximum three entry of service level is allowed |
| If Local Instrument information is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Local Instrument |
| If Category Purpose information is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Category Purpose |
| If Transaction Purpose information is provided, both code and proprietary should not be provided together | Either Coded or Proprietary form can be present for Purpose |
| If Account Identification Scheme related information is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Account Identification Scheme for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Account Type for the party role is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Account Type for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If Account Proxy Type for the party role is provided, both code and proprietary should not be provided together. | Either Coded or Proprietary form can be present for Account Proxy Type for <<party role>>  Given below are the list of Party Roles:  ORDPTY, BENINS, ORDINS, ACWINS, INTINS, INTIN2, INTIN3, PRVINS, PRVIN2, PRVIN3 |
| If either of Structured or Hybrid Postal Address information is provided, name should be provided for the party role | Name and Structured Address (at least Town Name and Country) or Hybrid Address should be present for <<party role>>  Given below are the list of Party Roles:  PRVINS, PRVIN2, PRVIN3, RECVER, INTINS, INTIN2, INTIN3, ORDPTY, ORDINS, ACWINS, BENINS |
| If Structured Postal Address details are provided, Town Name and Country are mandatory | For structured Postal Address, Town Name and Country must be present for <<party role>>  Given below are the list of Party Roles:  PRVINS, PRVIN2, PRVIN3, RECVER, INTINS, INTIN2, INTIN3, ORDPTY, ORDINS, ACWINS, BENINS |
| Both Name and either of Postal Address structured (minimum of town name and country) or Hybrid Address (address lines) should be provided for ordering customer | Name and Either Structured or Hybrid Address should be present for the Ordering Customer record |
| The same code should not be repeated for instruction for creditor agent | Same code word should not be repeated for Instruction for Creditor Agent. |
| End to End Identification of the payment should not start or end with “/” and should not contain “//” | End to End identification cannot start or end with "/" and should not contain "//" |

[CBPR+ Specific Validations](#)

The following table lists the CBPR+ specific validations performed for bank transfers (pacs.009):

| Validation | Error Description |
| --- | --- |
| The following payment currency codes are not allowed:   - XAU - XAG - XPD - XPT | Currency code XAU, XAG, XPD and XPT are not allowed |
| Name and either Structured Postal Address (minimum Country and Town name) or Hybrid Address (address lines) of the party role should be provided | If BIC is absent, Name and Structured Address (at least Country & Town Name) or Hybrid Address must be present for <<party role>>  Given below are the list of Party Roles: PRVINS, PRVIN2, PRVIN3, RECVER, INTINS, INTIN2, INTIN3, ORDPTY, ORDINS, ACWINS, BENINS |

## Supporting Configuration of Message Interface

The widely used network for CBPR+ messages is SWIFT Interact, which is currently supported by Delivery Module out of the box. But the bank can decide to use different network such as Managed File Transfer (MFT). The technical header in the outward message varies for each interface. Hence, Temenos Payments Hub can configure the network to route CBPR+ messages at individual correspondent bank level (BIC or Account). When the payment is to be routed through the correspondent banks in CBPR+ format, the system refers to the configuration and stores this information in the transaction, which would be later passed to the DE layer. The DE layer is responsible for creating technical header based on the network. Refer to the [Configuration](Configuration.htm) section for more information.

## CNY to CNH Currency Conversion

Banks located in China use CNY currency for transactions and the banks located outside China use CNH (Offshore Chinese Yuan) currency for trading purposes. However, CNY is the ISO currency code supported by SWIFT network.

Temenos Payments Hub support the conversion of CNY to CNH currency for incoming payments and non-payment messages based on the company-level requirements. Refer [Configuring CNY to CNH Currency Conversion](Configuration.htm#Config_CNY_CNH) section for details.

Since SWIFT network accepts messages only in CNY currency, any outgoing and redirected CBPR+ messages processed in CNH currency are converted to CNY before being sent out to the SWIFT network.

In this topic

- [Introduction to SWIFT MX](#IntroductiontoSWIFTMX)

- [Co-existence of MT and MX Format for SWIFT Cross Border Payments](#CoexistenceofMTandMXFormatforSWIFTCrossBorderPayments)
- [Message Types](#MessageTypes)
- [Related Features](#RelatedFeatures)
- [Payment Types](#PaymentTypes)
- [Payment Direction](#PaymentDirection)
- [Configurable Support for SWIFT MT or MX format to Send Cross Border Payments](#ConfigurableSupportforSWIFTMTorMXformattoSendCrossBorderPayments)
- [CBPR+ Payment Capture](#CBPRPaymentCapture)
- [CBPR+ Payment Repair](#CBPRPaymentRepair)
- [SWIFT CBPR+ Message Structure](#SWIFTCBPRMessageStructure)
- [Message Elements Supported in SWIFT CBPR+ Payments](#MessageElementsSupportedinSWIFTCBPRPayments)
- [Supported Characters in ISO Message](#SupportedCharactersinISOMessage)
- [Data Enrichment for MT and MX Format Conversion](#DataEnrichmentforMTandMXFormatConversion)
- [BIC Directory](#BICDirectory)
- [Code Word](#CodeWord)
- [Duplicate Check](#DuplicateCheck)
- [Warehousing](#Warehousing)
- [Forex (FX)](#ForexFX)
- [Payment Product for Processing SWIFT Payments](#PaymentProductforProcessingSWIFTPayments)
- [Filtering (Sanction Screening)](#FilteringSanctionScreening)
- [Booking](#Booking)
- [Charge Processing](#ChargeProcessing)
- [FATF Regulation](#FATFRegulation)
- [Relationship Management (RMA)](#RelationshipManagementRMA)
- [Unstructured Address Mapping](#UnstructuredAddressMapping)
- [Direct and Cover Processing](#DirectandCoverProcessing)
- [Routing SWIFT International Payments](#RoutingSWIFTInternationalPayments)
- [Acknowledgements for ISO20022 Messages](#AcknowledgementsforISO20022Messages)
- [Technical Acknowledgement Processing](#TechnicalAcknowledgementProcessing)
- [Payment Status Report (Business Acknowledgement) Processing](#PaymentStatusReportBusinessAcknowledgementProcessing)
- [Customer Payment Status Report Processing](#CustomerPaymentStatusReportProcessing)
- [Returning or Rejecting a Received International Payment](#ReturningorRejectingaReceivedInternationalPayment)
- [Processing Received Return Payment](#ProcessingReceivedReturnPayment)
- [Notification to Receive](#NotificationtoReceive)
- [Notification of Correspondence](#NotificationofCorrespondence)
- [Matching with Expected Receipts](#MatchingwithExpectedReceipts)
- [Auto Repair](#AutoRepair)
- [Debit and Credit Confirmations](#DebitandCreditConfirmations)
- [Customer Transfer STP (pacs.008 STP)](#CustomerTransferSTPpacs008STP)
- [Payment Processing Workflow](#PaymentProcessingWorkflow)
- [Supporting Configuration of Message Interface](#SupportingConfigurationofMessageInterface)
- [CNY to CNH Currency Conversion](#CNYtoCNHCurrencyConversion)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:50:39 PM IST