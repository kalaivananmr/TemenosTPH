# Introduction to SWIFT MX Claims and Charges

> Source: https://docs.temenos.com/docs/Solutions/Payments/International_Payments/PPSWCL/International_PaymentsCBPR/PPSWCL/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   SWIFT MX Claims and Charges > Introduction

- SWIFT MX Claims and Charges;)
  - [Introduction](../../International_PaymentsCBPR/PPSWCL/Introduction.htm)
  - [Configuration](../../International_PaymentsCBPR/PPSWCL/Configuration.htm)
  - [Working with](../../International_PaymentsCBPR/PPSWCL/Workingwith.htm)
  - [Tasks](../../International_PaymentsCBPR/PPSWCL/Tasks.htm)
  - [Outputs](../../International_PaymentsCBPR/PPSWCL/Outputs.htm)

Payments

# Introduction to SWIFT MX Claims and Charges

Updated On 22 March 2025 |
 47 Min(s) read

Feedback
Summarize

The Cross-Border Payments and Reporting Plus (CBPR+) working group defines the MX message formats and usage guidelines (available in the SWIFT CBPR+ portal).

Temenos Payments Hub supports the processing of cross-border international payments using SWIFT MX (ISO20022) messages. This guide explains the processing of the Charges Payment Request and Charges Payment Notification.

## Message Types

Temenos Payments Hub supports SWIFT MX (ISO20022) messages and workflows related to cross-border payments under a licensable module (PPSWMX).

In addition to the SWIFT MX license, the bank must also have a PPSWCL license to accept and send Charge Payment Request messages in ISO format from and to SWIFT. Similarly, under the same PPSWCL license, the bank can receive and accept Charges Payment Notification messages as well.

The following table lists the SWIFT CBPR+ messages supported by Temenos Payments Hub for Charges Payment Request and Charge Payments Notification.Read [SWIFT MX](../../../PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm) for more information.

| ISO20022 MX Message | Payment Order Type | MT Equivalent | Module Code | Outward | Inward | Redirect | Business Service |
| --- | --- | --- | --- | --- | --- | --- | --- |
| camt.106.001.02 | Charge Payment Request | MT191 | PPSWMX  PPSWCL |  |  | x | swift.cbprplus.01 |
| camt\_105\_001\_02 | Charges Payment Notification | MT190 | PPSWMX PPSWCL | x |  | x | swift.cbprplus.01 |

## Charge Payment Requests

The processing of outgoing and incoming charge payment requests are explained below. Following are the charge payment requests message types:

- camt.106 (Single) is MX equivalent of MT191/291
- camt.106 (Multiple) is MX equivalent of MT191 and MT199

camt.106 is the charges payment request message sent by a financial institution to another financial institution to request the payment of charges, interest and/or other expenses which are previously unknown to the receiver.

The business workflow and the processing workflow of charge payment request (camt.106) in the Temenos Payments Hub System is explained below.

