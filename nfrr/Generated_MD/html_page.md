# Canada.ca

# FINTRAC

# Guidance and resources for businesses (reporting entities)

# Methods to report to FINTRAC

# Batch Reporting

# Batch reporting to FINTRAC

Module 3: Large Cash Transaction Report specifications

Updated on October 23, 2023

From: Financial Transactions and Reports Analysis Centre of Canada (FINTRAC)

These specifications are available for reporting entities to be able to submit and change previously submitted Large Cash Transaction Reports through batch reporting for transactions that are dated before November 6, 2023.

# Important change as of November 6, 2023

Reporting entities must submit or change Large Cash Transaction Reports for transactions that have occurred as of November 6, 2023 or later through the FINTRAC API report submission.

Version 3.4.2

Includes specifications for Large Cash Transaction Reports (LCTR)

# 5.2.2 Detailed specification layout (Format version 03) — Large Cash Transaction Report

The following specifications outline the format for Large Cash Transaction Reports (LCTR) included in a batch, based on batch report format version "03".

Changes to this module are editorial revisions only. There are no legislative changes or changes in format.
---
Any report parts that are not applicable do not need to be included. However, all fields in each applicable part must be included, unless you are deleting a report (as explained in Section 3.4 and Part A below). If any fields in applicable parts have no data, pad those fields with spaces or zeros according to the required field format.

For additional information about Large Cash Transaction Report fields, refer to:

Reporting large cash transactions to FINTRAC

The layout for each LCTR report will be as follows, with all the parts of each transaction together:

- Part A
- Transaction 1
- Transaction 2, etc. (if there is more than one transaction to include in the report)

You can choose either of the following layouts for the parts of each transaction in your LCTR reports:

- Part B1, Part B2, Part D or E, if applicable, and any of Parts C, F or G that are applicable; or
- Part B1, Part B2, Part C if applicable, Part F or G if applicable, and Part D or E if applicable.

Note: If the LCTR transaction involved a business account and was a night deposit or a quick drop, Parts D, E, F and G do not apply to the report for that transaction.

An LCTR should only contain one transaction, unless it is about two or more cash transactions of less than $10,000 made within 24 consecutive hours of each other that total $10,000 or more.

# Part A: Information about where the transaction took place

This part is for information about you, reporting entity required to report the transaction to FINTRAC. It is also for information about the physical location where the transaction took place. If you need more information about what type of person or entity is a reporting entity, see the series of guidelines prepared by FINTRAC to explain reporting and other obligations.
---
If you have multiple branch or office locations, the information in this section should be about the branch or office location where the transaction took place. Transactions that happened at different branch or office locations should be reported on separate reports.

|Field No.|Field Name|Format|Comment|
|---|---|---|---|
|±|Part ID|X(2)|“A1”|
|±|Report|9(5)RJZ|Report sequence number within the preceding sub-header sequence number|
|±|Reporting entity report reference number|X(20)LJ|A unique report reference number is required for each report submitted from the same reporting entity. If you need to access this report in F2R, as explained in Section 3.4.2, this information will be in field 6A in Part A.|
|±|Action code|X(1)|If you are submitting a new batch (batch type “A”), enter “A” to indicate there is no change or deletion as this is a new report. If you are submitting a correction batch (batch type “C”), indicate whether this report is to be changed or deleted from a previously accepted batch. To change a report, use the action code “C” and complete the rest of the report. To delete a report, use the action code “D”. After you have provided your reporting entity's identifier number in field A1, immediately delimit that report with carriage return, line feed (&lt;CRLF&gt;). Continue with the next report or the batch trailer, as appropriate.|
---
# Reporting

# 1. Entity's Identifier Number

Enter your seven-digit identifier number assigned to you by FINTRAC at enrolment. For more information about this, contact your F2R administrator. This field is mandatory. If it is invalid, the entire batch will be rejected.

# 1A. Entity's Location Number

This represents information about where the transaction took place. Location numbers are assigned during the FINTRAC enrolment process and maintained by your F2R administrator. For more information about this, contact your F2R administrator.

For deposit taking institutions, this number is the branch portion of your transit number with leading zeroes. For example, the location number for branch 02831 of bank number 0004 would be 02831. For other types of reporting entities, this number will be created and assigned to you by FINTRAC. This field is mandatory. If it is invalid, the report will be rejected.

# 7. Contact's Surname

Enter the surname of the individual FINTRAC can contact for clarification about this report. This field is mandatory. If it is not included, the report will be rejected.

# 8. Contact's Given Name

