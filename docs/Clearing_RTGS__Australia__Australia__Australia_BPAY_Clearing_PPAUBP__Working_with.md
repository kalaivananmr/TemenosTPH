# Working with BPAY Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Australia/Australia/Australia_BPAY_Clearing_PPAUBP/Working_with.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Australia > [BPAY](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm) > Working with

- Australia;)
  - [BPAYBPAY](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm)
    - [Introduction](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm)
    - [Configuration](../../Australia/Australia_BPAY_Clearing_PPAUBP/Configuration.htm)
    - [Working with](../../Australia/Australia_BPAY_Clearing_PPAUBP/Working_with.htm)
    - [Tasks](../../Australia/Australia_BPAY_Clearing_PPAUBP/Tasks.htm)
    - [Outputs](../../Australia/Australia_BPAY_Clearing_PPAUBP/Outputs.htm)
  - [BECSBECS](../../Australia/Australia_BECS_PPBECS/Introduction.htm)
  - NPP Payments;)
  - BPAY Agency Banking;)
  - AURTGS Clearing;)
  - DE (BECS) Agency Banking;)
  - Clearing Directory Upload and Reachability Check;)

Payments

# Working with BPAY Clearing

Updated On 07 August 2025 |
 2 Min(s) read

Feedback
Summarize

This section helps the user to understand the working of BPAY.

## Manual Capture by Using `PO` Application

1. To capture BPAY bill payments, go to **User Menu**>**Payments**>**Payment Order Menu**>**Input Payment Order**>**Payment Order**>**Payment Order – Australian BPAY**.
2. Perform the following actions:
   - Validate the payment details (entered by the user) by invoking BPAY Clearing APIs (L2 enhancement).
   - On successful validation, it is sent for Supervisor’s approval.
   - On approval, it releases the payment to STP processing flow.







[Payment Awaiting Authorisation](#)






[Payment Authorised Successfully](#)



## Generation of BPAY Outgoing File

The following file (sample) is generated and sent to Clearing:



## Generation of Null File (when payment is not sent to BPAY)

The following file is generated when payment is not sent to BPAY:



## BPAY Payments Enquiry

The user needs to perform the following:

1. To view BPAY payments, go to **User Menu**>**Payments**>**Payment Hub**>**Payment Inquiries**>**Pending and Processed Payments**.
2. To filter BPAY payment, search for BPAY in *Channel*.

   It also allows to apply advanced filters on payment attributes.



## BPAY Payment Returns Enquiry

To view BPAY payments, go to **User Menu**>**Payments**>**Payment Hub**>**Payment Inquiries**>**Pending and Processed Payments**. It matches the return payment (received) with original payment and moves it to 999 (Complete) status and credits back to the customer account.



Moves the original transaction to 996 (Completed with Return) status.



In this topic

- [Working with BPAY Clearing](#WorkingwithBPAYClearing)
  - [Manual Capture by Using PO Application](#ManualCapturebyUsingPOApplication)
  - [Generation of BPAY Outgoing File](#GenerationofBPAYOutgoingFile)
  - [Generation of Null File (when payment is not sent to BPAY)](#GenerationofNullFilewhenpaymentisnotsenttoBPAY)
  - [BPAY Payments Enquiry](#BPAYPaymentsEnquiry)
  - [BPAY Payment Returns Enquiry](#BPAYPaymentReturnsEnquiry)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Wednesday, June 17, 2026 2:21:50 PM IST