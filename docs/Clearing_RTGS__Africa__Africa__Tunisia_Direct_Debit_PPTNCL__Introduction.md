# Introduction to Tunisia Direct Debit

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Africa/Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Africa > [Tunisia Direct Debit](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm) > Introduction

- Africa;)
  - [SYGMA RTGS SYGMA RTGS](../../Africa/Africa_SYGMA_RTGS_PPSYGM/Introduction.htm)
  - [SYSTAC Credit Transfer SYSTAC Credit Transfer](../../Africa/Africa_SYSTAC_CEMAC_CT_PPSYTC/Introduction.htm)
  - [SYSTAC Direct Debit SYSTAC Direct Debit](../../Africa/Africa_SYSTAC_CEMAC_DD_PPSYTC/Introduction.htm)
  - [SYSTAC Cheque Payment SYSTAC Cheque Payment](../../Africa/Africa_SYSTAC_Cheque_PPSYTC/Introduction.htm)
  - [Tunisia Credit Transfer Tunisia Credit Transfer](../../Africa/Tunisia_SIBTEL_CT_PPTNCL/Introduction.htm)
  - [Tunisia Direct Debit Tunisia Direct Debit](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm)
    - [Introduction](../../Africa/Tunisia_Direct_Debit_PPTNCL/Introduction.htm)
    - [Configuration](../../Africa/Tunisia_Direct_Debit_PPTNCL/Configuration.htm)
    - [Working with](../../Africa/Tunisia_Direct_Debit_PPTNCL/Working_with.htm)
    - [Tasks](../../Africa/Tunisia_Direct_Debit_PPTNCL/Tasks.htm)
    - [Outputs](../../Africa/Tunisia_Direct_Debit_PPTNCL/Outputs.htm)
  - [Tunisia Cheque Clearing Tunisia Cheque Clearing](../../Africa/Tunisia_Cheque_Clearing_PPTNCL/Introduction.htm)

Payments

# Introduction to Tunisia Direct Debit

Updated On 06 October 2022 |
 8 Min(s) read

Feedback
Summarize

SIBTEL is the central electronic clearing system for Tunisia Direct Debit (DD) collection scheme. The participant bank in Tunisia uses the clearing to process DD payments in TND currencies. The customer sends a DD collection request through a customer channel in a flat file format. The file triggers the DD transaction processing in the bank, after which funds are collected from the debtor and paid to the creditor on completion of the processing. The customer needs to have the transmitter code (issued by the central bank) to initiate the DD collection request.

## Customer Transmitter Code

Customer eligible to request a DD collection needs to have a unique transmitter code that is maintained with the participant bank. This code is captured at the customer or account level.

The user needs to capture the transmitter code locally.

## Outward DD Collection Request

The collection file received from the BH Net (customer channel) has mandate and DD records. Therefore, the file is split into two for processing:

- Mandate transaction
- DD transaction

- The mandate file is processed before DD transaction.
- The client specific team needs to handle the split of the customer file into mandate and DD files locally.

## Generation of Mandate File

The DD module uses the mandate files to create, amend, or cancel records in the system. After processing, the mandate files are generated and sent to clearing in the SIBTEL format.

The Country Model Bank team handles the requirement to receive, process and generate mandate file.

## Generation of DD File

Temenos Payments Hub (TPH) uses the file with DD collections mapped to neutral format. After mapping the file to internal mapping objects and file levels, it performs business validations (such as duplicate check, transmitter code, and posting restriction). If any validation fails, it rejects the entire file and sends the customer status report with a reason for rejection through the BH Net channel.

The client specific team needs to handle the following locally:

- Mapping of DD file to TPH (internal neutral format)
- Validating file and customer levels
- Generating customer status report to BH Net channel



The user can manually capture the outward DD collection request through the Order Entry (OE) version provided. The system identifies whether a transaction is a book or clearing based on the debtor bank code.

Temenos Payments Hub (TPH) supports book transfers and handles bank specific requirements locally.

In addition to the standard channel level validations, it performs reachability check and RIB (debtor’s account) validations.

The Country Model Bank team handles the mandate validation.

If all the validations are successfully, it checks for the following:

- Cut-off for sending the presentation file (09:00 AM)
- Processing is completed and placed in the ‘Out’ file queue