Enter the given name of the individual FINTRAC can contact for clarification about this report. This field is mandatory. If it is not included, the report will be rejected.

# 9. Contact's Other Name/Initial

Enter the middle initial or other name of the individual FINTRAC can contact for clarification about this report.
---
# Contact

|X(20)LJ|Enter the telephone number of the individual contact for clarification. Include the extension in field A10A if applicable.|
|---|---|
| |Format 999-999-9999.|
| |This field is mandatory. If it is not included, the report will be rejected.|

# Contact person telephone extension number

9(10)RJZ
Enter the telephone extension number, if available.
---
# Type of reporting entity

Enter the appropriate code to indicate the type of activity applicable to the transaction that took place.

|Code|Description|
|---|---|
|A|Accountant|
|B|Bank|
|C|Caisse populaire|
|D|Agent of the Crown that sells or redeems money orders|
|E|Casino|
|F|Co-op credit society|
|G|No longer applicable for this field|
|H|No longer applicable for this field|
|I|Life insurance broker or agent|
|J|Life insurance company|
|K|Money services business|
|L|Provincial savings office|
|M|Real estate|
|N|Credit union|
|O|Securities dealer|
|P|Trust and/or loan company|
|Q|British Columbia notary|
|R|Dealer in precious metals and stones|
|S|Credit union central|
|T|Financial services cooperative|

This field is mandatory. If it is not included, the report will be rejected.
---
# 24-hour rule

9(1) If the transaction being reported is of $10,000 or more, enter “0”. In this case, the report should only contain one transaction otherwise the report will be rejected. If a report contains two or more cash transactions of less than $10,000 made within 24 consecutive hours of each other that total $10,000 or more, enter “1”. In this case, the LCTR will have more than one transaction. This field is required. If it is invalid, the report will be rejected. If you need to access this report in F2R, as explained in Section 3.4.2, this information will be in the box above field 1 in Part A.

Total characters in Part A: 127 - Each LCTR must include Part A.

# Part B1: Information about transaction

Updated on October 23, 2023

This part is for information about the large cash transaction. If the large cash transaction was two or more cash transactions of less than $10,000 made within 24 consecutive hours of each other that total $10,000 or more, include those in the same report. If there are more than 99 such transactions that make up a large cash transaction, you will have to use more than one report.

|Field No.|Field Name|Format|Comment|
|---|---|---|---|
|±|Part ID|X(2)|“B1”|
|±|Part sequence number|9(2)RJZ|Sequence number of the reportable transaction included in the report, beginning at 01, to a maximum of 99.|
---
# Large Cash Transaction Report

|*1|Date of transaction|X(8)LJ|
|---|---|---|
|Enter the date of the large cash transaction. If the transaction was outside normal business hours, and you do not have the date, use the night deposit indicator in field B3. Date format YYYYMMDD. Date must be no earlier than the coming into force date of January 31, 2003, and must be before November 6, 2023 for this report type. It cannot be a future date and must be the same as or earlier than the posting date (if one is entered in field B4). This field is mandatory, unless you indicate that the transaction was a night deposit in field B3. In this case if you do not provide the date of transaction in this field, you must provide the date of posting in field B4.|Enter the date of the large cash transaction. If the transaction was outside normal business hours, and you do not have the date, use the night deposit indicator in field B3. Date format YYYYMMDD. Date must be no earlier than the coming into force date of January 31, 2003, and must be before November 6, 2023 for this report type. It cannot be a future date and must be the same as or earlier than the posting date (if one is entered in field B4). This field is mandatory, unless you indicate that the transaction was a night deposit in field B3. In this case if you do not provide the date of transaction in this field, you must provide the date of posting in field B4.|Enter the date of the large cash transaction. If the transaction was outside normal business hours, and you do not have the date, use the night deposit indicator in field B3. Date format YYYYMMDD. Date must be no earlier than the coming into force date of January 31, 2003, and must be before November 6, 2023 for this report type. It cannot be a future date and must be the same as or earlier than the posting date (if one is entered in field B4). This field is mandatory, unless you indicate that the transaction was a night deposit in field B3. In this case if you do not provide the date of transaction in this field, you must provide the date of posting in field B4.|
|2|Time of transaction|X(6)LJ|
|Enter the time of the large cash transaction. If the transaction was outside normal business hours, and you do not have the time, use the night deposit indicator in field B3. Time format HHMMSS (space-fill if time not available). This field requires reasonable efforts.|Enter the time of the large cash transaction. If the transaction was outside normal business hours, and you do not have the time, use the night deposit indicator in field B3. Time format HHMMSS (space-fill if time not available). This field requires reasonable efforts.|Enter the time of the large cash transaction. If the transaction was outside normal business hours, and you do not have the time, use the night deposit indicator in field B3. Time format HHMMSS (space-fill if time not available). This field requires reasonable efforts.|
|*3|Night deposit or quick drop indicator|9(1)|
|If the transaction was a night deposit enter a “1” in this field. If it was a quick drop, enter a “3”. Otherwise, enter “0”or “9”. This field is mandatory if there is no date of transaction indicated in field B1.|If the transaction was a night deposit enter a “1” in this field. If it was a quick drop, enter a “3”. Otherwise, enter “0”or “9”. This field is mandatory if there is no date of transaction indicated in field B1.|If the transaction was a night deposit enter a “1” in this field. If it was a quick drop, enter a “3”. Otherwise, enter “0”or “9”. This field is mandatory if there is no date of transaction indicated in field B1.|
---
# 4. Date of transaction

