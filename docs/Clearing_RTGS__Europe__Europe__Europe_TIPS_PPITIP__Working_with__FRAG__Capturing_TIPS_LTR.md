# Working with Target Instant Payment Settlement (TIPS) - Capturing Tips Ltr

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Europe/Europe/Europe_TIPS_PPITIP/Working_with.htm#Capturing_TIPS_LTR

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Europe > [Target Instant Payment Settlement](../../Europe/Europe_TIPS_PPITIP/Introduction.htm) > Working with

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

# Working with Target Instant Payment Settlement (TIPS)

Updated On 08 February 2024 |
 12 Min(s) read

Feedback
Summarize

This section helps the user to understand the working of TIPS.

## Capturing a TIPS Payment

- To initiate a SEPA payment, go to **User Menu** > **Payments** > **Payment Order** > **Input Payment Order** > **Domestic Plus**.
  The amount, debit account, beneficiary details (along with beneficiary BIC) are defined as shown in the below screenshot. It captures the below information in the payment order

  To initiate TIPS payment from the Domestic Plus screen, user should select INST as value for the *Payment Level Service Code* field.




- To authorise the payment order, go to **User Menu**>**Payments**>**Payment Order Menu**>**Authorise/Delete Payment Order**.

## Viewing Completed SEPA Instant Payments

The user can view the completed SEPA Instant Payments by using the standard Pending and Processed Payments enquiry. TPH allows users to filter the payments by searching the *Output Channel* as TIPS.



## Capturing TIPS LTR

This section describes the capturing of LTR in TIPS.

