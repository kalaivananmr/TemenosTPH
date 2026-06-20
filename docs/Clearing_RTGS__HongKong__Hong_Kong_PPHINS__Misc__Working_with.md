# Working with Hong Kong Faster Payments System (HK FPS)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/HongKong/Hong_Kong_PPHINS/Misc/Working_with.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Hong Kong > [Hong Kong FPS](../../Hong_Kong_PPHINS/Misc/Introduction.htm) > Working with

- Hong Kong;)
  - [Hong Kong FPSHong Kong FPS](../../Hong_Kong_PPHINS/Misc/Introduction.htm)
    - [Introduction](../../Hong_Kong_PPHINS/Misc/Introduction.htm)
    - [Configuration](../../Hong_Kong_PPHINS/Misc/Configuration.htm)
    - [Working with](../../Hong_Kong_PPHINS/Misc/Working_with.htm)
    - [Tasks](../../Hong_Kong_PPHINS/Misc/Tasks.htm)
    - [Outputs](../../Hong_Kong_PPHINS/Misc/Outputs.htm)
  - HKICL Cheque Clearing;)
  - CHATS MX Clearing;)
  - FPS Batch Clearing;)
  - CHATS Clearing Directory Upload and Reachability Check;)
  - HKFPS Instant and Batch Clearing Directory;)

Payments

# Working with Hong Kong Faster Payments System (HK FPS)

Updated On 07 August 2025 |
 6 Min(s) read

Feedback
Summarize

This section helps the user to understand the working of Hong Kong Faster Payment System (HK FPS).

## Capturing a HK FPS Payment Manually

The user can initiate an HK FPS payment in `PO` application. To perform this, do the following:

1. Go to **User Menu**>**Payments**>**Payment Order**>**Input Payment Order**>**Payment Order HK FPS**.



The user can initiate both instant (Type C1) and near-real time instant (Type C2) payment using the Payment Order page.

2. Enter the required details in the following fields:

| Field Name (Label) | Type | M/O | Remarks |
| --- | --- | --- | --- |
| **Main Version Page** | | | |
| *Payment Order Product* | Fixed value ‘HKFPSINST’ | M | Defaulted and disabled |
| *End to End Reference* | Text | O | Allows maximum of 35 characters |
| *Payment Type* | INST or INSTNT01 | M | Select one of the following:  - INST – Type C1 payment - INSTNT01 – Type C2 payment |
| *Payment Sub Type Code* | PERFORM\_PYE\_VR or SKIP\_PYE\_VR | M | Select from the drop-down |
| *Payment Amount* | Amount and currency | M | Select the currency as one of the following: HKD or CNY Does not allow the user to select other currencies. |
| *Payment Date* | Date | M | Defaulted to current business date and disabled Mapped to *Acceptant Date Time*, *Credit Value Date* and *Debit Value Date* field in the `PO` application. When mapping to *Acceptant Date Time* field, use the current time (though time is not used for processing) |
| Instructed Amount | Amount and currency | O | Allows to choose only non HKD or CNY currencies |
| Exchange Rate | Rate | O | System calculated |
| Initiating Party | Organisation or private identification | O |  |
| Originating Customer Address |  | O | Allows maximum of 70 characters |
| Originating Customer Name |  | M | Allows maximum of 40 characters |
| Originating Customer Account Number | Local account number | M | Allows maximum of 34 characters |
| Originating Customer Account IBAN | IBAN | O |  |
| Originating Customer’s Bank (NCC) | Clearing code | M |  |
| Originating Customer’s Bank | BIC | O |  |
| Beneficiary ID | Standard Temenos Transact field | O | Select from the drop-down |
| Beneficiary’s Bank NCC | Clearing Code | M |  |
| Beneficiary’s Bank BIC |  | O |  |
| Beneficiary’s Address |  | O | Allows a maximum of 70 characters |
| Beneficiary Account No | Account Number | C | This field is mandatory, when the *Alias Type* field is set as BBAN. If not, it is not mandatory. |
| Beneficiary’s Proxy ID | Credit Card Number, Mobile Number, Emai ID or FPS ID | C | Allows maximum of 34 characters This field is not mandatory, when the *Alias Type* field is set as BBAN. If not, it is mandatory. |
| Beneficiary Account IBAN | IBAN | O |  |
| Beneficiary Proxy id type | Can be selected | M | BBAN, AIN, EMAL, MOBN or CUST Allows only BBAN, and CUST and AIN for manual capture Mapped to *Alias Type* field |
| Beneficiary Account Name |  | M | Allows maximum of 40 characters |
| Purpose of Payment | Drop-down with predefined set of ISO purpose codes | O |  |
| **Charge Details (Sub Tab)** | | | |
| Charge Bearer | SHA | M | Defaulted to `PO` application product setup |
| Charges | Amount and currency | C | System calculated (through TPH simulation) |
| **Remittance Information (Sub Tab)** | | | |
| *Remittance Information**(Unstructured)* | Free text | O | Allows maximum of 140 characters |
| *Regulatory Reporting Information* | Free text | O | Allows maximum of 35 characters |
| *Remittance Info Structured - Creditor Reference* | Free text | O | Allows maximum of 35 characters |
| *Ordering Party Reference* |  | O | Free text (35) |