X(8)LJ Enter the date the transaction cleared, if this differs from the posting date of the transaction provided above. Date must be no earlier than the coming into force date of January 31, 2003, and must be before November 6, 2023 for this report type. It cannot be a future date and must be the same as or later than the transaction date. Date format YYYYMMDD. This field is mandatory if the transaction was a night deposit (code 1 in field B3) and you were unable to provide the date of transaction in field B1. In all other cases, this field requires reasonable efforts.

# 5. Amount of transaction

X(15)d Enter the total of funds involved in the transaction, including two decimal places. This is the total amount received to start the transaction. What happens to that total will be explained in Part B2 as one or more dispositions. If this amount was not in Canadian funds, you do not have to convert it but provide the currency information in field B6. This field is mandatory. If it is not included, the report will be rejected.

# 6. Transaction currency

X(3)LJ Enter the currency of the transaction, even if it was in Canadian funds. Refer to the currency code table in the technical documentation area of the Publications page on FINTRAC's Web site. This field is mandatory. If it is not included, the report will be rejected.
---
# How the transaction was conducted

Enter the appropriate code to indicate how the transaction was conducted. If the selections provided do not cover this particular transaction, indicate “Other” and provide details in field B7A.

|Code|Description|
|---|---|
|A|In-branch/Office/Store|
|B|ABM (Automated banking machine)|
|C|Armoured car|
|D|Courier|
|E|Mail deposit|
|F|This code is no longer used for this field|
|G|Other|
|H|Night deposit (must be used if "1" is entered at field B3)|
|I|Quick drop (must be used if "3" is entered at field B3)|

This field is mandatory. If it is not included, the report will be rejected.

# Other description

Provide a description of “Other” as explained above. This field is required if code “G” is entered in field B7.

Total characters in Part B1: 66 - Each LCTR must include Part B1.

# Part B2: Information about transaction disposition

This part is for information about how the transaction was completed (i.e., where the money went).

If the disposition was on behalf of an entity (other than an individual), refer to Part F.

If the disposition was on behalf of another individual, refer to Part G.

Provide information about the individual conducting the transaction as explained in
---
Part D or Part E. If the transaction had no other dispositions than a deposit to a business account, refer to Part E. If the transaction involved a disposition that was not a deposit to a business account, refer to Part D.

|Field No.|Field Name|Format|Comment|
|---|---|---|---|
|±|Part ID|X(2)|“B2”|
|±|Part sequence|9(2)RJZ|Sequence number of the disposition beginning at 01. If you need to enter more than one disposition for a particular transaction, you do so by including another disposition record with the part sequence number incremented by one, to a maximum of 30, once you have entered all information for the previous disposition.|
---
# Disposition of X(1)LJ

Enter the appropriate code to indicate what happened to the funds involved in the transaction. If the selections provided do not cover this particular disposition, indicate “Other” and provide details in field B8A.

|Code|Description|
|---|---|
|A|Deposit to an account|
|B|Outgoing electronic funds transfer|
|C|Conducted currency exchange|
|D|Purchase of casino chips|
|E|Purchase of bank draft|
|F|Purchase of money order|
|G|Purchase of traveller's cheques|
|H|Life insurance policy purchase or deposit (provide number in field B8B)|
|I|Securities purchase or deposit|
|J|Real estate purchase or deposit|
|K|Cash out|
|L|Other|
|M|Purchase diamonds|
|N|Purchase jewellery|
|O|Purchase precious metals|
|P|Purchase stones (excl. diamonds)|
|Q|Added to virtual currency wallet|
|R|Exchange to virtual currency|
|S|Outgoing virtual currency transfer|

