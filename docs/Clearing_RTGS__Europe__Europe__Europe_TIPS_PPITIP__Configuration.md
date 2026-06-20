# Configuring Target Instant Payment Settlement (TIPS)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_TIPS_PPITIP/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm) > Configuration

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
    - [Introduction](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
    - [Configuration](../../Europe/Europe_TIPS_PPITIP/Configuration.htm)
    - [Working with](../../Europe/Europe_TIPS_PPITIP/Working_with.htm)
    - [Tasks](../../Europe/Europe_TIPS_PPITIP/Tasks.htm)
    - [Outputs](../../Europe/Europe_TIPS_PPITIP/Outputs.htm)
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
  - [Nordic Credit Transfer Payments Nordic Credit Transfer Payments](../../Europe/Europe_NCT_Payments_PPNPCT/Introduction.htm)
  - [Nordic Instant Credit Transfer Nordic Instant Credit Transfer](../../Europe/Europe_Nordic_Instant_CT_Payments_PPINIP/Introduction.htm)
  - [Euro Swiss Interbank Clearing Euro Swiss Interbank Clearing](../../Europe/Europe_euroSIC_PPESIC/Introduction.htm)
  - [German Bundesbank RPSSCL Clearing German Bundesbank RPSSCL Clearing](../../Europe/Europe_GermanBundesbankRPSSCLClearing_PPRPCL/Introduction.htm)
  - SIC/EuroSIC Directory Upload and Reachability;)
  - [SIC - Instant Payment SIC - Instant Payment](../../Europe/Europe_SIC-IP/Introduction.htm)
  - [Spain IBERPAY Instant Clearing Spain IBERPAY Instant Clearing](../../Europe/Europe_Spain_IBERPAY/Introduction.htm)
  - Instant Payment Regulation (EU IPR);)

Payments

# Configuring Target Instant Payment Settlement (TIPS)

Updated On 10 July 2025 |
 14 Min(s) read

Feedback
Summarize

This section helps the user to understand the configuration of TIPS.

## TPH as a Direct Participant (DP)

This section helps the user to understand the configuration of Temenos Payment Hub (TPH) as a DP in TIPS Clearing.

