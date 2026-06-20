# Introduction to Hungary Instant Credit Transfer (HCT INST) Payments

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm) > Introduction

- Europe;)
  - [Target Instant Payment Settlement Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm)
  - [Hungary Instant Credit Transfer Payments Hungary Instant Credit Transfer Payments](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
    - [Introduction](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Introduction.htm)
    - [Configuration](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Configuration.htm)
    - [Working with](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Working_with.htm)
    - [Tasks](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Tasks.htm)
    - [Outputs](../../Europe/Europe_HCT_Instant_Payments_PPIHCT/Outputs.htm)
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

# Introduction to Hungary Instant Credit Transfer (HCT INST) Payments

Updated On 22 March 2025 |
 12 Min(s) read

Feedback
Summarize

TPH processes payments that are sent to or received from the HCT INST clearing by using the existing Instant Clearing Framework. The GIROInstant (GIROInst) service continuously processes, clears, and settles HCT INST transaction messages 24 hours a day and every calendar day of the year. The process flow of the payments is shown below:



1. The originator bank (TPH) receives an instant payment instruction from the originator, and performs the following for execution of the instant payment:
   - Generates the time stamp after receiving the transaction and user’s authentication
   - Validates the instruction and reserves the amount on the client’s account
   - Creates the HCT INST transaction
2. Additionally, it sends the HCT INST transaction message to the GIROInst.
3. GIROInst forwards the transaction message to the beneficiary bank.
4. The beneficiary bank sends the confirmation message to the GIROInst indicating the following:
   - Received the HCT INST transaction
   - Process the HCT INST transaction (positive confirmation) instantly
5. GIROInst executes the clearing on the respective accounts. It debits the originator bank and credits the beneficiary bank, and then notifies the sender and beneficiary of the execution.
6. The originator bank debits its client’s account (amount reserved in step 1).
7. Received funds are made available to the beneficiary (by the beneficiary bank) after receiving the settlement confirmation from GIROInst (response to the positive confirmation message sent in step 4).

[Types of Payment and Messages](#)

TPH supports the following HCT INST payment message types:

| Message | Message Type | Description | TPH Support |
| --- | --- | --- | --- |
| pacs.008.001.02 | B2B | Customer credit transfer | Inward and outward |
| pacs.004.001.02 | B2B | Return | Inward and outward |
| camt.056.001.01 | B2B | Payment cancellation request or request for recall | Inward and outward |
| camt.029.001.03 | B2B | Resolution of investigation | Inward and outward |
| pacs.028 | B2B | Payment status request | Inward and outward |
| pacs.002.001.03 | B2B | Clearing payment status report | Inward |
| pain.001.001.03 | C2B | Credit transfer initiation | Inward |
| pain.002.001.03 | B2C | Payment status report to customer | Outward |

[Bank Identifier Code (BIC) and IBAN](#)

HCT INST payments use IBAN and BIC to identify the bank, branch and beneficiary account.

[Initiating HCT INST Payment](#)

HICT INST payments can be initiated through the following:

|  |  |
| --- | --- |
| Pain.001 | HCT INST payments can be received through pain.001. System supports both single and bulk pain.001. The pain.001 can result in book transfer (beneficiary in the books of the processing bank) or an outward transfer (in this case, pacs.008 is sent to clearing). |
| `PAYMENT``.``ORDER``(PO)` application | Enter the following details in the PO application:   - Ordering customer - Beneficiary customer - Payment amount - Payment currency - Requested execution date or Requested credit value date (calculated based on PO product configuration)   The payment order is validated and the record is committed.    The payment order is authorised and processed as a book or an outward payment depending on where the beneficiary resides. For outward payments, pacs.008 message is generated to be sent to clearing. |



[Rejecting an Instant Payment from GIRO – pacs.002](#)

GIROInst rejects a payment transaction when it fails the content validation. TPH (originator bank) receives a negative final status report from GIRO that has the appropriate reason code for the rejection. The amount is not reserved on the originator bank account.



[Beneficiary Bank Rejects an Instant Payment – pacs.002](#)

Beneficiary bank can reject an instant payment transaction due to content problems. For example, if the bank cannot identify the final beneficiary indicated in the transaction, a negative status report is sent to GIRO (containing the relevant reason code for the rejection). The processing of the instant payment transaction ends when the following events occur:

- GIROInst platform sends out final status reports to the sending and receiving participants about the failure of the transaction.
- Releases the reservation on the originator bank’s account.



[Beneficiary Bank Resends Status Report after Time Out – pacs.002](#)

If the beneficiary bank does not receive a final status report from the GIROInst platform within the time out limit, it resends the original pacs.002 (automated) positive or negative status report to GIROInst from TPH. Depending on the final status of the transaction, the GIROInst response can be delivered again as a positive or negative confirmation message. Resending the status report is only allowed for the beneficiary bank on reaching the time out limit.

This can be resent a maximum of five times.



[Investigation Message Initiated by Originator Bank – pacs.028](#)

If the originator bank does not receive a confirmation message within the time out limit, it sends an investigation message to enquire the status of the original instant payment (pacs.008). The pacs.028 message is sent as an investigation message to GIRO. The investigation message is triggered automatically based on the configuration. The originator bank sends an investigation message only after time out. It can be sent a maximum of five times.

It can be sent a maximum of five times.

If GIROInst can find the transaction referenced in the investigation message (pacs.028), it resends the related final status report. If the transaction cannot be located, the system generates a negative report.



[Generating Recall Request](#)

[Receiving Positive Confirmation Response – camt.056 or pacs.004](#)

A recall request is initiated when originator bank wants to recall a previously settled HCT INST transaction. A recall can only be initiated by the originator bank or by customer’s request. Originator bank can initiate a recall based on the following reasons:

| Reason | Error Code |
| --- | --- |
| Duplication | DUPL |
| Erroneous HCT INST transaction due to technical problem | TECH |
| HCT INST transaction related to fraud | FRAD |

- The beneficiary bank has 30 days to reply to an HCT INST recall initiated by the originator bank.
- Subject to modification with any changes published in the SEPA Rulebook.

Originator bank can recall a transaction based on customer request for the following reasons:

| Reason | Error Code |
| --- | --- |
| Customer transferred the wrong amount | AM09 |
| Customer specified wrong account to credit | AC03 |
| Other reason, not specified by customer | CUST |

The customer of the originator bank can initiate a recall by the last day of the 13th month, since the original transaction. The beneficiary bank needs to reply within 30 days.

Subject to modification with any changes published in the SEPA Rulebook.

If the original beneficiary bank approves the recall, a pacs.004 return transfer message is sent in reply to the recall. GIROInst processes and settles the return transaction instantly and performs the following process:

1. Debits the original creditor bank.
2. Credits the original debtor bank.
3. Forwards the payment return (pacs.004) to the original debtor bank.
4. Sends a final status report (pacs.002) to the original creditor bank, which can be positive or negative status. The positive status report has the return transaction settlement date.
5. The original creditor bank debits the original payee’s account, after receipt of the positive final status report (pacs.002).
6. If the GIROInst settles a payment return (pacs.004), it sends the final status report (pacs.002) simultaneously to both banks (original creditor and debtor bank) that has the settlement date.
7. The original debtor bank can credit the original payer’s account, after receipt of the positive final status report (pacs.002).



[Receiving Negative Confirmation Response – camt.029](#)

If beneficiary bank rejects the recall, a camt.029 (recall rejected) message is sent. GIROInst validates and forwards the rejection message to the original originator bank for further processing. Depending on GIROInst’s validation, a status report (positive or negative) is sent to the original beneficiary bank as a reply.

The report is sent in pacs.002 format.



[Bulking Criteria](#)

HCT INST payment files are sent as individual payments (that is, one transaction for each file) to GIRO.

[Retrieving Original Credit Transfer](#)

During an incoming return the camt.056 or camt.029 message is received and original credit transfer message is retrieved based on the below matching conditions:

- Transaction amount
- Settlement date
- Original transaction ID in the R-Transaction against Transaction ID (original payment)

[Transactions with Missing Final Status Report](#)

During interbank clearing transactions, the banks can debit and credit their customers’ accounts only after receiving final status report (pacs.002) from GIROInst. The related clearing transaction types are as follows:

- Outgoing customer credit transfer (pacs.008 sent to GIRO)
- Incoming customer credit transfer (pacs.008 received from GIRO)
- Outgoing payment return (pacs.004 sent to GIRO)
- Incoming payment return (pacs.004 received from GIRO)

If the final status report cannot reach TPH due to an error, then TPH can process the transaction manually as follows:

- Provides enquiry that enables the user to list the transactions with missing final status report and status awaiting confirmation from the clearing.
- Additionally, enquiry also lists the payments that have exhausted the maximum retry count for sending automated investigation messages.

The missing status enquiry provides an option to manually perform the following:

|  |  |
| --- | --- |
| Reject the transaction (negative acceptance) | If the REJECT option is selected, provide the reason code for rejection. |
| Accept the transaction (positive acceptance) | If the ACCEPT option is selected, enter the new settlement date for the payment. The settlement date can be the current date or backdated. Future date is not allowed. |

- If a pacs.004 return transaction is manually rejected through the enquiry at the beneficiary (creditor), it cancels the funds reserved to re-book the payment and restores the status of the payment to its original status.
- If a payment is manually addressed to accept or reject the payment message, it goes through multiple authorisation levels (4-eyes principle).

[Bulk Initiated Recall Request – camt.056](#)

The user can initiate a bulk cancellation request by performing the following:

- Select multiple credit transfers
- Provide reason code for the cancellation request
- Authorise bulk cancellation request
- Generate camt.056 message

[Unhandled Incoming Recall Requests beyond a Time Limit](#)

Beneficiary bank has 30 business days to respond to incoming recall request (positive or negative). As part of COB, TPH sends the automatic rejection when incoming recall requests are not handled within the specified time limit.

- Bank configures 30 calendar days.
- Recall is received on 1st July.
- No response is received till 31st July end of day.
- COB process runs on 31st July.
- As part of COB, date is changed as 1st August.
- Recall request status is updated to REJECTED and camt.029 is sent.

## Duplicate Check

TPH performs duplicate check for an incoming pacs.008 and pacs.004 message based on the following:

- Transaction ID
- Transaction Type
- Transaction that is unique for 7 days

## Illustrating Model Parameters

To know more on parameter setup for Hungary Instant Payments, refer to [Temenos Payments Hub (PP)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Initiation (PI)](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm).

## Illustrating Model Products

HCT Instant module can send and receive HCT Instant payments in Hungary clearing.

In this topic

- [Introduction to Hungary Instant Credit Transfer (HCT INST) Payments](#IntroductiontoHungaryInstantCreditTransferHCTINSTPayments)

- [Duplicate Check](#DuplicateCheck)
- [Illustrating Model Parameters](#IllustratingModelParameters)
- [Illustrating Model Products](#IllustratingModelProducts)

Related topics:

- [APIs](../../APIs/Misc/APIs.htm#EP)
- [Temenos Payments Hub](../../Payments_Hub_(PP)/Misc/Introduction.htm)
- [Payments Initiation](../../Payment_Initiation_(PI)/Misc/Introduction_PI.htm)
- [Clearing Directory](../../Clearing_Directory_(CA)/Misc/Introduction.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:18:43 PM IST