This field is mandatory. If it is not included, the report will be rejected.

# 8A Other

Provide a description of “Other” as explained above. This field is required if code “L” is entered in field B8.
---
# Life insurance

|*8|Life insurance policy number|X(30)LJ|Provide life insurance policy number if disposition was a “Life insurance policy purchase or deposit”. This field is required if code “H” is entered in field B8.|
|---|---|---|---|
|*9|Amount of disposition|X(15)d|Enter the amount of funds involved in the disposition, including two decimal places. If the amount was not in Canadian funds, you do not have to convert it but provide the currency information in field B10. This field is mandatory. If it is not included, the report will be rejected.|
|*10|Disposition currency|X(3)LJ|Enter the currency of the disposition, even if it was in Canadian funds. Refer to the currency code table in the technical documentation area of the Publications page on FINTRAC's Web site. This field is mandatory. If it is not included, the report will be rejected.|
|*11|Other institution name and number or other person or entity|X(35)LJ|This is for additional information about the funds described in field B8. Provide the name including the identification number if applicable of any other institution involved in the disposition or provide the name of any other person or entity involved in the disposition. This field is mandatory if applicable.|
|*12|Other person or entity account or policy number|X(30)LJ|This is for additional information about the funds described in field B8. Provide the account number if applicable of any other person or entity involved in the disposition. Also provide any policy number related to the other person or entity, if applicable. This field is mandatory if applicable.|
---
# On behalf of X(1)LJ

Enter the appropriate code to indicate on whose behalf the disposition of funds is made.

|Code|Description|
|---|---|
|C|Not applicable (on behalf of self, complete Part D)|
|E|On behalf of an entity (complete Part D or Part E, as appropriate, and complete Part F)|
|F|On behalf of another individual (complete Part D and Part G)|
|G|Employee depositing cash to employer's business account (complete Part E). To include Part E, for all dispositions within a transaction, the disposition of funds in field B8 must be "A" (deposit to an account) and account type in field C3 must be "B" (business).|

This field is required. If it is invalid, the report will be rejected. If you need to access this report in F2R, as explained in Section 3.4.2, this information will be at the top of Part B2 (above field 8).

Total characters in Part B2: 139 - Each LCTR must include Part B2.

# Part C: Account information (if applicable)

This part is for information about the account if the transaction was in fact related to an account. As explained earlier, it is possible to have more than one transaction per report, and more than one disposition per transaction. Provide the account information, if applicable, for each transaction included in the report. If the related
---
disposition was a “Deposit”, this part is required. If a transaction was not related to an account, do not include Part C in the report for that transaction.

|Field No.|Field Name|Format|Comment|
|---|---|---|---|
|±|Part ID|X(2)|“C1”|
|±|Part sequence number|9(2)RJZ|Sequence number of the account information related to the disposition of funds (must match the part sequence number of the corresponding disposition in Part B2).|
|*1|Branch or transit number|X(12)LJ|Enter the branch number, transit number, or other appropriate identifying number of the entity where the relevant account is held, when applicable to the transaction. For example, if it is a bank account, enter the five-digit bank branch number and space-fill the rest of the field. This field is mandatory if this part is applicable. If the disposition of funds in field B8 is Code “A” (deposit to an account), and this part is not included, the report will be rejected.|
|*2|Account number|X(30)LJ|Enter the number of the relevant account. This field is mandatory if this part is applicable. If the disposition of funds in field B8 is Code “A” (deposit to an account), and this part is not included, the report will be rejected.|
---
# 3 Account type

X(1)LJ Enter the appropriate code to indicate the type of the relevant account. If the selections do not cover this particular account, indicate “Other” and provide details in field C3A.

|Code|Description|
|---|---|
|A|Personal|
|B|Business|
|C|Trust|
|D|Other|

This field is mandatory if this part is applicable. If the disposition of funds in field B8 is Code “A” (deposit to an account), and this part is not included, the report will be rejected.

# 3A Other description

X(20)LJ Provide a description of “Other” as explained above. This field is required if “D” is entered in field C3.

# 4 Account currency

X(3)LJ Enter the type of currency for the relevant account. Refer to the currency code table in the technical documentation area of the Publications page on FINTRAC's Web site.

This field is mandatory if this part is applicable. If the disposition of funds in field B8 is Code “A” (deposit to an account), and this part is not included, the report will be rejected.
---
# Account Holder Information