## Viewing HK FPS Payments

The user can perform the following with the HK FPS payments:

- View by using the standard enquiry ‘Pending and Processed Payments’.
- Filter by searching with *Channel* as HKFPSINST.

It also allows advanced filtering on the payment attributes (if required).






The user can view the payment and related details with the help of the following icons in the Enquiry page:

| Icon | Description | Screenshot |
| --- | --- | --- |
|  | View the Payment |  |
|  | View the details of the payment |  |

## Viewing the Incoming Return Payment

The user needs to perform the following actions:

1. On receiving the incoming return payment from HK FPS for an outgoing payment, it marks the original payment as returned and creates a new return payment is created.
2. To view the return payment in the existing Pending and Processed Payments page, search for the *Channel* as HKFPSINST and *Status Code* as 996.



## Understanding the HKFPSINST Reachability

Examples are provided below.

[Instant pacs.008 C1](#)

1. The configuration for the CT-PAYC01-CNY in the `CLEARING.DIRECTORY` application is done as per below.


2. Process the outgoing pacs.008 from the `PAYMENT.ORDER,HKFPSINSTAV` version with the payment type INST.


3. The payment is created and on running the medium service, the payment moves to 658. The reachability is successful.


4. The Audit Trail is updated as per below.


5. The `POR.SUPPLEMENTARY.INFO` record is updated as per below.

   [PDF](../../Resources/Images/Hong_Kong_FPS/POR.SUPP-BNK23108HBKHMFG0.pdf)

[Instant pacs.008 C2](#)

1. The `CA.CLEARING.DIRECTORY` application has been configured for CT-PAYC02-CNY.
2. Process the outgoing pacs.008 from the `PAYMENT.ORDER,HKFPSINSTAV` version.


3. The payment is created and on running the medium service, the payment moves to 658.


4. The Audit Trail is updated as per below.



In this topic

- [Working with Hong Kong Faster Payments System (HK FPS)](#WorkingwithHongKongFasterPaymentsSystemHKFPS)
  - [Capturing a HK FPS Payment Manually](#CapturingaHKFPSPaymentManually)
  - [Viewing HK FPS Payments](#ViewingHKFPSPayments)
  - [Viewing the Incoming Return Payment](#ViewingtheIncomingReturnPayment)
  - [Understanding the HKFPSINST Reachability](#UnderstandingtheHKFPSINSTReachability)




Copyright © 2020-2026 Temenos Headquarters SA

Cookie Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Wednesday, June 17, 2026 2:15:08 PM IST