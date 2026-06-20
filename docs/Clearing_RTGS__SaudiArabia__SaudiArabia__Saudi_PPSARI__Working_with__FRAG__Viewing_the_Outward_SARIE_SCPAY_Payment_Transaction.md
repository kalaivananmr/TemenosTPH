# Working with Saudi Arabian Riyal Interbank Express (SARIE) - Viewing The Outward Sarie Scpay Payment Transaction

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/SaudiArabia/SaudiArabia/Saudi_PPSARI/Working_with.htm#Viewing_the_Outward_SARIE_SCPAY_Payment_Transaction

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Saudi Arabia > [Saudi Arabia Riyal Interbank Express (SARIE)](../../SaudiArabia/Saudi_PPSARI/Introduction.htm) > Working with

- Saudi Arabia;)
  - [Saudi Arabia Riyal Interbank Express (SARIE) Saudi Arabia Riyal Interbank Express (SARIE)](../../SaudiArabia/Saudi_PPSARI/Introduction.htm)
    - [Introduction](../../SaudiArabia/Saudi_PPSARI/Introduction.htm)
    - [Configuration](../../SaudiArabia/Saudi_PPSARI/Configuration.htm)
    - [Working with](../../SaudiArabia/Saudi_PPSARI/Working_with.htm)
    - [Tasks](../../SaudiArabia/Saudi_PPSARI/Tasks.htm)
    - [Outputs](../../SaudiArabia/Saudi_PPSARI/Outputs.htm)
  - [Saudi Arabia Instant Payments System (SAIPS) Saudi Arabia Instant Payments System (SAIPS)](../../SaudiArabia/Saudi_Instant_Payments_System_PPISIP/Introduction.htm)

Payments

# Working with Saudi Arabian Riyal Interbank Express (SARIE)

Updated On 06 October 2022 |
 4 Min(s) read

Feedback
Summarize

This section helps the user to understand the working of SARIE.

## Manual Capture of SARIE Single Customer Payment

1. To capture a payment, go to **User Menu**>**Payments**>**Payment Order**>**Input Payment Order**>**Payment Order – SARIE.CTR.INPUT**.



2. To manually authorise the payment, go to **User Menu**>**Payments**>**Payment Order**>**Authorise/Delete Payment Order** (PO.UNAUTH.TXN).



## Viewing the Payment Enquiries

To enquire the payment, perform the following:

1. Go to **User Menu**>**Payments**>**Payment Hub**>**Payment Inquiries**>**Pending and Processed Payments**>**Pending Process Payments – Transaction-wise**.



2. To view the detailed view of the payment, click .






## Viewing the Received Files or Messages

To view received files or messages, perform the following:

1. Go to **User Menu**>**Payments**>**Payments Hub**>**Payment Inquiries**>**Received and Sent File Details**>**Received Files Details**>**Received Message/File Details List**.

The enquiry output is split into three sections as shown below.

| Section | Screenshot |
| --- | --- |
| Received File Details |  |
| Received Bulk Details |  |
| Received Message Details |  |

## Viewing the Output Payment Files

To view sent files, perform the following:

1. Go to **User Menu**>**Payments**>**Payments Hub**>**Payment Inquiries**>**Received and Sent File Details**>**Sent File Details**.

The enquiry output is split into three sections as shown below.

| Section | Screenshot |
| --- | --- |
| Sent File Details |  |
| Sent Bulk Details |  |
| Sent Message Details |  |

## Viewing the SCPAY Clearing Directory Records

To view clearing directory, perform the following:

1. Go to **Admin Menu**>**Framework Parameter**>**Clearing Directory**>**Search Clearing Directory** (CA.CLEARING.DIRECTORY).



2. In the list of records, select the required ID to view the details.






## Viewing the Outward SARIE SCPAY Payment Transaction

To view outward SARIE failed transaction in the Repair queue, perform the following:

1. Go to **User Menu**>**Payments**>**Payment Hub**>**Payment Inquiries**>**Pending Payments**>**Pending Repair Payments**.



2. To view the details of a particular outward SARIE failed transaction, click .






3. To view the debit credit details of the failed transaction, click the **Debit Credit Info** tab.



4. To view the error details of the failed transaction, click the **Error Information** tab.



The user can repair or cancel a transaction in the Repair page by selecting the appropriate value in *Return/Reject Payment* field.



## Viewing the Inward SARIE SCPAY Payment Transaction

To view the inward SARIE failed transaction in the Repair queue, perform the following:

1. Go to **User Menu**>**Payments**>**Payment Hub**>**Payment Inquiries**>**Pending Payments**>**Pending Repair Payments**.



2. To view the details of a particular inward SARIE failed transaction, click .



3. To view the error details of the failed transaction, click the **Error Information** tab.



## Viewing the Mapped MT298/12 or MT298/35

To view mapped MT298/12 or MT298/35 by using the Field 20 (FTNumber) of the message, perform the following:

- Go to **User Menu**>**Payments**>**Payment Hub**>**Payment Inquiries**>**Received and Sent File Details**>**Received File Details**>**Received Message/File Details List**.



## Viewing the Enquiry with Tag 20 Invalid in MT298

1. To view unmatched MT 298, go to **User Menu**>**Payments**>**Payment Hub**>**Payment Inquiries**>**Received and Sent File Details**>**Received File Details**>**Received Message/File Details List**.



2. To enquire for mismatch or invalid file in tag20 of SARIESR (MT298/12 or MT298/35) message, search for SARIE in *Channel* field and UNMATCHED in *File Status* field.




The list of received messages or files is displayed.



In this topic

- [Working with Saudi Arabian Riyal Interbank Express (SARIE)](#WorkingwithSaudiArabianRiyalInterbankExpressSARIE)

- [Manual Capture of SARIE Single Customer Payment](#ManualCaptureofSARIESingleCustomerPayment)
- [Viewing the Payment Enquiries](#ViewingthePaymentEnquiries)
- [Viewing the Received Files or Messages](#ViewingtheReceivedFilesorMessages)
- [Viewing the Output Payment Files](#ViewingtheOutputPaymentFiles)
- [Viewing the SCPAY Clearing Directory Records](#ViewingtheSCPAYClearingDirectoryRecords)
- [Viewing the Outward SARIE SCPAY Payment Transaction](#ViewingtheOutwardSARIESCPAYPaymentTransaction)
- [Viewing the Inward SARIE SCPAY Payment Transaction](#ViewingtheInwardSARIESCPAYPaymentTransaction)
- [Viewing the Mapped MT298/12 or MT298/35](#ViewingtheMappedMT29812orMT29835)
- [Viewing the Enquiry with Tag 20 Invalid in MT298](#ViewingtheEnquirywithTag20InvalidinMT298)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:21:38 PM IST