|*5A|Account holder 1|X(45)LJ|Enter the full name of each account holder, up to three. If there are more than three, you need not provide more. This field is mandatory if this part is applicable. If the disposition of funds in field B8 is Code “A” (deposit to an account), and this part is not included, the report will be rejected.|
|---|---|---|---|
|*5B|Account holder 2|X(45)LJ|Enter the full name of each account holder, up to three. If there are more than three, you need not provide more. This field is mandatory if this part is applicable. If the disposition of funds in field B8 is Code “A” (deposit to an account), and this part is not included, the report will be rejected.|
|*5C|Account holder 3|X(45)LJ|Enter the full name of each account holder, up to three. If there are more than three, you need not provide more. This field is mandatory if this part is applicable. If the disposition of funds in field B8 is Code “A” (deposit to an account), and this part is not included, the report will be rejected.|

Total characters in Part C: 205 - If a transaction was not related to an account, do not include Part C in the report for that transaction.

# Part D: Information about the individual conducting the transaction that is not a deposit into a business account (if applicable)

This part is for information about the individual who conducted the transaction if this transaction was not a deposit into a business account. A business account is an account for a business, for a non-profit organization, etc. (i.e., one that is other than a personal or trust account). If the transaction and all its dispositions were a deposit.
---
to a business account, refer to the instructions for Part E.

As explained earlier, it is possible to have more than one transaction per report. Provide this information for each applicable transaction if at least one disposition is not a deposit into a business account. For example, if there were two dispositions for a particular transaction and they were both deposits to a business account (other than a night deposit or a quick drop), you would complete Part E. If one of the dispositions was other than a deposit to a business account, you would complete Part D.

|Field No.|Field Name|Format|Comment|
|---|---|---|---|
|±|Part ID|X(2)|“D1”|
|±|Part sequence number|9(2)RJZ|Sequence number of the individual conducting the transaction (must match the part sequence number of the corresponding transaction in Part B1).|
|*1|Surname|X(20)LJ|Enter the last name of the individual who conducted the transaction. This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D1 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
---
# 2

Given name X(15)LJ

Enter the first name of the individual who conducted the transaction. This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D2 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 3

Other name/initial X(10)LJ

Enter the middle initial or other name (if applicable) of the individual who conducted the transaction. This field requires reasonable efforts, if this part is applicable.

# 4

Entity client number X(12)LJ

Enter the client number issued to the individual who conducted the transaction, if applicable. This field is mandatory if applicable, if this part is applicable.

# 5

Street address X(30)LJ

Enter the civic address of the individual who conducted the transaction. This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D5 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.
---
# Transaction Information

|*6|City|X(25)LJ|Enter the town or city of the individual who conducted the transaction.|
|---|---|---|---|
|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D6 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D6 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D6 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D6 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
|*7|Country|X(2)LJ|Enter the country of the individual who conducted the transaction.|
|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D7 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D7 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D7 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D7 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
|*8|Province/State|X(20)LJ|Enter the province or state of the individual who conducted the transaction.|
|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D8 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D8 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D8 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D8 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
---
# 9. Postal/zip code

X(9)LJ Enter the postal or zip code of the individual who conducted the transaction. This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D9 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 10. Country of residence

X(2)LJ Enter the country of permanent residence of the individual who conducted the transaction. Refer to the country code table in the technical documentation area of the Publications page on FINTRAC's Web site. This field requires reasonable efforts, if this part is applicable.

# 11. Home telephone number

X(20)LJ Enter the home telephone number of the individual who conducted the transaction. This field requires reasonable efforts, if this part is applicable. Field D11A, home telephone extension number, has been eliminated.
---
# 12 Individual's

X(1)LJ Enter the appropriate code to indicate the document identifier used to identify the individual who conducted the transaction. If the selections provided do not cover the identifier used, indicate “Other” and provide details in field D12A.

|Code|Description|
|---|---|
|A|Driver's licence|
|B|Birth certificate|
|C|Provincial health card|
|D|Passport|
|E|Other|
|F|Record of Landing or Permanent residence card|

This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D12 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 12A Other description

X(20)LJ Provide a description of “Other” as explained above. This field is required if code “E” is entered in field D12.
---
# Document Identification Fields

# 13 ID number

X(20)LJ Enter the number of the document described in field D12 or D12A that was used to identify the individual who conducted the transaction. This field is mandatory if this part is applicable. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D13 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field. Note: A social insurance number (SIN) should not be provided in this field. If the identifier document described in field D12A is a SIN card, space-fill this field.

# 14 Country of issue