The outward file is generated and sent to clearing at the scheduled frequency time (09:30 AM). It also changes the status of the transaction from 706 to 999 and generates the customer-side accounting as follows:

If the channel cut-off (09:00 AM) has passed for the day, it warehouses the transaction with dates recalculated to the next working date. On the Start of Day (SOD) of the due date (settlement date), it de-warehouses the transaction and performs further processing.

- If DD initiation is a child of a batch (configured as part of the netting agreement, where *Batch Booking Indicator* is set as Y), it uses:
  - Debit clearing suspense account (configured in clearing setting)
  - Credit batch suspense account (configured for each company)
- If it is the total requested bulk amount of a batch booking (transaction is known as the parent transaction of children in the batch), it uses:

- Debit batch suspense account (configurable for each company)
- Credit creditor account (ordering client)

- If a DD initiation is a single transaction (or configured as part of netting agreement, where *Batch Booking Indicator* is set as N), it uses:

- Debit clearing suspense account (configured in clearing setting)
- Credit creditor account (ordering client)

- As clearing follows post-settle accounting framework, the settlement-side nostro booking (generated after the reject cut-off time 09:00 PM on running the settlement service) uses:

- Credit clearing suspense account
- Debit clearing nostro account

## Inward Mandate File from Clearing

The DD module receives and uses the mandate files with details. During processing, it creates, amends and cancels the mandates based on the details received in the file.

The Country Model Bank team handles the mandate files locally.

The processing of inward DD file needs to start after completing the inward mandate file in DD module (handled locally).

## Inward DD File from Clearing

The DD presentation file from SIBTEL clearing debtor is mapped to TPH neutral mapping objects. It performs file level duplicate checks based on the ‘Lot Number’ received in the header of the incoming file. Additionally, performs standard business validations and processes the transaction as Straight-Through Processing (STP).

After processing, it generates customer-side bookings and marks the transaction status as 999. It also generates the booking based on the following details:

- Debit customer account
- Credit clearing suspense account

Additionally, generates settlement entries for nostro bookings (after the reject cut-off time 09:00 PM on running the settlement service) using:

- DR clearing suspense account
- CR clearing nostro account

## Outward Reject for Inward DD Transaction

If any validation fails for the inward DD transaction, it moves the record to Repair status (235). The user can perform the following in the Repair queue records:

- Process the transaction further by correcting the anomaly in processing
- Reject the transaction by giving appropriate reject code

The outgoing reject file is generated according to the channel cut-off and frequency configuration in the format acceptable to SIBTEL clearing. As clearing follows post-settle accounting, it does not generate any bookings for the outward reject. It adjusts the settlement entries for inward DD amount with the amount of the reject transaction, and uses the net amount at the end of reject cut-off.

## Inward Reject File

The inward reject file is received from clearing, when the debtor bank rejects the transaction. This file is mapped to TPH neutral mapping objects and original transaction is identified based on the unique seven digit number (DD Number) sent in the outgoing file.

After original transaction is identified, it copies the details from the original transaction to return transaction created for the inward reject. If the system cannot identify the original transaction for the inward reject, it moves the transaction to Repair queue for the user to modify or correct the anomaly in the transaction. After processing the inward reject, it generates reversal entries based on the following details:

- Debit customer account
- Credit clearing suspense account

The settlement entries amount is adjusted for the inward reject and the net amount is used for settlement.

## Inward CRS Report Files from Clearing

The CRS files received from clearing has all the transaction details exchanged between clearing and bank. These inward files are mapped to Temenos Payments Hub neutral mapping objects. The user can view the data received in the file in report format using an inquiry.

In this topic

- [Introduction to Tunisia Direct Debit](#IntroductiontoTunisiaDirectDebit)

- [Customer Transmitter Code](#CustomerTransmitterCode)
- [Outward DD Collection Request](#OutwardDDCollectionRequest)
- [Generation of Mandate File](#GenerationofMandateFile)
- [Generation of DD File](#GenerationofDDFile)
- [Inward Mandate File from Clearing](#InwardMandateFilefromClearing)
- [Inward DD File from Clearing](#InwardDDFilefromClearing)
- [Outward Reject for Inward DD Transaction](#OutwardRejectforInwardDDTransaction)
- [Inward Reject File](#InwardRejectFile)
- [Inward CRS Report Files from Clearing](#InwardCRSReportFilesfromClearing)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 3:34:07 PM IST