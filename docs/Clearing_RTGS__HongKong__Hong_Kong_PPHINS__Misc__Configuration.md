# Configuring Hong Kong Faster Payments System (HK FPS)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/HongKong/Hong_Kong_PPHINS/Misc/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Hong Kong > [Hong Kong FPS](../../Hong_Kong_PPHINS/Misc/Introduction.htm) > Configuration

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

# Configuring Hong Kong Faster Payments System (HK FPS)

Updated On 07 August 2025 |
 3 Min(s) read

Feedback
Summarize

The following modules are configured to process HK FPS payments:

| Module | Description |
| --- | --- |
| `PAYMENT.ORDER` (`PO`) application | Helps manual capture of HK FPS payments |
| Temenos Payment Hub (TPH) | Helps processing of HK FPS payments |

## `PO` Application for Payment Capture

The user can configure PAYMENT.ORDER product. To perform this, do the following:

1. Go to **Admin Menu**>**Payments Hub**>**Payment Order Admin Menu**>**Payment Order Product Setup**.
2. Select the *Product Name* as HKFPSINST in the `PO` application.



3. Enter the required details in the following fields:

| Field | Description |
| --- | --- |
| *Reachability Check* | To enable the validation of reachability of beneficiary bank through HK FPS against HK FPS clearing directory, set as BIC. |
| *Pay Through Beneficiary* | To indicate that beneficiary is an external bank, set to Yes. |
| *Reserve Funds* | To indicate that the funds reservation happens in `PO` application, set as Yes. |
| *Check Transparency* | To indicate that simulation is done in payment system (TPH), set as Yes. |

## HK FPS Clearing in TPH

The user can configure HK FPS (an instant clearing system) in TPH. To perform this, do the following:

1. Go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing**.
2. Select the *Record ID* as HKFPSINST.









3. Enter the required details in the following field:

| Field | Description |
| --- | --- |
| *Outgoing Message Type* | Define the FPS message types as required (in ISO20022 format) |
| *RTGS System* | Set as I (as this is an instant clearing) |
| *Availability* | Set as 24By7 |

4. To define further characteristics of the payment based on message type and direction, go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing Setting**.






The user can configure the *HK FPS Clearing Account Number* and *Suspense Account Number*.

|  |  |  |
| --- | --- | --- |
| TPH Product Setup | Light Weight | To configure the HK FPS incoming payments from clearing, go to **Admin Menu**>**Payments Hub**>**Product Determination**>**Product Condition – Light**. |
| Medium Weight | To configure a product for outgoing HK FPS payments originating from `PO` application, go to **Admin Menu**>**Payments Hub**>**Product Determination**>**Product Condition – Medium**. |

To know more on the setup of product conditions, refer to [Products](../../Payments_Hub_(PP)/Product_Determination/Configuration.htm#top) and [Preferences](../../Payments_Hub_(PP)/Client_Condition/Configuration.htm#top) section.

## Reachability in HKFPSINST

The user can configure a record for the bank to be reachable through HKFPSINST. To perform this, do the following:

1. Go to **Admin Menu**>**Framework Parameter**>**Clearing Directory**.



2. Select the required details in the following fields: *Payment Channel, NCC, Scheme*, and *Currency*.

To know more, refer to [Clearing Directory](../../Clearing_Directory_(CA)/Misc/Configuration.htm#top).

## Configurations for FATF check for HKFPS payments

1. Enablefatfreg to be set as Y in PP.COMPANY.PROPERTIES.


In this topic

- [Configuring Hong Kong Faster Payments System (HK FPS)](#ConfiguringHongKongFasterPaymentsSystemHKFPS)
  - [PO Application for Payment Capture](#POApplicationforPaymentCapture)
  - [HK FPS Clearing in TPH](#HKFPSClearinginTPH)
  - [Reachability in HKFPSINST](#ReachabilityinHKFPSINST)
  - [Configurations for FATF check for HKFPS payments](#ConfigurationsforFATFcheckforHKFPSpayments)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Wednesday, June 17, 2026 2:15:06 PM IST