X(2)LJ Enter the country of issue of the document used to identify the individual who conducted the transaction. This field is mandatory if this part is applicable. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D14 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.
---
# 15

# Province/State of issue

X(20)LJ  Enter the province or state of issue of the document used to identify the individual who conducted the transaction.

If the country of issue is Canada, field D15 must contain a valid Canadian province or territory. If it is the United States or Mexico, field D15 must contain a valid state. Refer to the relevant code tables in the technical documentation area of the Publications page on FINTRAC's Web site for valid provinces, territories and states.

This field is mandatory if this part is applicable. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D15 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 16

# Individual's date of birth

X(8)LJ    Enter the date of birth of the individual who conducted the transaction.

Date format YYYYMMDD. Must be within the past 120 years, and cannot be a future date.

This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D16 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.
---
# Part D: Information about the individual conducting the transaction

|17|Individual's occupation|X(30)LJ|Enter the occupation of the individual who conducted the transaction.|
|---|---|---|---|
|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D17 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D17 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D17 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|This field is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field D17 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
|18|Individual's business telephone number|X(20)LJ|Enter the business telephone number of the individual who conducted the transaction.|
|This field requires reasonable efforts, if this part is applicable.|This field requires reasonable efforts, if this part is applicable.|This field requires reasonable efforts, if this part is applicable.|This field requires reasonable efforts, if this part is applicable.|
|18A|Individual's business telephone extension number|9(10)RJZ|Enter the telephone extension number, if available.|

Total characters in Part D: 300 - Each LCTR transaction must include either Part D or Part E, unless the transaction was a night deposit or a quick drop to a business account (in this case, neither Part D nor Part E is required).

# Part E: Information about the individual conducting the transaction that is a deposit into a business account (other than a quick drop or night deposit) (if applicable)

This part is for information about the individual who conducted the transaction if this transaction and all its dispositions were a deposit into a business account (other than a quick drop or a night deposit). A business account is an account for a business, for a non-profit organization, etc. (i.e., one that is other than a personal or trust account). If any of the dispositions were other than a deposit to a business account, Part D must be completed.

As explained earlier, it is possible to have more than one transaction per report.
---
Provide Part E information for each applicable transaction if all dispositions for a transaction are a deposit into a business account.

Note: To include Part E for a transaction, the on behalf of indicator in Part B2 (field B13) has to be “E” or “G” and for all dispositions within a transaction, the disposition in Part B2 (field B8) has to be “A”. Also, account type in field C3 has to be “B”.

|Field No.|Field Name|Format|Comment|
|---|---|---|---|
|±|Part ID|X(2)|“E1”|
|±|Part Sequence Number|9(2)RJZ|Sequence number of the individual conducting the transaction (must match the part sequence number of the corresponding transaction in Part B1).|
|*1|Surname|X(20)LJ|Enter the last name of the individual who conducted the transaction. Field E1 is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field E1 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
|*2|Given name|X(15)LJ|Enter the first name of the individual who conducted the transaction. Field E2 is mandatory if this part is applicable. If this part is applicable, and it is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field E2 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
|3|Other name/initial|X(10)LJ|Enter the middle initial or other name (if applicable) of the individual who conducted the transaction. This field requires reasonable efforts, if this part is applicable.|
---
Total characters in Part E: 49 - Each LCTR transaction must include either Part D or Part E, unless the transaction was a night deposit or a quick drop to a business account (in this case, neither Part D nor Part E is required).

# Part F: Information about the entity on whose behalf the transaction was conducted (if applicable)

This part only applies if the disposition was conducted on behalf of a third party other than an individual, as indicated in Part B2. To include Part F, the on behalf of indicator in Part B2 (field B13) has to be “E”.

|Field No.|Field Name|Format|Comment|
|---|---|---|---|
|±|Part ID|X(2)|“F1”|
|±|Part sequence number|9(2)RJZ|Sequence number of the “on behalf of an entity” information related to the disposition of funds (must match the part sequence number of the corresponding disposition in Part B2).|
|*1|Corporation, trust or other entity name|X(35)LJ|Enter the full name of corporation or other entity on whose behalf the transaction was conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F1 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
---
# 2 Type of business

X(20)LJ Describe the type of business for the entity on whose behalf the transaction was conducted. This field is mandatory if this part is applicable. If this part is applicable, and these fields are not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F2 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 3 Street address

X(30)LJ Enter the civic address of the entity on whose behalf the transaction was conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F3 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 4 City

X(25)LJ Enter the town or city of the entity on whose behalf the transaction was conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F4 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.
---
# Transaction Reporting Fields

