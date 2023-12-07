const std = @import("std");

const Hand = struct { cards: [5]u8, bid: i32 };

pub fn main() !void {
    const allocator = std.heap.page_allocator;

    var file = try std.fs.cwd().openFile("input", .{});
    defer file.close();

    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();

    var buf: [1024]u8 = undefined;
    var hands = std.ArrayList(Hand).init(allocator);

    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var tokens = std.mem.tokenizeSequence(u8, line, " ");
        var bid: i32 = undefined;
        var i: i8 = 0;
        while (i < 2) : (i += 1) {
            const cards_slice = tokens.next() orelse break;
            const bid_str = tokens.next() orelse break;
            var buffer: [5]u8 = undefined;

            std.mem.copyBackwards(u8, &buffer, cards_slice);
            bid = try std.fmt.parseInt(i32, bid_str, 10);

            try hands.append(Hand{ .cards = buffer, .bid = bid });
        }
    }

    const hands_slice = try hands.toOwnedSlice();
    std.sort.insertion(Hand, hands_slice, {}, lessThanHand);
    var total: i32 = 0;
    var i: i32 = 1;
    for (hands_slice) |hand| {
        total += hand.bid * i;
        i += 1;
    }

    std.debug.print("{d}\n", .{total});
}

const HandType = enum(u8) { HIGH, PAIR, PAIR2, KIND3, FULLHOUSE, KIND4, KIND5 };
fn computeType(hand: Hand) HandType {
    var already_finded = [5]u8{ 0, 0, 0, 0, 0 };
    var count_finded = [_]i8{ 0, 0, 0, 0, 0 };

    for (hand.cards) |card| {
        for (&already_finded, 0..) |*card_finded, i| {
            if (card_finded.* == 0) {
                card_finded.* = card;
                count_finded[i] += 1;
                break;
            }

            if (card == card_finded.*) {
                count_finded[i] += 1;
                break;
            }
        }
    }

    var pairs: i8 = 0;
    var threes: i8 = 0;
    for (count_finded) |c| {
        switch (c) {
            5 => return HandType.KIND5,
            4 => return HandType.KIND4,
            3 => threes += 1,
            2 => pairs += 1,
            1 => {},
            0 => break,
            else => unreachable,
        }
    }

    if (threes == 1) {
        if (pairs == 1) return HandType.FULLHOUSE;
        return HandType.KIND3;
    }

    if (pairs == 1) return HandType.PAIR;
    if (pairs == 2) return HandType.PAIR2;

    return HandType.HIGH;
}

fn lessThanHand(context: void, lhs: Hand, rhs: Hand) bool {
    const r_type = computeType(rhs);
    const l_type = computeType(lhs);

    if (r_type != l_type) {
        return @intFromEnum(l_type) < @intFromEnum(r_type);
    }

    var i: u8 = 0;
    while (i < 5) : (i += 1) {
        if (lhs.cards[i] == rhs.cards[i]) {
            continue;
        } else {
            switch (rhs.cards[i]) {
                'A' => return true,
                'K' => return lhs.cards[i] != 'A',
                'Q' => return lhs.cards[i] != 'A' and lhs.cards[i] != 'K',
                'J' => return lhs.cards[i] != 'A' and lhs.cards[i] != 'K' and lhs.cards[i] != 'Q',
                'T' => return lhs.cards[i] != 'A' and lhs.cards[i] != 'K' and lhs.cards[i] != 'Q' and lhs.cards[i] != 'J',
                else => {
                    return lhs.cards[i] < rhs.cards[i];
                },
            }
        }
    }
    _ = context;

    return true;
}
