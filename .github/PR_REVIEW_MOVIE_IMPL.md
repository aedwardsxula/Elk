# Review notes

This PR is a review wrapper for the recent changes pushed to  and contains a short summary for reviewers.

Recent commits (most recent first):

fe3b708 Remove local UML svg per user request
1726de3 Add unit tests for Movie: happy path and None rating
facfe57 Implement Movie class per UML: title, rating, plot, to_json
f97006d Stop tracking UML svg/png; allow lead to commit source files
317069a Add/update Assets/uml.vsdx — embed UML svg and place image on Page-1
13e4c45 Add best-effort UML .vsdx (embedded svg)

Summary of what changed:
- Implement  class per UML (fields: title, rating, plot; method: to_json)
- Add unit tests for  (happy path + None rating)
- Stop tracking  and , updated 
- Added  with embedded SVG and placed image shape on Page-1
- Cleaned up accidental pyc commits and updated 

Note: The substantive commits are already present on ; this PR contains only this small review helper commit so reviewers can use the PR UI to comment.