|*5|Country|X(2)LJ|Enter the country of the entity on whose behalf the transaction was conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F5 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
|---|---|---|---|
|*6|Province/State|X(20)LJ|Enter the province or state of the entity on whose behalf the transaction was conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F6 was not obtained at the time of the transaction (and is not available from your records), you can space-fill these fields.|
|*7|Postal/zip code|X(9)LJ|Enter the postal or zip code of the entity on whose behalf the transaction was conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F7 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
|8|Business telephone number|X(20)LJ|Enter the telephone number of the entity on whose behalf the transaction was conducted. This field requires reasonable efforts, if this part is applicable.|
---
# 8A Business telephone number extension

Enter the telephone extension number, if available.

# 9 Incorporation number

Enter the incorporation number if the entity is a corporation. This field is mandatory if applicable, if this part is applicable. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F9 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field. If an incorporation number does not exist for a corporation, space-fill this field.

# 10 Country of issue

Provide the country of issue of the incorporation number of the entity on whose behalf the transaction was conducted (if it was a corporation). This field is mandatory if applicable, if this part is applicable. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F10 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field. If an incorporation number does not exist for a corporation, space-fill field F10.
---
# Province/State of issue

X(20)LJ Provide the province or state of issue of the incorporation number of the entity on whose behalf the transaction was conducted (if it was a corporation).

If the country of issue is Canada, field F11 must contain a valid Canadian province or territory. If it is the United States or Mexico, field F11 must contain a valid state. Refer to the relevant code tables in the technical documentation area of the Publications page on FINTRAC's Web site for valid provinces, territories and states.

This field is mandatory if applicable, if this part is applicable. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field F11 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

If an incorporation number does not exist for a corporation, space-fill field F11.

# Individuals authorized to bind the entity or act with respect to the account

# Individual's name 1

X(35)LJ Provide the name of an individual who is authorized to bind the entity or act with respect to the account. This field requires reasonable efforts, if this part is applicable.

# Individual's name 2

X(35)LJ Provide the name of an individual who is authorized to bind the entity or act with respect to the account. This field requires reasonable efforts, if this part is applicable.
---
# 12C Individuals

Provide the name of an individual who is authorized to bind the entity or act with respect to the account. This field requires reasonable efforts, if this part is applicable.

Individual's name 3

Total characters in Part F: 316 - Do not include Part F in the report for a transaction if it was not conducted on behalf of an entity or if an employee deposited cash in his or her employer's business account.

# Part G: Information about the individual on whose behalf the transaction was conducted (if applicable)

This part only applies when the disposition was conducted on behalf of a third party that is an individual. To include Part G, the on behalf of indicator in Part B2 (field B13) has to be “F”.