[TIPS Clearing](#)

In Model Bank (MB), TPH acts as a DP in the TIPS Clearing. It can directly exchange messages with the TIPS Clearing Channel (if configured). To configure TIPS clearing, perform the following:

- Define the TIPS source.
- Define clearing (as a DP).
- Define the Message Type Level settings for clearing.
- Configure customer status reports to be sent at the correspondent bank and customer levels.
- Configure reports for TIPS payments.

[Defining TIPS Clearing as a Source](#)

TPH can receive payments from clearing. Hence, as a pre-requisite to clearing setting, define *Source* *Type* as NC (Non-client) in PP.SOURCE table. To define a source, go to **Admin Menu** > **Payments Hub** > **Static Data** > **Source**.

[Defining TIPS as a Clearing Channel](#)

TPH can connect to the clearing channel as it is a DP to clearing. To perform this, do the following actions:

1. Go to **Admin Menu** > **Payments Hub** > **Local Clearing** > **Clearing**.
2. Define the following fields in the Clearing House of the PP.CLEARING table:

   | Field | Description |
   | --- | --- |
   | *Clearing Name* | Set as TIPS |
   | *Participant Type* | If it is a clearing channel, then leave it blank. |
   | *File Transaction Ind* | If it is a single (not file) payment, set as T. |
   | *Clearing Type* | If it is an instant payment, set as I. |
   | *Clearing BIC* | BIC of the Clearing House to which the TIPS payment is sent. |
   | *RTGS System* | If it is an instant channel, set as I. |
   | *Time Zone* | Time zone used while timestamping payments that are sent to clearing. [ClosedExample](#) TIPS requires all payment initiations (to the Clearing House) to be timestamped with UTC time zone as the base. This is different from the time zone of the processing company (defined in the PP.COMPANY.PROPERTIES). |
   | *Target Execution Time* | Until when TPH can process outward instant payment after the Originator PSP has Time Stamped the Transaction (in seconds). |
   | *Posting Method* | The following values are available: - DebitNow – Reserves, books and sends the payment to the Clearing House. On confirmation from clearing, it marks the payment as completed or reverses the payment (based on positive or negative confirmation). - DebitOnPayConfirmation – Reserves and sends the payment to the Clearing House. On confirmation from clearing, it books the payment or cancels the reservation (based on positive or negative confirmation). |
   | *Inst Pay Rej Booking* | Action that system needs to perform when clearing sends a negative confirmation for an originated credit transfer (original transaction). The following values are available: - Reverse – This value performs the below functions:   - Sets status of original transaction to Rejected.   - Performs payment reversal.   - Reverses debit and credit amounts with charges applied.   - Does not calculate any new charges for the payment. - ReverseAndCharge – This value performs the below functions:   - Sets the status of original transaction to Rejected.   - Creates a new transaction reversing the debit and credit parties.   - Applies any charge configured for a new transaction   - Charges the customer for a negative confirmation from clearing. Any charges applied on the original payment remains the same. |
   | *Screening**Response**Action* | Behaviour of the system on receiving 'Possible Hit' response from the Filtering engine. - SendPendingConfirmation –Sends a pending status confirmation message defined in the *Clearing**Status**Message**Type* field (PP.CLEARING.SETTING table). - Reject – Sends a negative confirmation to clearing - Blank – No action required |
   | *24by7Channel* | Has the following values: - 24/7 – Channel is available 24/7 for processing instant payments. System assumes that all days are working days, hence, does not perform holiday checks. - Blank – System is a non-24/7 channel for processing instant payment and checks for cut-off and holidays. |
   | *Clearing**Status**Message**Type* | Message type used when sending status confirmation to the Clearing House. - Can be positive, negative or interim confirmation. - A valid value in the PP.MSGPAYMENTTYPE |
   | *Ack**Type**Bene**ficiary* *Bank* | Defines whether the beneficiary bank expects the confirmation from clearing as: - TechnicalHandshake - Confirmation Message (not applicable for IPs) - On receiving an instant payment, it processes and sends the confirmation to clearing. - Beneficiary bank then expects a technical handshake through the interface layer for the confirmation message sent.  In some cases, clearing cannot support technical handshake and only sends a confirmation message (pacs.002). |
   | *Investigation Time* *Out**and* *Clearing Investigation Msg Type* | Time (in seconds) after which an automatic investigation (specified in the *Clearing Investigation Msg Type* field) is sent to clearing. |
   | *Investigation Retry Count* | Maximum number of times an investigation message can be resent when a confirmation for an originated payment is not received |
   | *Investigation Retry Time* | Time interval between sending automatic investigation messages |

[Message Types](#)

Define the following fields to configure the message types:

| Field | Description |
| --- | --- |
| *Clearing Transaction Type* | Helps to define the outgoing message in the associated *Outgoing**Message**Type* field. This needs to be a valid record in the PP.TRANSACTION.TYPES table`.` |
| *Out Message Format API* | It is mutually exclusive with the *Clearing Transaction Type* and *Outgoing Message Type* *fields*.  - If an API is defined to return the outgoing message type, system uses the API. - If API is not defined, it refers the associated multi-value set to find the outgoing message type. |
| *Outgoing Message Type* | Uses when sending the payment to the clearing house or DP. This needs to be a valid value in the PP.MSGPAYMENTTYPE table. |

[](#)[Supporting Hybrid Address](#)

To support sending a hybrid address in the outward message, configure the Address Type as 'Hybrid, Str, Unstr'.

If left blank, the hybrid address is not sent in the outward message. When the value is set as 'Hybrid, Str', it sends either hybrid or structured address details, respectively.

[Defining the TIPS Clearing Settings Based on Message Type and Direction](#)

1. Go to **Admin Menu** > **Payments Hub** > **Local Clearing** > **Clearing Setting**.
2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Max Inst Time Out* | Time (in seconds) within which the entire round trip of an instant payment needs to be completed |
   | *Auto Negative Cancel Req Response* | If an incoming cancellation request receives a negative response (original transaction not found or cancellation requests is beyond the allowed days), set the value as Y. This denotes that payment can be processed automatically without manual intervention |
   | *Original Trn LookUp Criteria API* | API used to retrieve the original transaction related to the incoming return, reversal or refund message. It differs based on clearing and clearing transaction types. If API is not defined, the above transaction types are not matched to the original transaction. |

## IP Channel for TIPS Clearing when TPH is a DP

If TPH is a DP to clearing, it can receive payments from an IP and forward it to the TIPS clearing. Similarly, TPH can receive payments from TIPS clearing and forward it to IP. Hence, the IP channel and source need to be configured in TPH.

[Defining IP as the Source](#)

- Define the *Source Type* field as NC (Non–client) in the PP.SOURCE table, as IP is a source from where payments are received.

Key to PP.SOURCE and PP.CLEARING tables are the same.

Key to the PP.CLEARING table needs to be an identifier for the IP. This can be a user defined name.

- Set the *Participant Type* field as IP, which denotes it is an IP channel.

Automatic triggering of investigation messages does not apply for IPs.

[Defining the IP Channel Attributes](#)

- Define the IP channel attributes in the PP.CLEARING.SETTING table.

  The *Max* *Inst Time Out* field does not apply for IPs.
- Configure the *Negative Cancel Req Response* and *Original* *Transaction Returns* *API* fields.

## TPH as an IP

TPH as an IP in the TIPS clearing can only connect to the DP. Hence, define DP as a channel in the PP.CLEARING table. To perform this, do the following actions:

1. Go to **Admin Menu** > **Payments Hub** > **Local Clearing** > **Clearing**.

   Key to PP.SOURCE and PP.CLEARING tables are the same.
2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Channel Name* | Defines DP as a channel in PP.CLEARING table. - Name can be user defined. - A record with the same name needs to exist in the PP.SOURCE table. |
   | *Source Type* | DP is a source from where the payments are received. Set as NC (Non-client) in PP.SOURCE table. |
   | *Participant Type* | Denotes that TPH is connecting to a DP, when set as DP. |
   | *Clearing BIC or Clearing NCC* | Sends and receives payments from BIC or NCC of the DP. |
   | *Posting Method* | Allows to debit and send the payment to DP (as TPH is the IP), when set as DebitNow. |

## Customer Status Reports

[Correspondent Bank Conditions](#)

This table specifies the type of payment confirmation sent to the ordering customer for a correspondent bank (where TPH is a DP). The following are the configuration relating to confirmations:

- Whether ACK, NACK or BOTH are required.
- Whether an interim status report is required
  - If a correspondent bank sends a payment (which is forwarded to Clearing), then an interim status confirmation can be sent to the correspondent bank (if configured).
  - Once the payment reaches its final state (Completed or Cancelled), a final status confirmation is sent. This enables correspondent banks to know the status of their payments.

The *Message* *Type* (sent) is set as ACK or NACK.

[Client Conditions (Customer level configuration)](#)

Customer or account level agreements are available for instant payments. Hence, a default record is configured to hold the configuration. The following are the configurations relating to confirmations:

- Whether ACK, NACK or BOTH confirmations are required.
- Whether an interim status report is required
  - If a customer initiates a payment (which is forwarded to the Clearing), then an interim status confirmation is sent to the customer (if configured).
  - Once the payment reaches its final state (Completed or Cancelled), a final status confirmation is sent.

The *Message Type* (sent) is set as ACK or NACK.

To know more, refer to Status Reporting section.

[Bank to Customer Statement](#)

A new directory (TIPSSOA) is created in EB.FILE.UPLOAD.TYPE to receive the Statement of Account (SOA) report from clearing.

1. To receive statements, go to **Admin Menu** > **Framework Parameter** > **Payments** > **Bulk Payments** > **Bulk Upload Type**.



2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *Upload Dir* | Path from which the incoming message is uploaded |
   | *Extension* | File format of the incoming message |
   | *Interface Routine* | Routine that maps the tags from the received message against the fields in PP.CLR.REPORTS.FILE table |
   | *Xsd Dir* | Path in which the XSD is placed |
   | *Xsd File* | Original file name of the XSD (that belongs to the clearing) |
   | *Xml Validation Routine* | Routine that validates the incoming message against the XSD file |

## Return and Reject Codes

TIPS allows returning the settled original credit transfers based on the cancellation request received from the originating bank or creating the recall for the original credit transfer based on the TIPS-applicable return and reject codes.

To configure the reason codes, go to **Admin Menu** > **Payments** > **Payment Hub** > **Bank System Administration** > **Local Clearing** > **Clearing Return Code**.



Configure the following key fields as shown in above screenshot:

| Field | Description |
| --- | --- |
| *CompanyID* | Indicates the company for which the record is created |
| *ClearingID* | Specifies the name of the clearing maintained at TPH |
| *ClearingReturnCode* | Indicates the reason code for initiating the recall request |
| *ReturnCodeLevel* | Indicates the level for each clearing reason code defined:   - F – File based Level - B – Bulk Based Level - T – Transaction Based Level |
| *ReturnCodeDescription* | Describes the reason code given in the ClearingReturnCode field |
| *ClearingTransactionType* | Defines the transaction type of the clearing |
| *ClearingNatureCode* | Defines the code which identifies the nature of the clearing payment |
| *ReturnAllowedDays* | Indicates the maximum days up to which recall can be initiated or recall request can be received. Format is as follows, where X is the number of days:   - X: X working days - XC: X calendar days - XW: X working days |
| *Reason Code Type* | Indicates if the defined ClearingReturnCode is ISO or proprietary based on reason code |
| *Bank Cust Initiated* | Indicates if request is initiated by bank or customer:   - B – Initiated by bank - C – Initiated by customer - \* - Applicable for both |

Read the [Configuring Manual Repair](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Manual_Repair/Configuration.htm) topic in the Manual Repairs guide for more details on configuring return and reject codes.

## Cancellation Request by Bank

Read the Cancellation Request by Bank section in the [Configuring Manual Repair](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Manual_Repair/Configuration.htm) topic of the Manual Repairs guide for more details on creation of cancellation request by the bank.

## Cancellation Request by Originator

Read the Cancellation Request by Originator section in the [Configuring Manual Repair](https://docs.temenos.com/docs/Solutions/Payments/Payments/PP/Payments_Hub_(PP)/Manual_Repair/Configuration.htm) topic of the Manual Repairs guide for more details on creation of cancellation request by the originator.

## Inclusion of Distinguished Name

A new record should be created in the DE.CARRIER table with record Id as ‘TIPS’. This is used for storing and retrieving the distinguished names.

In this topic

- [Configuring Target Instant Payment Settlement (TIPS)](#ConfiguringTargetInstantPaymentSettlementTIPS)

- [TPH as a Direct Participant (DP)](#TPHasaDirectParticipantDP)
- [IP Channel for TIPS Clearing when TPH is a DP](#IPChannelforTIPSClearingwhenTPHisaDP)
- [TPH as an IP](#TPHasanIP)
- [Customer Status Reports](#CustomerStatusReports)
- [Return and Reject Codes](#ReturnandRejectCodes)
- [Cancellation Request by Bank](#CancellationRequestbyBank)
- [Cancellation Request by Originator](#CancellationRequestbyOriginator)
- [Inclusion of Distinguished Name](#InclusionofDistinguishedName)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:18:38 PM IST