[Message Workflow of Charge Payment Requests](#)

The diagram given below depicts the business workflow for single and multiple charge payment request and the source is SWIFT.



Business Workflow for Single and Multiple Charge Payment Request

Agent A sends a Business Message, such as a Customer Credit Transfer (pacs.008) message to Agent B indicating charge wil be born by the Debtor.

Agent B may use the Charges Payment Request message to request an amount of charges related to an underlying business message. This request is settled using the Financial Institution Credit Transfer message (pacs.009).

[Mapping Correlation between MT191 and camt.106](#)

Below image illustrates the mapping correlation between MT191 and camt.106 and the source is SWIFT.




Mapping Correlation between MT191 and camt.106

|  |  |
| --- | --- |
| Charges/ Per Transaction/ Charges Identification | Field 20 Transaction Reference Number |
| Charges/ Per Transaction/ Underlying Transaction | Field 21 Related Reference |
| Charges/ Per Transaction/ Record/ Total Charges per Record/ Total Charges | Filed 32B Currency Code, Amount |
| Group Header, Charges Account Agent or Charges/ Per Transaction/ Record/ Debtor Agent | Filed 52 Ordering Institution |
| Charges/ Per Transaction/ Record/ Charges Breakdown | Field 71B Details of Charge |
| Charges/ Per Transaction/ Record/ Instruction for Instructed Agent | Field 72 Sender to Receiver Information |

[Message Flows between Agents](#)

Below image represents the message flow between agents for the underlying transaction which is settled serially and the source is SWIFT. The Instructed Agent request a charge using the camt.106, following pacs.008 with Charge Bearer DEBT.




High Level First Intermediary Agent Charges Payment Request

|  |  |
| --- | --- |
|  | Debitor Agent (A) initiates a serial payment (with charge bearer DEPT) towards the creditor agent (D) using B and C as intermediators |
|  | Agent B requests that the Debtor pays a charge for processing the payment. Agent B sends this request to the Debtor's bank (Debtor Agent) |
|  | Agent A settles the Charges Request Payment by executing a pacs.009 quoting the Charges Identification references as in the end-to-end identifier of the payment, together with new UETR |

Below image represents the message flow between agents for the underlying transaction which is settled through cover method. The Instructed Agent may request a charge using the camt.106, following pacs.008 with Charge Bearer DEBT.




High Level Direct and Cover payment Creditor Agent Charges Payment Request

|  |  |
| --- | --- |
|  | Debitor Agent (A) initiates a payment (with charge bearer DEPT) using the cover method to the creditor agent (D) |
|  | Creditor Agent B requests that the Debtor (DEBT) pays a charge for processing the payment. Agent D sends this request to the Debtor's bank (Debtor Agent) |
|  | Agent A settles the Charges Request Payment by executing a pacs.009 towards Agent D quoting the Charges Identification references as in the end-to-end identifier of the payment, together with the new UETR |
|  | Agent B processes the payment on Agent C through the Payment Market Infrastructure |
|  | Payment Market Infrastructure settles the payment between Agent B and Agent C as a direct participants of the Market Infrastructure |
|  | Agent C receives the payment and credits the account of Agent D |

### High-Level Structure Details of camt.106

Given below are the tag elements in camt.106.

[Charges Requestor](#)

The Charges Requestor element identifies the agent that is requesting the charge and the receiver who receives the charge amount in a successfully settled charges request. The agent is not necessarily the sender of the message. The charges requestor becomes the creditor in pacs.009 that is used to successfully settle the charges payment request.

The user configures *ClaimBeneficiaryBIC* at the company level with the valid financial institution BIC. This field indicates the bank sending out the claim to receive the fund, if this financial institution is different from the bank that is sending out the claim request. This is an optional field.

[Charges Identification](#)

The Charges Identification element captures the unique reference associated with the charges request used by the charges requestor to reconcile the payment (settlement) of charges payment request. It can be considered equivalent to the Transaction Reference Number (Field 20) of the legacy MT charge messages.

[Charges >> Per Transaction >> Record](#)

The Per Transaction nested element captures the details of charges being requested for the underlying transaction and as necessary breakdown of the charge being requested. The record indicates the number of transactions for which the charge payment request is sent to the correspondent bank.

In a single charge payment request, the number of record can be one whereas in multiple charge payment requests, the number of records can be many and there is no upper limit set as part of the SWIFT specification. Each record has an unique ‘Record ID’ that identifies the record of the charges and it is used for reconciliation purposes. The record ID tag is not present for a single request.

The following are the sub tags.

[Underlying Transactions](#)

Identifies the underlying transaction by providing the ability to capture references from the underlying business message or transaction that is related to the charges payment request. The subtags include Message Identification, Message Name Identification, Instruction Identification, End to End Identification, UETR, and so on.

[Total Charges Per Record](#)

Identifies the total charges applied for the transaction. This number should be equal to the number of charges breakdown items.

[Charges Breakdown Items](#)

Provides a detailed breakdown of total charges based on the charge type. This tag contains ‘Amount’, and ‘CreditDebitIndicator’ which have a fixed value of 'DBIT' and Type.

The Amount tag specifies only the charges that are due from the correspondent bank. If the charges are already received as part of the transaction but it is less than the charge amount then this tag specifies only the due amount and not the received amount.

For every charge applied for the transaction, there is a separate entry of charges breakdown items in the outgoing charges payment request messages.

Any charges that are applied for the transaction other than manual repair are specified with the type as DEBT in the charges breakdown tag.

When the underlying transaction is processed from the repair queue, manual repair charges are applied for the transaction. In such cases, the charge type is specified as NSTP in the charges breakdown tag.



Example of Charges Breakdown Information

[Instruction for Instructed Agent](#)

Captures the instruction for the receiver of the charges payment request where the information is additionally qualified with a code. The information and the codeword (PBEN – Pay Beneficiary) is defaulted by the system and the user cannot change these details.

## Processing Workflow of Outgoing Charge Payment Request

This section explains the processing workflow of the outgoing charge payment request message for the underlying Incoming or redirected transaction.

[Determination of Charges due from Sending Bank](#)

On receiving the incoming payment or redirected payment with the charge option as DEBT, the system determines the charges due from the sending bank based on the charges agreement with the correspondent bank.

Read [Fees and Billing](../../../../Payments/PP/Payments_Hub_(PP)/Fees_and_Billing/Introduction.htm) user guide document.

[Charges Payment Request Message Generation](#)

The outward charges payment request message is generated based on the bank claims agreement configuration. The configuration is set up based on the correspondent’s bank preference.

In addition to the SWIFTMX license, the bank must have a PPSWCL license for configuring ‘Claim Type’ as camt.106 in the bank agreement table. Read [Fees and Billing](../../../../Payments/PP/Payments_Hub_(PP)/Fees_and_Billing/Introduction.htm) for more information on the configuration of the bank’s preference for claim requests.

[Charges Payment Request for Clearing Message](#)

On receiving the underlying transaction from clearing with DEBT or OUR charge option, the charges determination process are same for clearing payment as well but the charge payment request message is sent to the receiving bank through the SWIFT network. As per SWIFT CBPR guidelines, it is mandatory to populate the Instruction Identification of the underlying transaction in the charge payment request.

Instruction Identification of clearing payment can have 35 characters whereas as per SWIFT guidelines, the Instruction Identification tag can contain only 16 characters. So, in this scenario of sending camt.106 for clearing payment, if the Instruction ID tag contains more than 16 characters then in the claim message only ‘15 characters with + sign’ is populated to avoid negative error from the SWIFT network.

[Determination of Message Type for Outgoing Charge Payment Request](#)

Once camt.106 is configured as a Claim Type in the bank claims agreement table, the system performs the following validations to check if the ISO message can be exchanged with the bank.

- Processing bank is SWIFTMX enabled based on the configuration (SWFMXEffectiveDate) in COMPANY properties.
- Current year is greater than or equal to the SWIFT MX Release Year for Charges Payment Request. The user has to configure the corresponding SWIFT.PARAMETER record with the appropriate release year for charge payment request. Read [Configuration](Configuration.htm) for more information.

If any of the above validation fails, the Close of Business (COB) does not pick up the record for processing and hence the claim transaction is not created. In addition to the above validation, the system also checks the existence of an Relationship Management (RMA) between the Temenos Payment Hub (TPH) bank and the receiver of the charge payment request message.

If there is no RMA, the system creates the claim transaction and routes the camt.106 charge payment request message to repair queue with a warning message as ‘RMA doesn’t exist with an Instructed Agent for sending camt.106 message'. Read [Working with](Workingwith.htm) section for more information.

If the user accepts the warning and submits the payment from the repair queue, the claim transaction continues with processing. Once the accounting entries are raised, the camt.106 messages get generated and sent SWIFT.

[Delivery of Charge Payment Request Message to SWIFT](#)

The ISO charge payment request message (camt.106) gets routed to the SWIFT network through the Delivery module. Once camt.106 is routed to SWIFT, the system updates the status of the claim transaction as follows based on whether acknowledgment or Delivery Notification (DLN) is received (based on configuration).

| Status of camt.106 when message is emitted | Ack Req (BFW API) | DLN Req (BFW API) | Status update |
| --- | --- | --- | --- |
| Charge Payment Request Message ready to be sent | Yes | Yes | Message sent and waiting for ACK (677) |
| No | Yes | Message sent and waiting for DLN (673) |
| Yes | No | Message sent and waiting for ACK (677) |
| No | No | Complete (999) |

The status of the claim record gets updated as ‘Processed’ when the status of the claim transaction is moved to 999.

The camt.106 messages require a Business Application Header (BAH) to be added as per the CBPR+ format. Delivery Framework maintains the required configurations to populate the appropriate business service and message definition identifier for the respective channel or message combinations.

- camt.106.001.02 swift.cbprplus.01
- camt.106.001.02 swift.cbprplus.mlp.01

[ACK NAK Processing for Outgoing Charge Payment Request](#)

When a technical NACK/ACK is received for an outgoing camt.106, the system updates the acknowledgment details against the outgoing message in the system.

[Positive Acknowledgment](#)

Following are the process steps that get updated on receiving the positive acknowledgment from the network.

- If the status of the payment is ‘Payment Sent and waiting for Ack’ then it gets moved to the next status when a positive network acknowledgment is received.
- For a camt.106 following is also performed:
  - Payment status is moved to complete if DLN is not required for the underlying payment and the status of the claim is marked as Processed or the payment status is moved to ‘Payment sent and waiting for DLN’ if DLN is required.
  - If the status of the payment is not in ‘Payment sent and waiting for Ack’, then the system updates the audit trail to indicate the positive acknowledgment is received but the status is not moved. This could happen when the DLN is received before the network acknowledgment (exceptional scenario).

[Negative Acknowledgment](#)

When a technical NACK is received for an outgoing camt.106, the system updates the status of the payment so that it is displayed in the SWIFT ISO Technical exception queue from where the user can take the respective actions.

The accounting entries of the transaction are not automatically reversed on receipt of a negative acknowledgment.

If the status of the payment is not in ‘Payment sent and waiting for Ack’, then the system updates the audit trail to indicate that the negative acknowledgment is received but status is not moved.

The system stores the information of negative acknowledgment in the audit trail of the transaction.

[](#)[Action from SWIFT ISO Technical Exception Enquiry](#)

The following actions are available in the SWIFT ISO Technical exception enquiry, the user can take following actions.

The table below defines the Release options provided to the user.

| Option | Description |
| --- | --- |
| Cancel | It is not applicable to the Charges Payment Request message. So, when the user clicks this option, the system displays an error message as ‘Action is not applicable’. |
| Complete | When the user clicks this option, the payment status is updated as ‘Complete’ (999) and the status of the claim record is marked as processed. The audit trail is updated as ‘Completed from SWIFT ISO Technical Exception Queue by <user\_id> on <Date\_Time>’.  The user selects the ‘Complete’ action when the message is sent out again from the external interface. |
| ProcessAsAckReceived | It is applicable for the Payment Sent and waiting for ACK/NACK (Status Code 677) and NACK received for payment (680) statuses. For camt.106, this action moves the payment to the next status by assuming that the user has received ACK and continues processing. The payment is marked as complete irrespective of whether DLN is required or not and the status of the claim record is marked as Processed. The system updates the audit trail as ‘Processed as Ack Received from Technical Exception Queue by <user\_id> on <Date\_Time>’. |
| ProcessAsDLNReceived | It is applicable for the Payment sent and waiting for DLN and Negative DLN received for payment statuses. For camt.106, this action moves the payment to the next status assuming that the user has received positive DLN. The system marks the payment as complete and the status of the claim record is marked as processed. The audit trail gets updated as ‘Processed as DLN Received from Technical Exception Queue by <user\_id> on <DateTime>’. |
| Resubmit | The system opens the DE version screen for the outgoing message. The user selects the Resubmit option to resubmit the message. On resubmitting, the same payload gets resubmitted to the network. Only when the message status is awaiting ACK or awaiting DLN, the system add a possible duplicate indicator in BAH. No possible duplicate indicator is specified for other message statuses. Once resubmitted, the audit trail gets updated as ‘camt.106 is resubmitted by <CurrentUserName> at <CurrentDateTime>’. |

[Processing Positive or Negative Delivery Notifications for Outgoing camt.106](#)

When a Delivery notification (positive, negative) is received for an outgoing camt.106, the system updates the notification details against the outgoing message.

[Positive Notification](#)

- If the status of the payment is ‘Payment Sent and waiting for Ack’ or ‘Payment Sent and waiting for DLN’, then the system moves it to the next status Complete, and the updates the status of the claim as ‘Processed’.
- If the status of the payment is not in ‘Payment Sent and waiting for Ack’ or ‘Payment sent and waiting for DLN’, then the system updates the audit trail to indicate positive DLN is received but the status is not moved.

[Negative Notification](#)

When a negative DLN is received for an outgoing camt.106, the system updates the status of the payment so that the message is displayed in the SWIFT ISO Technical exception queue from where the user can take manual actions. Read [Action from SWIFT ISO Technical Exception Enquiry](#Action) for more information.

- If the status of the payment is ‘Payment Sent and waiting for Ack’ or ‘Payment sent and waiting for DLN’, then the system mark it as NACK received based on negative DLN received.
- If the status of the payment is not any one of the above, then the system updates the audit trail to indicate DLN is received but the status is not moved.

The accounting entries of the transaction are not automatically reversed on receipt of a negative DLN. The information of negative acknowledgment gets stored in the audit trail of the transaction.

[Ability to Handle XSD Validation in TPH Transformation Layer](#)

When TPH is unable to transform the charge payment request details into XML format as per CBPR+ camt.106 specification guidelines, the system marks the status of the claim transaction as ‘Payment failed XSD validation’.

Payment transactions with the status ‘Payment failed XSD validation’ are also displayed in the SWIFT ISO Exception Technical Exception Enquiry screen. The user takes the following actions for such payments.

- Complete: The user marks the status of the payment as complete when the message is not sent again through TPH (sent manually through an external system). For camt.106, the system marks the status of the claim as ‘Processed’.
- Cancel: Cancel option is not applicable for Charges Payment Request message. So, when user clicks this option, the system displays an error message as ‘Action not applicable’.

[Support of Unicode Character Set for camt.106 CBPR+ Message](#)

As per CBPR ISO 20022 guidelines, all SWIFT ISO MX elements which are defined by data type as TEXT should contain FIN X characters. The table below displays the available FIN X characters .

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| a-z | A-Z | 0-9 | / | - | ? |
| : | () | . | , | ' | + |

Apart from the above-mentioned FIN X characters, the special characters are allowed in

- All party (agents and non-agents) Name and Address elements.
- The Related Remittance Information element.
- The Remittance Information (structured & unstructured) element.
- The Email Address where included as part of a Proxy elements.

The table below displays the supported special characters.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ! | \* | | | @ | > | { |
| # | = | } | [ | < | ; |
| & | ^ | ~ | \ | . | $ |
| % | \_ | " | ] | ’ |  |

If there is no configuration in the system to replace a not allowed character, then it gets replaced with a full stop.

For the camt.106 message, the following fields can contain the special characters listed by CBPR+ in addition to FIN MX characters.

- Charge Requestor Name and Address tags
- Debtor Agent Name and Address tags
- Debtor Agent account Proxy ID tags

[Charges Payment Request - Pagination](#)

camt.106 charges payment (multiple transaction) request does not have any form of pagination.

For multiple charge payment requests, the system can group only 30 transactions. If the number of transactions during claim generation exceeds 30 for a particular bank, the system sends the remaining request in a different camt.106 message.

[Correlation between Payments and Outward Charge Payment Request](#)

The below image represents the references of incoming or redirected payment messages for which the outgoing claim message is generated. The underlying transaction reference number originally assigned by the sender is populated in the outgoing charge payment requests in the Instruction Identification tag.




Correlation between Payments and Outward Charge Payment Request

[Enquiry for Viewing Outward Charges Payment Request Message](#)

The user can view the outward charges payment request message generated for the underlying transaction using the Pending and Processed enquiry. The user can also view all the outward charge payment request messages and their corresponding status using a separate enquiry.

Read [Working With](Workingwith.htm) section for more information.

## Processing Workflow of Incoming Charge Payment Request

This section explains the processing workflow of the incoming charge payment request message sent by the correspondent bank to request the payment of charges, interest and/or other expenses.

[Incoming Charges Payment Request – Mapping](#)

On receiving the incoming charges payment request message, both single and multiple requests are mapped in the Received File details enquiry. To access this enquiry goto,

User Menu > Payments > Payment Hub > Payment Inquiries > Received and Sent Files Details > Received File Details > Received Messages / File Details List

From the Received File Details enquiry, the user can view the received XML by using View Blob Messages. For multiple charges payment request, the user can view the received XML message up to 20 transactions. If the received message is grouped for more than 20 records, then user can view the messages only in neutral format.

All the received incoming charges payment request messages are stored in the PP.IN.CLAIM.REQ table. Read [Fees and Billing](../../../../Payments/PP/Payments_Hub_(PP)/Fees_and_Billing/Introduction.htm#) user guide for more details on mapping.

[Incoming Charges Payment Request – Validation](#)

This section explains the pre-validations performed for incoming ISO charges payment request message on receiving into Temenos Payments Hub.

[Duplicate Check](#)

On receiving an incoming charges payment request message (Camt.106), the system performs a duplicate check based on the criteria defined in the *Case Duplicate Check* field in the PP.MSGMAPPINGPARAMETER table. The criteria for duplicate check are:

- Underlying Transaction - Record >> Underlying Transaction >> Instruction ID from XML.
- Sender BIC from XML.
- *Total Charges Amount* field in XML - Charges >> Per Transaction >> Record >> Total Charges Per Record >> Total Charges Amount

If multiple claim request is received for the same transaction with the same amount from the same sender BIC, then the claim request is considered as duplicate and moved to Unauth enquiry with an error message: Duplicate claim request received for the same transaction. This error message is displayed as a warning and is updated in the *Reject Description* field as well.

[Duplicate Claim Payment Check](#)

On receiving an incoming charges payment request for the transaction for which the settlement transfer is already processed, and the bank transfer is not in cancelled, rejected, or reversed status, then the record moves to unauth enquiry with an error message: Duplicate Claim Payment already exists. This error message is displayed as a warning and is updated in the *Reject Description* field as well.

[Identifying Original Transaction](#)

On receiving an incoming charges payment request message, the system identifies the original transaction based on the criteria defined in *Originalpmtidapi* in the PP.MSGMAPPINGPARAMETER table.

| XML | PP.IN.CLAIM.REQ FIELD |
| --- | --- |
| Charges >> Per Transaction >> Record >> Underlying Transaction >> Instruction Identification | RelatedRef |
| Charges >> Per Transaction >> Record >> Underlying Transaction >> UETR | OriginalUETR |

If the API is not defined, then the system uses the default criteria to identify the original transaction. The default criteria is identifying the transaction based on comparing the Underlying Transaction >> Instruction ID with the FTnumber of the underlying transaction.

If there is no record for the FTnumber specified in the claim request, then the record moves to unauth enquiry with an error message: “Related Payment record not found for this claim request”. This error message is displayed as a warning and is updated in the *Reject Description* field as well.

[Claim Request for Invalid Transaction](#)

On receiving an incoming charges payment request message, the system checks if the request is received for the valid transaction by performing the below validations,

- Direction not Outgoing and redirected
- Status not equal to 999
- Charge option not equal to OUR
- Message type not equal to 103, 103+, 102, 102+, pacs.008, pacs.009

If any of the above conditions are fulfilled, then the claim request is considered as invalid, the record moves to the unauth enquiry with an error message: Claim Request not valid for Related Payment. This error message is displayed as a warning and is updated in the Reject Description field as well.

[Pre-validation Failure – Unauth Enquiry](#)

If any of the above validation fails, then the system stores the received claim record in Hold status and moves the record to the Rcvd Claims – Unauth List – Auth enquiry.

Read [Fees and Billing](../../../../Payments/PP/Payments_Hub_(PP)/Fees_and_Billing/Introduction.htm#) user guide for more information about the user actions from this enquiry.

For an ISO charges payment request message which gets displayed in the unauth enquiry due to validation failure, the user can take action and move the record to live enquiry. From the Received Claims List enquiry, the user can settle the charge payment request by initiating the bank transfer.

[Pre-validation Success – Live Enquiry](#)

If all the above-mentioned validations are successful, then the system moves the received claim record to the Received Claims List enquiry for manual action. This enquiry displays the incoming claim request with below statuses.

- Pending– The incoming claim request which has passed all the validations, or the request is authorised from the Unauth enquiry, but the payment message is not yet created.
- Ignored– The incoming claim request which is manually ignored by the user. From this status, payment transaction cannot be created for the claim request.
- InProgress– The payment transaction is created for the incoming claim request, but the payment message is not processed completely and is in interim status.
- Processed – The payment transaction is created for the incoming claim request and the message is processed successfully.

SWIFT ISO Charges payment request message is displayed in ISO Received Claims List. To access this goto User Menu > Payments > Payment Hub > Payment Inquiries > Received and SentFile Details > Received File Details > Received Claims > ISO Received Claims List.

| Actions | Description |
| --- | --- |
| Settle with Outgoing BTR | The system opens the order entry version to initiate the bank transfer for the incoming claim request. The  Senders Reference field in OE page is auto-populated with Charge Identification tag of camt.106 message. End to End identification field in OE screen is auto populated with the “Rel Reference” field – the underlying transaction Ftnumber. Transaction Currency and Transaction amount is auto-populated from the incoming claim request message. Creditor BIC is auto-populated with the “Charges Requestor” tag of the incoming camt.106 message. Receiver is auto-populated with the Sender BIC Message type is defaulted as CLMPMT. |
| Settle with Book BTR | The system opens the order entry version to initiate the book transfer with the output channel defaulted as LEDGER. |
| Original Payment Details | The system displays the original underlying transaction details from pending and processed enquiries. |
| Ignore Claim | The system allows the user to ignore the claim request and also enter the reject description for the same. |
| View Claim Message | The system displays the received claim request details from the Delivery module, and also the details from the claim request table. |

Once the bank transfer is initiated and committed, the transaction is sent for the second user approval. If the authoriser rejects the transaction, then the claim record is updated back to pending status. If the transaction is approved by the second user and if the transaction moves to the repair queue during processing, the user can cancel the bank transfer from the repair queue.

If the bank transfer initiated for the claim request is cancelled by the user, then the claim record is updated back to pending status.

[Correlation between incoming Charges Request and Outgoing Bank Transfer](#)



[Technical Exception Processing of Outgoing Bank Transfer (Claim Payment)](#)

- When the outgoing bank transfer (Pacs.009) which is initiated for the incoming claim request is waiting for the acknowledgement from clearing or network or has already received the negative acknowledgement or negative dln, then the message is displayed in the SWIFT or RTGS ISO Technical Exception enquiry.
- From the enquiry, if the user clicks Cancel, then the accounting entries of the transaction are reversed, and the status is updated as Reversed (993).
- The corresponding the incoming claim record is also updated back to Pending status from In Progress.
- When the user clicks Claim Payment Details from the Received Claims List enquiry, the transaction is not displayed.

[Business Exception Processing of Outgoing Bank Transfer (Claim Payment)](#)

- Once the outgoing bank transfer which is initiated for the incoming claim request is sent to the correspondent bank, it is possible to receive the business reject (Pacs.002 RJCT) from the other bank.
- On receiving the business reject for the bank transfer, in TPH the processing is either STP or non STP based on the reason code configuration in the PP.CLEARING.RETURNCODE table.
- If the processing is STP, then the reject transaction is created with the reversal of accounting entries and original transaction status is updated to 998.
- If the processing is non-STP, then the message is parked in Business exception enquiry. On clicking Accept from the enquiry, then the same update takes place for the transaction. Once the transaction is moved to 998, then the corresponding claim record is also updated back to Pending status.
- When user clicks Claim Payment Details from the Received Claims List enquiry, the transaction is not displayed.

[Archival of Incoming Charges Payment Request](#)

The incoming ISO charges payment requests which are present in the ISO Received Claims List enquiry with status as Ignored and Processed are archived from the live table and moved to the archived table based on the configuration in ARCHIVAL application. Read [Archival section](Configuration.htm#Configur) in configuration for more information.

[Outgoing Claims and Incoming Claims in Standalone System](#)

In TPH Standalone payments instance, for both outgoing and incoming charges payment requests, the replication of the account and customer information is mandatory for the payment processing.

## Charge Payment Notification

The processing of incoming charges payment notification (105 (Single/Multiple) is MX equivalent of MT190/290) is explained here.

The camt.105 is the charges payment notification message sent by an account servicing institution to the account owner to advise charges, interest, or other adjustments to the owner's account. It provides details of charges which were previously unknown to the receiver.

The business and the processing workflows of charges payment notification (camt.105) in Temenos Payments Hub System are as follows.

[Message Workflow of Charge Payment Notification](#)

The diagram below represents the business workflow for single and multiple charge payments notifications where the account servicing institution sends a charge payment notification (camt.105) message to the account owner to notify them of a charge due to be taken from their account.

The subsequent charge is reported as a debit entry in a statement report such as camt.053 customer statement message.



[Mapping Correlation between MT190 and camt.105](#)

The diagram below illustrates the mapping correlation between MT190 and camt.105



[Message Flows between Agents](#)

Following a pacs.008 with settlement method INDA, the Instructed Agent may notify the Instructing Agent (as the Account Owner) of a charge related to the payment. The charge as agreed upon in account terms is deducted from the account and represented in a Customer Statement.

The diagram below represents the message flow when a single charge payments notification is received.



Following a period (day. week, month, and so on) where the Account Owner’s account has accrued several charges on their account, the Account Servicing Institution notifies the Account Owner of the total (consolidated) charge for the various charge records. The total charges as agreed upon in the account terms are deducted from the account on the value date specified and represented in the customer statement.

The diagram below represents the message flow when multiple charge payments notifications are received.



### High Level Structure Details of camt.105

[Charges Requestor](#)

The Charges Requestor element identifies the agent that is providing notice the charge. This agent is not necessarily the sender of the message. Agent that requests the charges, if other than the sender.

[Charges Identification](#)

The Charges Identification element captures the unique reference associated with the charge notification which can be used by the Charges Account owner to reconcile the payment (settlement) of this charge on their account statement. It can be considered an equivalent in the legacy MT directly comparable with the Transaction Reference Number (Field 20) of the legacy MT charge messages.

[Charges >> Per Transaction >> Record](#)

The Charges Per Transaction nested element captures the details of the charge, including the underlying transaction the charge relates to, and a breakdown of the charge being collected. The record indicates the number of transactions for which the charges payment notification is received.

In a single charges payment notification, the number of records can be one, while in a multiple charges payment notification, there can be multiple and there is no upper limit set by the SWIFT specification for this tag element.

In this record, there are four mandatory sub-tag elements like Record Identification, Underlying Transaction, Total Charges Per Record, Charges Breakdown and Value Date.

| Sub-Tag Element | Description |
| --- | --- |
| Underlying Transactions | Identifies the underlying payment transaction for which the charges are being notified. At least one identification must be provided, this allows the receiver to identify from this reference, the underlying business transaction the charge is related to.  This can be compared to Related Reference (Field 21) of the legacy MT Charges payment notification message. Account Servicers Reference should be used as a default if no other identification element is relevant for the underlying transaction.  Some sub-tags are Message Identification, Message Name Identification, Instruction Identification, End to End Identification, UETR, and so on. |
| Total Charges Per Record | Indicates the sum of the number of Charge Breakdown Items records. For example, 2 indicates that there are two occurrences of the Charge Breakdown element. The Total Charges Amount is the sum of Charge Breakdown Amount records. |
| Charges Breakdown Items | Indicates a detailed breakdown of total charges by the type of charge. For example, DEBT is where the pacs.008 Charge Bearer indicates all charges are to be borne by the Debtor. NSTP for non-straight through processing charges and so on. |
| Value Date | Indicates the date and time on which the charge is considered and represented in the statement entry. |

## Processing Workflow of Incoming Charges Payment Notification

This section explains the processing workflow of the incoming charges payment notification message sent by the account servicing institution to the account owner to advise charges, interest, or other adjustments to the owner's account. It provides details of the charges which are previously unknown to the receiver.

[Incoming Charges Payment Notification – Mapping](#)

On receiving the incoming charges payment notification message, both single and multiple notifications are mapped in the Received File Details enquiry which can be accessed from:

User Menu >> Payments >> Payment Hub >> Payment Inquiries >> Received and Sent Files Details >> Received File Details >> Received Messages / File Details List

From the Received File Details enquiry, the user can view the received xml using the View BLOB Messages button. For a multiple-charges payment notification message, the user can view the received xml message for up to 20 transactions. If the received message is grouped for more than 20 records, then the user can view the messages only in a neutral format.

All the received incoming charges payment notification messages are stored in the EB.QUERIES.ANSWERS table.

[Incoming Charges Payment Notification – Validation](#)

This section explains the pre-validations performed for incoming ISO charges payment notification message upon receipt into Temenos Payments Hub.

[Duplicate Check](#)

On receiving the incoming charges payment notification message (camt.105), the system does not perform a duplicate check.

[Identifying Original Transaction](#)

On receiving the incoming charges payment notification message, the system identifies the original transaction based on the criteria defined in ORIGINALPMTIDAPI in the PP.MSGMAPPINGPARAMETER table.

| XML | EB.QUERIES.ANSWERS |
| --- | --- |
| Charges >> Per Transaction >> Record >> Underlying Transaction >> Instruction Identification | REL.REFERENCE |
| Charges >> Per Transaction >> Record >> Underlying Transaction >> UETR | UETR.REF |

If an API is not defined, then the system uses the default criteria to identify the original transaction. The default criteria are identifying the transaction based on comparing the Instruction ID (with the FTnumber or UETR) with the EndToEndReference of the underlying transaction.

When the system derives the Original Transaction reference successfully:

- The EBQA record is created with the status as INWORK. The user can take necessary action from here, that is, map the Derive FT Number against the Charge notification EBQA record in the *Orig Ft Number* field. Once the system identifies the original transaction, it stores the details of the EBQA case created in POR.SUPPLEMENTARY.INFO as follows:
  - Store the case details in POR.SUPPLEMENTARY.INFO of the underlying transaction.
  - On receiving multiple notifications for a payment, the system stores the following details as multivalued.
    - Case Type - camt.105- ORIG.MSG.TYPE (pacs.008, pacs.009, MT103, MT202, MT205)
    - Case Id - EBQAID advice record is created for the underlying payment.
- The system updates the audit trail of the underlying transaction as 'Inward Charges Payment Notification is received for this payment' along with RecordID reference. (When EBQA =INWORK and Original Transaction is found)

When the system is unable to derive the Original Transaction reference (FT Number of outgoing message):

- An EBQA record is created with status as INWORK, also the Error Reason field is updated as 'Original Transaction is not found for this charge notification' in the EB. QUERIES.ANSWERS table.
  - If UETR and Instruction ID are not present in the charges notification message, a EBQA record should be created with status as INWORK, then the Error Reason is updated as 'Charges Notification is not received for a payment transaction.'
  - Note: TPH should always take precedence over the UETR (Unique End-to-End Transaction Reference) when both UETR and Instruction ID are present in the charge notification message received while determining the underlying transaction.

[Enquiry to List and Action on the Notification:](#)

The system holds the received charges payment notification record in the Received Charge Payment Notification enquiry for manual action. Temenos Payment System displays the Charges Payment Notification records received and are currently in the INWORK status. The user can view all the incoming charges payment notifications with the below statuses.

- INWORK– The incoming charges payment notification which has passed all the validations, or the notification is awaiting for manual action from enquiry, but the payment message is not yet created.
- INPROGRESS– The payment transaction is created for the incoming charges payment notification, but the payment message is not processed completely and is in interim status.
- PROCESSED– The payment transaction is created for the incoming charges payment notification and the message is processed successfully.
- IGNORED – The incoming charges payment notification which is manually ignored by the user. From this status, a payment transaction cannot be created for the claim request.

SWIFT ISO charges payment notification message is displayed in the Inward Charges Payment Notification enquiry accessible from the below menu navigations.

User Menu >> Payments >> Payment Hub >> Payment Inquiries >> Received and Sent File Details >> Received File Details >> Received Charges Payment Notification >> Inward Charges Payment Notification

| Actions | Description |
| --- | --- |
| Create Book Txn | The system opens the Order Entry version to initiate the book transfer with output channel defaulted as LEDGER and message type as CHGADV. |
| View Notification Details | The system displays the corresponding Charges payment notification record details stored in EBQA. |
| View Original Transaction | The system displays the original underlying transaction details from the Pending and Processed enquiry. |
| Ignore Notification | The system allows the user to ignore the claim request and to enter the reject description for the same. |
| View Notification Message | The system displays the received notification request details from the Delivery module. |

Once the book transfer is initiated and processed:

- When payment Direction EQ 'B' and Incoming Message Type EQ 'CHGADV' and Sender's references EQ 'Charge Identification' from Charge notification message and Transfer Type EQ 'B', then EBQA status is updated as follows: If the book transaction is:
  - Created directly into the Live table (600) or not authorised (315) or parked in any interim status - Status must be updated as InProgress.
  - Processed successfully till 999 - Status should be updated as PROCESSED.
  - Created and failed due to validation failure and parked in the Repair queue or User cancelled the payment from the Repair screen - Status must be changed from InProgress to INWORK.
- When the second approver rejects or deletes the book transfer, then a notification status must be updated as INWORK again.
  - If the rejected book transaction is modified and committed, then the system updates the status as InProgress again.
- When the user manually cancels the book transfer from repair queue, then FT number of book transfer updated in charges payment notification record should be deleted and the status must be updated as INWORK again.

[Archival of incoming Charges Payment Notification](#)

The incoming ISO charges payment notification present in the Inward Charges Payment Notification enquiry is archived from the live table and moved to archived table based on the archival days configuration in ARCHIVAL record. Read [Archival](Configuration.htm#Configur) section in configuration for more information.

[Incoming Charges Payment Notification in Standalone System](#)

In TPH Standalone payments instance, for the incoming charges payment notification, the replication of the account and customer information is mandatory for payment processing.

In this topic

- [Introduction to SWIFT MX Claims and Charges](#IntroductiontoSWIFTMXClaimsandCharges)

- [Message Types](#MessageTypes)
- [Charge Payment Requests](#ChargePaymentRequests)
- [Processing Workflow of Outgoing Charge Payment Request](#ProcessingWorkflowofOutgoingChargePaymentRequest)
- [Processing Workflow of Incoming Charge Payment Request](#ProcessingWorkflowofIncomingChargePaymentRequest)
- [Charge Payment Notification](#ChargePaymentNotification)
- [Processing Workflow of Incoming Charges Payment Notification](#ProcessingWorkflowofIncomingChargesPaymentNotification)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:57:44 PM IST