If the individual conducted the disposition on his or her own behalf, this part does not apply. In that case, information about the individual should be put in Part D. If the disposition was conducted on behalf of an entity (other than an employee depositing cash in his or her employer's business account), Part F should be completed.

|Field No.|Field Name|Format|Comment|
|---|---|---|---|
|±|Part ID|X(2)|“G1”|
|±|Part sequence number|9(2)RJZ|Sequence number of the “on behalf of an individual” related to the disposition of funds (must match the part sequence number of the corresponding disposition in Part B2).|
---
# 1 Surname

X(20)LJ Enter the surname of the individual on whose behalf the transaction is conducted.

Field G1 is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field G1 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 2 Given name

X(15)LJ Enter the given name of the individual on whose behalf the transaction is conducted.

Field G2 is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field G2 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 3 Other name/initial

X(10)LJ Enter the middle initial or other name (if applicable) of the individual on whose behalf the transaction is conducted.

This field requires reasonable efforts, if this part is applicable.
---
# 4. Street address

X(30)LJ Enter the civic address of the individual on whose behalf the transaction is conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field G4 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 5. City

X(25)LJ Enter the town or city of the individual on whose behalf the transaction is conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field G5 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.

# 6. Country

X(2)LJ Enter the country of the individual on whose behalf the transaction is conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field G6 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.
---
# Transaction Information

|*7|Province/State|X(20)LJ|Enter the province or state of the individual on whose behalf the transaction is conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field G7 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
|---|---|---|---|
|*8|Postal/zip code|X(9)LJ|Enter the postal or zip code of the individual on whose behalf the transaction is conducted. This field is mandatory if this part is applicable. If this part is applicable, and this field is not included, the report will be rejected. If the 24-hour rule indicator (“1”) is entered in field A12 and, because of this, information for field G8 was not obtained at the time of the transaction (and is not available from your records), you can space-fill this field.|
|9|Home telephone number|X(20)LJ|Enter the home telephone number of the individual on whose behalf the transaction is conducted. This field requires reasonable efforts, if this part is applicable. Field G9A, home telephone extension number, has been eliminated.|
|10|Office telephone number|X(20)LJ|Enter the office telephone number of the individual on whose behalf the transaction is conducted. This field requires reasonable efforts, if this part is applicable.|
---
# 10A

Office telephone extension number

Enter the telephone extension number, if available.

# 11

Individual's date of birth

Enter the date of birth of the individual on whose behalf the transaction is conducted.

Date format YYYYMMDD.

Must be within the past 120 years, and cannot be a future date.

This field requires reasonable efforts, if this part is applicable.

# 12

Individual's identifier

Enter the appropriate code to indicate the document used to identify the individual on whose behalf the transaction was conducted. If the selections provided do not cover the identifier used, indicate “Other” and provide details in field G12A.

|Code|Description|
|---|---|
|A|Driver's licence|
|B|Birth certificate|
|C|Provincial health card|
|D|Passport|
|E|Other|
|F|Record of Landing or Permanent residence card|

This field requires reasonable efforts, if this part is applicable.

# 12A

Other description

Provide a description of “Other” as explained above. This field is required if code “E” is entered in field G12.
---
# Document Identification

|13|ID number|X(20)LJ|Enter the number of the document described in field G12 or G12A that was used to identify the individual on behalf of whom the transaction was conducted. This field requires reasonable efforts, if this part is applicable. Note: A social insurance number (SIN) should not be provided in this field. If the identifier document described in field G12A is a SIN card, space-fill field G13.|
|---|---|---|---|
|14|Country of residence|X(2)LJ|Enter the country of permanent residence of the individual on whose behalf the transaction was conducted. Refer to the country code table in the technical documentation area of the Publications page on FINTRAC's Web site. This field requires reasonable efforts, if this part is applicable.|
|15|Country of issue|X(2)LJ|Enter the country of issue of the document used to identify the individual on whose behalf the transaction was conducted. This field requires reasonable efforts, if this part is applicable.|
---
# 16

Province/State

X(20)LJ Enter the province or state of issue of the document used to identify the individual on whose behalf the transaction was conducted.

If the country of issue is Canada, field G16 must contain a valid Canadian province or territory. If it is the United States or Mexico, field G16 must contain a valid state. Refer to the relevant code tables in the technical documentation area of the Publications page on FINTRAC's Web site for valid provinces, territories and states.

This field requires reasonable efforts, if this part is applicable.

# 17

Individual's occupation

X(30)LJ Enter the occupation of the individual on whose behalf the transaction was conducted.

This field requires reasonable efforts, if this part is applicable.
---
# Relationship to Individual

Enter the appropriate code to indicate the relationship of the person conducting the transaction to the individual on whose behalf the transaction is conducted. If the selections provided do not cover the relationship, indicate “Other” and provide details in field G18A.

|Code|Description|
|---|---|
|A|Accountant|
|B|Agent|
|C|Legal counsel|
|D|Borrower|
|E|Broker|
|F|Customer|
|G|Employee|
|H|Friend|
|I|Relative|
|J|Other|

This field requires reasonable efforts, if this part is applicable.

# Other Relationship

Provide a description of “Other” as explained above. This field is required if code “J” is entered in field G18.

Total characters in Part G: 309 - Do not include Part G in the report for a transaction if it was not conducted on behalf of another individual or if an employee deposited cash in his or her employer's business account.
---
# 5.3.2 LCTR Structure Flowchart

|Sart|Wrzeterston|
|---|---|
|(raattion niorator)|Frt 32|
|Droston intrnaton;|Frt C|
|iourt Inornator|Jositon tran ettyy|
|etpoy?- rena|rpoer|
|Jisoston|ote|
|Rranote|jspston?|
|3ocout:| |
|Ajirotar|Eioiepom|
|[snsicon:| |
---
# Start

Is it an employee depositing cash to employer's business account?

Is it quick drop night deposit? (On behalf of entity information)

# End of

# Startot?

wux

# Part 8

Jerost? (On behalf of information)
---
# Sartoic

# Quick CTop

# Fat D

eepoir

vival corjrttina

Erjofc

# Stmoc

# Jukctooc

# Fart [

(Namaotinaiviu

conjucon? tarsacton}

Eniod

Date Modified:

2023-10-23