[Initiating and Authorizing LTR from `Payment.Order` (PO)](#)

Perform the following steps to initiate a LTR for TIPS from PO:

1. Go to **User Menu** > **Payments** > **Liquidity Management** > **Front Office** > **LTR Initiation** > **LTR Initiation**.
2. Select TIPSPAYLTR from the *Payment Order Product* dropdown and enter TIPS in the *Output Channel* field along with capturing the amount, execution date, debit account, external debit account, credit account, external credit account, amount, currency and so on. Read [Liquidity Transfer Request](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Request/Working_with.htm#Capturing_LTR_from_PO_Application) user guide for more information on the data to be entered in each field.
3. Click  after providing the required details.
4. Click after validation.



Perform the following steps to authorise the TIPS LTR payment order:

1. Go to **User Menu** > **Payments** > **Liquidity Management** > **Front Office** > **LTR Authorise/Delete** > **Authorise/Delete LTR Payments**.
2. Click  on the transaction to be authorized. The payment details are displayed in read-only mode for the supervisor to view.
3. Click  to authorise.

[Initiating and Authorizing LTR from Order Entry (OE)](#)

Perform the following steps to initiate a LTR from OE:

1. Go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **LTR** > **LTR Initiation** > **LTR Initiation**.
2. Enter TIPS in the*Output Channel* field along with capturing the amount, execution date, debit account, external debit account, credit account, external credit account, amount, currency and so on. Refer [Liquidity Transfer Request](../../Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Request/Working_with.htm#Capturing_LTR_from_OE_Application) user guide for more information on the data to be entered in each field.



3. Click  to validate the entered details and derive the internal account or external account details. The user can modify the details and re-validate if there is any error.
4. Click. The payment is submitted and sent for supervisor’s approval.

Perform the following steps to authorise the payment:

1. Go to **User Menu** > **Payments** > **Liquidity Management** > **Front Office** > **LTR Authorise/Delete** > **Authorise/Delete LTR Payments**.
2. Click  on the transaction to be authorized. The payment details are displayed in read only mode for the supervisor to view.
3. Click  to authorise.

On approval, the payment is processed, accounting entries are posted and the LTR payment message (camt.050) is generated and sent to TIPS.

[Viewing TIPS LTRs initiated from PO](#)

To view the TIPS LTRs initiated in PO, go to **User Menu** > **Payments** > **Liquidity Management** > **Front Office** > **LTR** > **LTR Enquiries**.

Filter the LTR payment that needs to be viewed as shown below:



[Viewing TIPS LTRs initiated from OE](#)

To view the TIPS LTRs, go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **LTR** > **LTR Enquiries** > **View LTR Payments**.

Filter the LTR payment that needs to be viewed as shown below:



[Repairing TIPS LTR Payment](#)

To view the payments waiting for repair, go to **User Menu** > **Payments** > **Liquidity Management** > **Back Office** > **LTR** > **LTR Exceptions** > **LTR Repair Queue**.

It moves the payment to repair state (status = 235), if there is an error while processing LTR payments.

Filter the LTR payment that needs to be repaired as shown below:



Refer [Liquidity Transfer Request](https://docs.temenos.com/docs/Solutions/Payments/Payments/LQ/Payments_Hub_(PP)/Liquidity_Transfer_Request/Introduction.htm) user guide for more information on capturing, viewing and repairing LTRs.

## Viewing Payments Awaiting Confirmation

The user can view the payments awaiting confirmation from clearing. To perform this, do the following actions:

- Go to **User Menu**>**Payments**>**Payments Hub**> **Instant Payments**>**Pending and Processed Instant Payments** (with filter on Channel = TIPS).



## Viewing a Payment Received From IP in TPH (as DP) Redirected to TIPS Clearing

The user can view the payments received from an IP. To perform this, do the following actions:

1. Go to **User Menu**>**Payments**>**Payments Hub**>**Instant Payments**>**Pending and Processed** enquiry (with filter on Channel = TIPS).
2. Set the *Direction* field as R (Redirect), as the originating source criteria is the name of the IP channel.

   This is an optional field.

## Viewing Cancellation Requests Sent Out

To view the status of the recall requests sent out, go to **User Menu**>**Payments**>**Payments Hub**>**Instant Payments**>**Instant Payment Cancellations**>**Create cancellation request**>**Outward Cancellation Req-View Status**.

The status of the recall requests are as follows:

- Accepted – CANCELACCEPTED
- Rejected – CANCELREJECTED
- Sent – CANCELLATIONSENT

## Viewing Cancellation Request from Counterparty Bank

To view the status of the recall request received in TPH from the counterparty banks, go to **User Menu**>**Payments**>**Payments Hub**>**Instant Payments**>**Instant Payment Cancellations**>**Create cancellation request**>**Inward Cancellation Request - View Status**.

The status of the requests are as follows:

- Recall requests in progress – INWORK
- Rejected recall request – REJECTED
- Successfully processed recall request – CANCELACCEPTED

If the beneficiary lies with the Indirect Participant (IP), a camt.056 is forwarded automatically to the IP and the status of the inward cancellation request is set as ‘FORWARDED’.

## Initiating Investigation Message

To initiate status request or investigation (pacs.028) for an already sent cancellation request (camt.056), go to **User Menu**>**Payments**>**Payments Hub**>**Instant Payments**>**Instant Payment Cancellations**>**Outward Cancellation - Req Update**.



## Investigations

[Sending Investigations](#)

If TPH does not receive any confirmation for the instant payment from clearing, the user can initiate an investigation message to the clearing. To perform this, do the following actions:

1. Go to **User Menu**>**Payments**>**Payment Hub**>**Instant Payments**>**Investigation & Reversal**>**Unconfirmed Instants Payments**>**Unconfirmed - Exp Time Out/All**.
2. Select the Send Inquiry or Investigation option.

[Viewing Automatic Investigations Sent Out](#)

TPH can be configured to automatically send an investigation message to the clearing when confirmation is not received within the configured time (in seconds). The user can view initiation details of the automatic investigations. To perform this, do the following actions:

- Go to **User Menu**>**Payments**>**Payment Hub**>**Instant Payments**>**Pending and Processed Instant Payments**> **Pending and Processed Inst Payments**>**View in Detail** (Audit Trail dropdown).






[Viewing Investigations from Clearing](#)

- To view the investigations received from clearing (status as INVESTIGATED), go to **User Menu**>**Payments**>**Payment Hub**>**Instant Payments**>**Investigation & Reversal**>**Unconfirmed Instant Payments**>**Inward Investigation - Repair**>**Payment Investigations**>**Payment Investigations** (Investigations).

  If the original transaction is not found, then TPH sends a negative confirmation to clearing (pacs.002).
- To view the details of this message, go to **User Menu**>**Payments**>**Payment Hub**>**Instant Payments**>**Pending and Processed Instant payments**> **Pending and Processed Inst Payments**>**View in Detail** (*Audit Trail* drop-down).

  TPH also updates the status of the inward investigation as INVSTREJECTED.

[Viewing Investigations from IPs banks](#)

An investigation message (pacs.028) is received from the IP for a processed payment. TPH sends a positive confirmation (pacs.002) to IP as it is already processed. This enables the user to view the investigations received from IP (status as INVESTIGATED). To perform this, do the following actions:

- Go to **User Menu**>**Payments**>**Payment Hub**>**Instant Payments**>**Investigations**>**Payment Investigations**>**Payment Investigations (Investigations)**.

## Processing Returns and Recalls

This section helps the user to understand the processing of returns and recalls.

[Cancelling a Processed Payment](#)

1. Go to **User Menu**>**Payments**>**Payments Hub**>**Instant Payments**>**Instant Payment Cancellations**>**Create Cancellation Request**>**Customer Initiated Cancellation Request**.
2. Enter the FT Number of the instant payment that needs to be cancelled and then select the Cancel by Originator option.

   Once the payment is cancelled, the status of other payments in the same enquiry is displayed.
3. Enter the appropriate ISO reason code to initiate the bank initiated or customer-initiated recall requests.

   Similarly, TPH allows users to generate positive (pacs.004) or negative (camt.029) responses on Incoming Cancellation Requests by providing appropriate the ISO reason code.

[Viewing Cancellation Requests Sent Out](#)

To view the status of the recall requests sent out, go to **User Menu**>**Payments**>**Payments Hub**>**Instant Payments**>**Instant Payment Cancellations**>**Create Cancellation Request**>**Outward Cancellation Req-View Status**.

The status of the recall requests are as follows:

- Accepted – CANCELACCEPTED
- Rejected – CANCELREJECTED
- Sent – CANCELLATIONSENT

[Viewing Cancellation Request from Counterparty Bank](#)

The status of the inward recall requests are as follows:

- Recall requests in progress – INWORK
- Rejected recall request – REJECTED
- Successfully processed recall request – CANCELACCEPTED

If the beneficiary lies with the IP, then a camt.056 is forwarded (automatically) and status of the inward cancellation request is set as FORWARDED.

[Initiating Investigation Message](#)

To initiate status request or investigation (pacs.028) for an already sent cancellation request (camt.056), go to **User Menu**>**Payments**>**Payments Hub**>**Instant Payments**>**Instant Payment Cancellations**>**Outward Cancellation - Req Update**.



[](#)[Viewing TIPS Clearing Directory Records](#)

To view the records in the clearing directory, go to **Admin Menu**>**Framework Parameter**>**Clearing Directory**>**Search Clearing Directory TIPS**.



[Uploading Clearing Reports](#)

To upload the camt.053 received through EB.FILE.UPLOAD, set *Upload Type* as TIPSSOA. The status changes to ‘Uploaded’ after it is successfully uploaded.



[Viewing Statement of Accounts Received from TIPS](#)

To view the report received for the day, perform the following:

1. Go to **User Menu**>**Payments**>**Payment Hub**>**Payment Inquiries**>**Reports**>**Local Clearing Report**>**TIPS Clearing SOA Report**.
2. To filter the reports, enter the required details in the following fields:

| Field | Description |
| --- | --- |
| *File Reference* | Identification of the file received from TIPS |
| *Received Date Time* | Date and time at which the file is received |



The above fields are non-mandatory, as it displays the files even without the filter.

Some reports and related information is described below:

[Statement of Account List](#)

Lists the files received from the master enquiry. To view the details of individual files, click .



[Statement Summary](#)

Lists the details of statements (such as Opening Balance, Closing Balance) available in the file.



[Transaction Summary](#)

Helps the user to view the transaction summary (such as Transaction Reference, Amount), click  in Statement Summary. Both liquidity transfer and instant payment transaction details are available. The *Trnx Recon Status* field matches the *Transaction Reference* with the details available in system.

- If the details match, it displays .
- If not, it displays .



In this topic

- [Working with Target Instant Payment Settlement (TIPS)](#WorkingwithTargetInstantPaymentSettlementTIPS)

- [Capturing a TIPS Payment](#CapturingaTIPSPayment)
- [Viewing Completed SEPA Instant Payments](#ViewingCompletedSEPAInstantPayments)
- [Capturing TIPS LTR](#CapturingTIPSLTR)
- [Viewing Payments Awaiting Confirmation](#ViewingPaymentsAwaitingConfirmation)
- [Viewing a Payment Received From IP in TPH (as DP) Redirected to TIPS Clearing](#ViewingaPaymentReceivedFromIPinTPHasDPRedirectedtoTIPSClearing)
- [Viewing Cancellation Requests Sent Out](#ViewingCancellationRequestsSentOut)
- [Viewing Cancellation Request from Counterparty Bank](#ViewingCancellationRequestfromCounterpartyBank)
- [Initiating Investigation Message](#InitiatingInvestigationMessage)
- [Investigations](#Investigations)
- [Processing Returns and Recalls](#ProcessingReturnsandRecalls)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 4:18:40 PM IST