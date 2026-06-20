# Introduction to BPAY Clearing - Introductiontobpayclearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Australia/Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm#IntroductiontoBPAYClearing

---

# Introduction to BPAY Clearing

Updated On 07 August 2025 |
 5 Min(s) read

Feedback
Summarize

BPAY is an electronic bill payment system in Australia. It enables to make payments to organisations registered as BPAY billers, through a bank's online, mobile or telephone banking facility. A biller number is allocated to a business that is registered with BPAY. The customer making a payment needs to log on to the bank’s portal and enter the Biller Code, Customer Reference Number and Transaction Amount. On successful validation, the customer’s bank transfers the funds electronically to the biller’s bank.

## BPAY Participants

The following are the types of BPAY participants:

- Bill payer’s bank
- Biller’s bank
- BPAY clearing

## Types of Payment and Messages

TPH supports the following BPAY message types:

| Message | Description | TPH Support |
| --- | --- | --- |
| BPAYPDF | Payer Detail File | Outward |
| BPAYRTN | BPAY Return File | Inward |

The BPAY message workflow is shown below.



## BPAY Cut-Off Time

When TPH process the bill payments, it sends the Payer Detail File (PDF) to Clearing. Clearing then forwards the file to the billers’ banks to credit their accounts with the bill payments. This PDF file is sent to the clearing two times a day (at 3.30 PM and 7.15 PM Sydney time). If instructions are not available in the file, it sends NULL file within the cut-off times with a blank header and footer.

## Outward Bill Payment Processing



| Activity | Description |
| --- | --- |
| Manual capture of bill payment from branch or back-office by using Payment Order page | Captures bill payments from PO application page and enters the Biller Code, CRN, Bill Amount by using the BENEFICIARY table. Performs the following on selecting the Beneficiary ID:  - Defaults the Biller Code and CRN - Invokes an API from BPAY clearing to retrieve biller information (such as Biller Name)  Additionally, if the CRN flag returned by the API is ‘Y’, it removes the CRN number in the page (if any). The user needs to enter the variable CRN to continue the bill payment. |
| Biller code, CRN and payment method validations | Triggers a synchronous API call to BPAY clearing (validate BPAY payment) and validations the payment, when the user enters the Commit button () in the Payment Order page.  - If the clearing API returns an error, it is displayed on the page. - If there are no errors, the bill payment is successfully submitted to TPH for further processing. |
| Account validations | Validates whether the ordering account has the following:  - A valid Temenos Transact account - No posting restrictions - Sufficient balance to cover the bill payment |
| Balance reservation | Reserves the balance in the debit account for the bill amount. |
| Routing and channel cut-off | Determines the routing channel based on the product setup for the bill payment and does other channel validations (such as cut-off check). |
| Debit posting | If the validations are successful, system passes the accounting entries by debiting the customer account and crediting the clearing suspense account. |
| Generation of the Payer Detail File (PDF) | Collates all bill payments parked in a status (to be sent to BPAY) and forms a PDF (flat file) in the clearing specification (to be sent to clearing based on the cut-off time defined in the system). If bill payments are not generated in the system at the designated cut-off time, it sends a null (blank) file (with header and footer) to BPAY. |

## Inward Bill Payment Reject Processing



| Activity | Description |
| --- | --- |
| Reject file received in TPH | Validates whether the reject file is in the correct format and then accepts it. |
| Return processing | Checks whether the original bill payment can be found based on a combination of the Biller Code, CRN, Transaction Reference and Channel.  Additionally, checks if the return is received within the allowed days for return configured in the system. |
| Credit account validations | Validates the credit account in the core banking system for posting restriction, closure, and other validations. |
| Posting | If the original is found and validated, TPH passes the accounting entry to debit the returns suspense and credit the customer’s account for the bill payment return. |

## Illustrating Model Parameters

Read the [Payment Hub (PH)](../../Payments_Hub_(PP)/Misc/Introduction.htm), [Payment Suite (PH)](../../Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm) and [Clearing Directory (CA)](../../Clearing_Directory_(CA)/Misc/Introduction.htm) for information on parameter setup for BPAY outward bill payments and Inward returned bill payment.

## Illustrating Model Products

BPAY Clearing Australia module provides the facility to send Outward Bill Payments and Inward Returned Bill Payments.