# Working with Jordan RTGS

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Jordan/Jordan/Jordan_PPJDNC/Working%20with.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Jordan > [Jordan RTGS](../../Jordan/Jordan_PPJDNC/Introduction.htm) > Working with

- Jordan;)
  - [Jordan RTGS Jordan RTGS](../../Jordan/Jordan_PPJDNC/Introduction.htm)
    - [Introduction](../../Jordan/Jordan_PPJDNC/Introduction.htm)
    - [Configuration](../../Jordan/Jordan_PPJDNC/Configuration.htm)
    - [Working with](../../Jordan/Jordan_PPJDNC/Working with.htm)
    - [Tasks](../../Jordan/Jordan_PPJDNC/Tasks.htm)
    - [Outputs](../../Jordan/Jordan_PPJDNC/Outputs.htm)

Payments

# Working with Jordan RTGS

Updated On 08 November 2022 |
 4 Min(s) read

Feedback
Summarize

This section helps the user to understand how to manually capture bank and customer transfers. Additionally, it enables to view Jordan RTGS payments enquiries and output messages.

## Capturing the Bank Transfers Manually

The user can capture bank transfers from its Order Entry (OE) page in TPH. The OE payments allow an Operator to impose a number of values which override the configuration in the payment engine. Bank transfers are initiated by back-office users.

The OE page in TPH is a generic Payment Order capture page and not specific to Jordan RTGS.

1. Go to **User Menu**>**Payments**>**Payment Hub**>**Initiate Payment Transaction**>**Initiate Bank Transfer**>**Outgoing Transfer**.
2. Enter the required details in the following fields:

| Field | Type | Mandatory (M)/Optional (O) | Remarks |
| --- | --- | --- | --- |
| Priority | Numeric | M | Any value from 1 to 9 can be populated. It depends on the bank’s requirement.  The input value is prefixed with 000 and populated in tag 113 – priority code of the outgoing SWIFT message. |
| Output Channel | Text | O | JO – RTGS channel can be selected and imposed while capturing the payment.  If channel is not imposed, the system selects JO – RTGS channel automatically during Product Determination. |
| Transaction Currency | Currency | M | Currency needs to be JOD |
| Transaction Amount | Amount | M | Amount can be any valid amount and there is no maximum limit |
| Execution Date | Date | O |  |
| Receiver Institution | Text | M | Needs to be a valid BIC |
| Debit Account Number | Account Number | M |  |
| Debit Account Address |  | M |  |
| Debtor Agent Bank |  | M | Bank Identification Code (BIC) |
| Intermediary Institution Account |  | O |  |
| Intermediary Institution Address |  | O |  |
| Intermediary Institution Bank Code |  | O | BIC |
| Account with Institution Bank Code |  | O | BIC |
| Account with Institution Address |  | O |  |
| Beneficiary Bank BIC | Text | M | If Receiver Institution is not provided, this field is mandatory. |
| Beneficiary Account | Account Number | M | Maximum of 34 characters |
| Beneficiary Name | Text | M | Maximum of 70 characters |
| Beneficiary Bank Address |  | O |  |
| Additional Information |  | O | Sender to Receiver information |

## Capturing Customer Transfers Manually

The user can capture customer transfers from its OE page in TPH. The OE payments allow an Operator to impose a number of values, which overrides the configuration in the payment engine.

The OE page in TPH is a generic Payment Order capture screen and not specific to JO − RTGS.

1. Go to **User Menu**>**Payments**>**Payment Hub**>**Initiate Payment Transaction**>**Initiate Customer Transfer**>**Outgoing Transfer**.
2. Enter the required details in the following fields:

| Field | Type | Mandatory (M)/Optional (O) | Remarks |
| --- | --- | --- | --- |
| Charge Option | Text | O | BEN, SHA and OUR |
| Charges |  | O | Amount, currency and account details |

## Viewing the Payment Enquiry

The user can view Jordan RTGS payments in TPH by using the standard ‘Pending and Processed Payments’ enquiry.

To view Jordan RTGS payment, search for JORTGS in Channel.



It also allows advanced filtering on payment attributes (if required).

The results grid is shown below.



A detailed view of the payment is shown below.







## Viewing the Output Message

The user can select the required payment, generate and view its output message. To perform this, do the following:

1. Go to **User Menu**>**Payments**>**Payments Hub**>**Payment Inquiries**>**Pending and Processed Payments**>**Pending Process Payments – Transaction wise**.
2. To view the details, select ‘ViewInDetail’ for the respective transaction.
3. To generate its output message, from the Options drop-down click Outgoing Message.



In this topic

- [Working with Jordan RTGS](#WorkingwithJordanRTGS)

- [Capturing the Bank Transfers Manually](#CapturingtheBankTransfersManually)
- [Capturing Customer Transfers Manually](#CapturingCustomerTransfersManually)
- [Viewing the Payment Enquiry](#ViewingthePaymentEnquiry)
- [Viewing the Output Message](#ViewingtheOutputMessage)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:19:03 PM IST