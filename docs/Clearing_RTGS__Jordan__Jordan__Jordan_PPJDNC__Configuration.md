# Configuring Jordan RTGS

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Jordan/Jordan/Jordan_PPJDNC/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Jordan > [Jordan RTGS](../../Jordan/Jordan_PPJDNC/Introduction.htm) > Configuration

- Jordan;)
  - [Jordan RTGS Jordan RTGS](../../Jordan/Jordan_PPJDNC/Introduction.htm)
    - [Introduction](../../Jordan/Jordan_PPJDNC/Introduction.htm)
    - [Configuration](../../Jordan/Jordan_PPJDNC/Configuration.htm)
    - [Working with](../../Jordan/Jordan_PPJDNC/Working with.htm)
    - [Tasks](../../Jordan/Jordan_PPJDNC/Tasks.htm)
    - [Outputs](../../Jordan/Jordan_PPJDNC/Outputs.htm)

Payments

# Configuring Jordan RTGS

Updated On 06 July 2023 |
 3 Min(s) read

Feedback
Summarize

Temenos Payment Hub (TPH) bank can be a direct participant of Jordan RTGS (JO – RTGS). The channel through which it routes the payment determines the participation type in TPH. TPH comes with already available configuration records for Jordan RTGS. The following are the important parameters to configure the JO – RTGS:

## Direct Participant

The user can configure Jordan RTGS for a direct participant. To perform this, do the following:

1. Go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing**.



2. Enter the required details in the following fields:

| Field | Description |
| --- | --- |
| *Swift Based* | Set to Y (as Jordan RTGS is a SWIFT-based clearing) |
| *Settlement Type* | Set to GROSS (as Jordan RTGS is an RTGS settlement system) |
| *Service Identifier* | Set to JOD to populate in the tag 103 of the outgoing message (which denotes Jordan RTGS payment) |
| The above fields are important elements that determine the uniqueness and behavior of payments in a clearing. | |
| *Clearing Country Code* | Set to JO (as the country code for JORDAN is JO) |
| *RTGS System* | Set to Y (as Jordan RTGS is a RTGS system) |
| *Skip Reachability* | Set to Y (if reachability check is not required for to send Jordan RTGS system) |
| *Clearing File Transaction Indicator* | Set to T (as Jordan RTGS is based on the transaction) |
| *Clearing Currency* | Set to JOD (as TPH currently supports only JOD currency for Jordan RTGS payments) |

3. To define further characteristics of the payment based on direction, go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing Setting**. The below screen shows the setup for Outgoing MT103 messages.



Similarly, the user can configure different message types (MT103, MT202) and directions of payments (Incoming and Outgoing).

4. Enter the required details in the following fields:

| Field | Description |
| --- | --- |
| *Message Direction* | Direction of the payment for which this Clearing Setting record is created. |
| *Clearing Account Number* | Clearing account (nostro) of the clearing in the clearing currency. |
| *Message Payment Type* | Type of message for which the clearing setting record is created. For example, 103, 202.  This needs to be either 103 or 202, as TPH currently supports only these messages for Jordan RTGS clearing. |

## Clearing Cut-Off

The user can configure different cut-off times for customer transfer (MT103) and bank transfer (MT202) in TPH. To perform this, do the following:

Go to **Admin Menu**>**Payments Hub**>**Routing & Settlement**>**Channel Cut-off**.



In this topic

- [Configuring Jordan RTGS](#ConfiguringJordanRTGS)

- [Direct Participant](#DirectParticipant)
- [Clearing Cut-Off](#ClearingCutOff)




Copyright © 2020-2026 Temenos Headquarters SA

Cookie Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:19:02 PM IST