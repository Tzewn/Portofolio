# Fast Vertical Shorts

## Plan the parts first

- Confirm the source video, the target length for each part, the layout, the subtitle choice and the delivery format before you download anything.

- Expand the part count when the user asks for as many clips as the strong moments support, and plan the full batch before rendering.

- Pick the highlight moments from the source captions or transcript first, so you only fetch the segments you will actually render.

- Write down the start and end time for every part before rendering, and keep each part inside the length the user asked for.

## Match a reference style when the user shares one

- View a reference clip the user shares with `browser.browse` first, and describe its layout from what you saw before you try to download it.

- Name the layout elements you can match, such as a large facecam area, a hook banner, the main footage area and the subtitle style, and say plainly what you could not identify.

- State the limits before rendering, such as a small source facecam turning soft when enlarged and per word timing being estimated from sentence captions.

- Build one example part from files you already have before you remake a whole batch in a new style.

- Apply the style the user confirms to every remaining part, and keep the earlier version of each finished part unchanged.

## Get the source without hammering it

- Fetch only the segments you need when the source allows it, and reuse one downloaded segment for every part that overlaps it.

- Stop fetching from the source after a rate limit, a bot check, a timeout or an HTTP 403 response, and do not retry in a loop in the same session.

- Deliver the parts that are finished and name the parts still pending, instead of holding everything back for the blocked parts.

## Prepare the text early, with or without subtitles

- Prepare the subtitle file for every planned part before rendering the videos, so pending parts already have usable subtitles.

- Clean the source captions into readable lines in the requested language, and keep the separate subtitle file beside each rendered clip.

- Burn the subtitles into the vertical video only when the user wants them on the video, and still deliver the editable subtitle file.

- Keep the hook banner text when the user chooses a no subtitle version, and deliver the subtitle files as editable side files only.

## Render fast and check only the essentials

- Render vertical video at 1080 by 1920 with a fast preset when the user asks for speed, and skip frame by frame review and long companion documents.

- Check only the essentials on every finished part, which are the duration, the resolution, audible audio, the confirmed layout and subtitle choice, and a file that plays.

- Send each finished part as soon as it passes those checks, with its subtitle file, and say plainly which parts remain and why.

## Auto-Clip intake (merged from the user's Auto-Clip draft, 25 Nov 2026)

- Accept an Auto-Clip request in this shape: a long YouTube video or livestream link, an optional transparent PNG watermark (and optional outro file), and the user's choices for clip count, seconds per clip (default 60), layout (split or blur-bg) and subtitles on or off.

- Score the strongest moments from the transcript or auto-captions first, then give the user a candidate list with timestamps so the user picks which moments get rendered.

- Verify each candidate with a frame check so the clip is not an intro, logo or black screen before rendering.

- Render each clip at 1080 by 1920 with hook text and the channel name, overlay the watermark when supplied, and attach the outro at the end when supplied. Default output is a 60 second clip plus outro, H.264 video with AAC audio, and no subtitles unless the user asks for them.

- Send an image preview first; render the full video only after the preview looks right.

- Hand over the final video files plus a clip list naming each clip's source timestamp, hook and contents.

- Keep the limits plain: result quality follows the source (a 360p source stays soft), uploading to YouTube, TikTok or Instagram is a separate step outside this skill, and this is a general clipper, not a campaign-claim tool — some clipper campaigns ban AI or auto-clipping, and claim risk stays with the user.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [YouTube](https://www.youtube.com/) for confirming the source video title, duration and captions. Carry the exact video link into `browser.browse` and verify the title and length before planning the parts.

## Alternatives for better results

- Ask the user to upload the source file when platform downloads keep failing, so rendering no longer depends on the platform.

- Deliver subtitles and timestamps first when video rendering is blocked, so the user can still review or post the text parts.

- Use a connected clip connector when local rendering is slow, and keep the same essential checks on the result.
